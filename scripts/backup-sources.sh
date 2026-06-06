#!/bin/bash
# backup-sources.sh
# Sauvegarde "dispatchée" de Sources/ vers le réseau pro (SynologyDrive-ZE3D) :
# chaque type d'élément va dans sa maison propre ; le miroir Claude Code ne garde
# QUE ce qui n'a aucune autre maison. Appelé par le hook "Stop" + lançable à la main.
#
# SÉCURITÉ : chaque cible est GUARDÉE (aucune synchro si la source est absente/vide)
# => supprimer/vider le dossier de travail n'efface JAMAIS les sauvegardes du serveur.

ROOT="/Users/emmanuelzerdoun/Documents/SITE WEB"
SRC="$ROOT/Sources"
STAMP="$ROOT/scripts/.sources-backup.stamp"
SYN="/Users/emmanuelzerdoun/Library/CloudStorage/SynologyDrive-ZE3D"

MIRROR="$SYN/05 - SITE/01 - CLAUDE CODE/Sources"
SIG_DEST="$SYN/00 - SOCLE/03 - CHARTE - ID VISUEL/04 - SIGNATURES MAILS"
GBP_DEST="$SYN/04 - COM/01 - GOOGLE BUSINESS PRO/01 - PHOTOS"
QR_DEST="$SYN/00 - SOCLE/03 - CHARTE - ID VISUEL/05 - QR CODE SITE"

# Garde-fou global : on ne fait RIEN si Sources/ est absent ou vide.
[ -d "$SRC" ] && [ -n "$(find "$SRC" -type f ! -name '.DS_Store' -print -quit 2>/dev/null)" ] || exit 0

# Rien à faire si rien n'a changé depuis le dernier passage.
if [ -f "$STAMP" ] && [ -z "$(find "$SRC" -type f ! -name '.DS_Store' -newer "$STAMP" -print -quit 2>/dev/null)" ]; then
  exit 0
fi

# Copie d'un sous-dossier vers sa maison propre (ADDITIF : ne supprime jamais ce que
# le fondateur aurait ajouté manuellement dans ce dossier). Guardé : skip si source vide.
push_dir() {
  local s="$1" d="$2"
  [ -d "$s" ] && [ -n "$(find "$s" -type f ! -name '.DS_Store' -print -quit 2>/dev/null)" ] || return 0
  mkdir -p "$d"
  rsync -a --exclude='.DS_Store' "$s/" "$d/" >/dev/null 2>&1
}

# 1) Signatures mail -> 00 - SOCLE/03 - CHARTE - ID VISUEL/04 - SIGNATURES MAILS
push_dir "$SRC/Signatures mail" "$SIG_DEST"
# 2) GBP photos -> 04 - COM/01 - GOOGLE BUSINESS PRO/01 - PHOTOS
push_dir "$SRC/GBP photos" "$GBP_DEST"
# 3) QR codes -> 00 - SOCLE/03 - CHARTE - ID VISUEL/05 - QR CODE SITE
push_dir "$SRC/QR codes" "$QR_DEST"

# 4) Le reste -> miroir Claude Code, SANS ce qui est déjà rangé ailleurs :
#    - Charte graphique (logos -> 02 LOGOS-VISUELS ; PDF+HTML -> 01 CHARTE GRAPHIQUE)
#    - Signatures mail, GBP photos, QR codes (rangés ci-dessus)
#    --delete-excluded retire aussi ces éléments du miroir s'ils y traînent.
#    => le miroir ne garde que : Rendus/ + Photos/ (aucune autre maison).
mkdir -p "$MIRROR"
rsync -a --delete --delete-excluded \
  --exclude='.DS_Store' \
  --exclude='/Charte graphique' \
  --exclude='/Signatures mail' \
  --exclude='/GBP photos' \
  --exclude='/QR codes' \
  "$SRC/" "$MIRROR/" >/dev/null 2>&1

touch "$STAMP"
exit 0
