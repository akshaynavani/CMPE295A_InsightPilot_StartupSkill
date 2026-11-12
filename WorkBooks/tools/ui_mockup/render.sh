#!/bin/sh
# Render the UI mockup to assets/ch6_ui_mockup.png at 2x with headless Chrome.
HERE="$(cd "$(dirname "$0")" && pwd)"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=1700,1265 \
  --screenshot="$HERE/../../assets/ch6_ui_mockup.png" "file://$HERE/investigation_workspace.html"
