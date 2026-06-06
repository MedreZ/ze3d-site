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

# ─── GARDE-FOU ANTI-EFFACEMENT ───────────────────────────────────────────────
# Si le dossier de travail Sources/ est ABSENT ou VIDE, on n'exécute PAS le miroir.
# => supprimer (ou renommer/déplacer) le dossier de travail ne supprime JAMAIS la
#    sauvegarde des sources sur le serveur (rsync --delete ne s'exécute pas).
if [ ! -d "$SRC" ] || [ -z "$(find "$SRC" -type f ! -name '.DS_Store' -print -quit 2>/dev/null)" ]; then
  exit 0
fi
# ─────────────────────────────────────────────────────────────────────────────

if [ ! -f "$STAMP" ] || [ -n "$(find "$SRC" -type f -newer "$STAMP" -print -quit 2>/dev/null)" ]; then
  mkdir -p "$DEST"
  # On EXCLUT les éléments déjà rangés ailleurs sur le réseau pro (pas de doublon) :
  #  - logos -> 00 - SOCLE/03 - CHARTE - ID VISUEL/02 - LOGOS - VISUELS
  #  - charte PDF -> 00 - SOCLE/03 - CHARTE - ID VISUEL/01 - CHARTE GRAPHIQUE
  # --delete-excluded => ces éléments sont aussi retirés du miroir s'ils y traînent.
  rsync -a --delete --delete-excluded \
    --exclude='.DS_Store' \
    --exclude='Charte graphique/Logo ZE3D - *' \
    --exclude='Charte graphique/Charte graphique - ZE3D.pdf' \
    "$SRC/" "$DEST/" >/dev/null 2>&1
  touch "$STAMP"
fi
exit 0
