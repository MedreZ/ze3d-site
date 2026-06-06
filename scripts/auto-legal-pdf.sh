#!/bin/bash
# auto-legal-pdf.sh
# Régénère automatiquement les PDF juridiques (Mentions légales / CGV) UNIQUEMENT
# si une source a changé depuis le dernier passage. Appelé par le hook "Stop"
# de Claude Code (donc à la fin de chaque tour où un fichier légal a été modifié).
# Le script Python ne régénère que le document réellement modifié et archive
# automatiquement l'ancienne version (cf. scripts/generate-legal-pdfs.py).

ROOT="/Users/emmanuelzerdoun/Documents/SITE WEB"
STAMP="$ROOT/scripts/.legal-pdf.stamp"
ML="$ROOT/src/pages/mentions-legales.astro"
CGV="$ROOT/src/pages/cgv.astro"
PY="/usr/local/bin/python3"

if [ "$ML" -nt "$STAMP" ] || [ "$CGV" -nt "$STAMP" ]; then
  "$PY" "$ROOT/scripts/generate-legal-pdfs.py" >/dev/null 2>&1
  touch "$STAMP"
fi
exit 0
