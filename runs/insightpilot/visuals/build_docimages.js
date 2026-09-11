// Build visuals/docimages.json: which rendered visuals belong to which artifact.
// Run from runs/<slug>/. Resolves bare filenames in the manifest's source column
// against the whole run tree, not just the top-level directories.
//
// ---------------------------------------------------------------------------
// RUN-LOCAL CHANGE vs. templates/build_docimages.js, made deliberately:
// the template maps PNG rasters only. This run has zero rasters (no text-to-image
// capability in the session that built phase 8) while all 53 HTML frames exist, so
// the template would report "0 placements" and list every artifact as unillustrated
// — which is false for the reader and makes A52b unverifiable.
//
// This version maps BOTH forms and labels each placement with its form, so:
//   - the A52b contract ("no substantive artifact left with zero illustrations")
//     can actually be checked, and
//   - the raster count is still reported honestly and separately as zero.
// A PNG wins over an HTML frame for the same visual id when both exist.
// ---------------------------------------------------------------------------
const fs = require('fs');
const path = require('path');

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.name === 'node_modules' || e.name.startsWith('.')) continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out);
    else if (e.name.endsWith('.md')) out.push(p.replace(/\\/g, '/'));
  }
  return out;
}

const allDocs = walk('.').map(p => p.replace(/^\.\//, ''));
const byBase = {};
for (const p of allDocs) (byBase[path.basename(p)] = byBase[path.basename(p)] || []).push(p);

// Rendered rasters, if any.
const pngs = {};
if (fs.existsSync('visuals/images')) {
  for (const f of fs.readdirSync('visuals/images').filter(f => /\.png$/i.test(f))) {
    const m = f.match(/^(V\d+)_/);          // V01..V112 - not a fixed slice
    if (m) pngs[m[1]] = f;
  }
}

// HTML frames.
const frames = {};
if (fs.existsSync('visuals/infographics')) {
  for (const f of fs.readdirSync('visuals/infographics').filter(f => /\.html$/i.test(f))) {
    const m = f.match(/^(V\d+)_/);
    if (m) frames[m[1]] = f;
  }
}

// One visual per id, raster preferred.
const visuals = {};
for (const [id, file] of Object.entries(frames)) visuals[id] = { file: `infographics/${file}`, form: 'html' };
for (const [id, file] of Object.entries(pngs)) visuals[id] = { file: `images/${file}`, form: 'png' };

const man = fs.readFileSync('visuals/visual_manifest.md', 'utf8');
const docImg = {};
const mermaidRows = [];
for (const line of man.split('\n')) {
  const m = line.match(/^\| (V\d+) \|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|/);
  if (!m) continue;
  const id = m[1];
  const title = m[2].trim();
  const form = m[5].trim();
  // Rows already satisfied by a Mermaid diagram inside their own source artifact
  // need no separate file; they still count as illustrating that artifact.
  if (form === 'mermaid') mermaidRows.push({ id, title, src: m[4].trim() });
  if (!visuals[id] && form !== 'mermaid') continue;
  const targets = new Set();
  for (const ref of (m[4].match(/[A-Za-z0-9_\/]+\.md/g) || [])) {
    const clean = ref.replace(/^\.\//, '');
    if (allDocs.includes(clean)) { targets.add(clean); continue; }
    const base = path.basename(clean);
    // unique basename match anywhere in the tree (D04.md -> tech/architecture/D04.md)
    if (byBase[base] && byBase[base].length === 1) targets.add(byBase[base][0]);
    else if (byBase[base]) {
      const hit = byBase[base].find(p => p.endsWith('/' + clean)) || byBase[base][0];
      targets.add(hit);
    }
  }
  const v = visuals[id] || { file: null, form: 'mermaid' };
  for (const t of targets) (docImg[t] = docImg[t] || []).push({ id, file: v.file, form: v.form, title });
}

fs.writeFileSync('visuals/docimages.json', JSON.stringify(docImg));
const all = Object.values(docImg).flat();
const byForm = all.reduce((a, p) => (a[p.form] = (a[p.form] || 0) + 1, a), {});
console.log(`docimages.json: ${Object.keys(docImg).length} documents, ${all.length} placements`);
console.log(`  by form: ${Object.entries(byForm).map(([f, n]) => `${f}=${n}`).join('  ')}`);
console.log(`  rasters on disk: ${Object.keys(pngs).length}   html frames on disk: ${Object.keys(frames).length}`);
const bare = allDocs.filter(d => !docImg[d] && !/^(visuals\/|audit\/|README\.md)/.test(d));
console.log(`still unillustrated (content docs): ${bare.length}`);
bare.forEach(b => console.log('   ' + b));

// Slug -> filename map, so documents can place a visual inline by slug
// (the pitch deck marks each slide "visual: V-star-curve").
const slugMap = {};
for (const [id, v] of Object.entries(visuals)) {
  const m = path.basename(v.file).match(/^V\d+_(.+)\.(png|html)$/);
  if (m) slugMap[m[1]] = v.file;
}
fs.writeFileSync('visuals/slugmap.json', JSON.stringify(slugMap));
console.log(`slugmap.json: ${Object.keys(slugMap).length} slugs`);
