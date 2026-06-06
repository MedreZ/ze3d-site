#!/bin/bash
# backup-sources.sh
# Copie miroir du dossier Sources/ du projet vers le serveur pro (Synology Drive,
# sauvegardé automatiquement). Ne se déclenche que si Sources/ a changé depuis le
# dernier passage. Appelé par le hook "Stop" de Claude Code (et lançable à la main).
#
# Source : <projet>/Sources/
# Dest   : SynologyDrive-ZE3D/05 - SITE/01 - CLAUDE CODE/Sources/
#
# rsync --delete = vrai miroir (la copie reflète exactement Sources/). Synology
# conserve de toute façon ses propres versions, donc aucune perte définitive.

ROOT="/Users/emmanuelzerdoun/Documents/SITE WEB"
SRC="$ROOT/Sources"
DEST="/Users/emmanuelzerdoun/Library/CloudStorage/SynologyDrive-ZE3D/05 - SITE/01 - CLAUDE CODE/Sources"
STAMP="$ROOT/scripts/.sources-backup.stamp"

if [ ! -f "$STAMP" ] || [ -n "$(find "$SRC" -type f -newer "$STAMP" -print -quit 2>/dev/null)" ]; then
  mkdir -p "$DEST"
  rsync -a --delete --exclude='.DS_Store' "$SRC/" "$DEST/" >/dev/null 2>&1
  touch "$STAMP"
fi
exit 0
