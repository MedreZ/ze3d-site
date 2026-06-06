#!/bin/bash
# build-charte-pdf.sh
# Régénère le PDF de la charte graphique depuis son HTML et le place :
#   (1) en local : Sources/Charte graphique/Charte graphique - ZE3D.pdf
#   (2) sur le serveur pro : 00 - SOCLE/03 - CHARTE - ID VISUEL/01 - CHARTE GRAPHIQUE/
# Ne se régénère que si un fichier source de la charte (HTML ou image) a changé.
# Appelé par le hook "Stop" de Claude Code, et lançable à la main.

ROOT="/Users/emmanuelzerdoun/Documents/SITE WEB"
DIR="$ROOT/Sources/Charte graphique"
HTML="$DIR/charte-graphique-ZE3D.html"
PDF_LOCAL="$DIR/Charte graphique - ZE3D.pdf"
SYNO_DIR="/Users/emmanuelzerdoun/Library/CloudStorage/SynologyDrive-ZE3D/00 - SOCLE/03 - CHARTE - ID VISUEL/01 - CHARTE GRAPHIQUE"
STAMP="$ROOT/scripts/.charte-pdf.stamp"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

[ -f "$HTML" ] || exit 0

# Régénère seulement si le HTML ou une image de la charte est plus récent que le dernier passage.
if [ -f "$STAMP" ] && [ -z "$(find "$DIR" -type f ! -name '*.pdf' -newer "$STAMP" -print -quit 2>/dev/null)" ]; then
  exit 0
fi

URL="file://${HTML// /%20}"
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$PDF_LOCAL" "$URL" >/dev/null 2>&1
mkdir -p "$SYNO_DIR"
cp "$PDF_LOCAL" "$SYNO_DIR/Charte graphique - ZE3D.pdf"
cp "$HTML" "$SYNO_DIR/charte-graphique-ZE3D.html"   # source HTML rangée avec le PDF
touch "$STAMP"
exit 0
