#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rebuild-brand-assets.py
Régénère TOUS les assets visuels du site à partir des sources canoniques
de Sources/Charte graphique/, à dimensions calées (rendu identique sur le site).

Sources canoniques :
  - Logo ZE3D - LN.png         (logotype + nom)        -> header
  - Logo ZE3D - Logotype FF.png (logotype fond foncé)  -> footer
  - Logo ZE3D - Logotype.png   (logotype fond clair)   -> splash
  - Logo ZE3D - Favicon.png    (ZE sur cercle blanc)   -> favicons
  - Logo ZE3D - LNP.png        (logotype+nom+phrase)   -> carte og sociale
"""
from PIL import Image, ImageFilter
from pathlib import Path

SRC = Path("Sources/Charte graphique")
PUB = Path("public")

def load(name):
    return Image.open(SRC / name).convert("RGBA")

def crop_content(im):
    bb = im.getbbox()
    return im.crop(bb) if bb else im

def fit(im, max_w=None, max_h=None):
    w, h = im.size
    s = min([x for x in [
        (max_w / w) if max_w else None,
        (max_h / h) if max_h else None] if x is not None])
    return im.resize((max(1, round(w * s)), max(1, round(h * s))), Image.LANCZOS)

print("=" * 60)

# ── 1. HEADER : logo-ln.png (logotype + nom) ───────────────────────
ln = crop_content(load("Logo ZE3D - LN.png"))
ln.save(PUB / "logo-ln.png")
disp_h = 68
disp_w = round(disp_h * ln.width / ln.height)
print(f"✓ logo-ln.png          {ln.width}x{ln.height}  (affichage {disp_w}x{disp_h})")

# ── 2. FOOTER : logo-fond-fonce.png (logotype FF) ──────────────────
ff = crop_content(load("Logo ZE3D - Logotype FF.png"))
ff.save(PUB / "logo-fond-fonce.png")
f_h = 120
f_w = round(f_h * ff.width / ff.height)
print(f"✓ logo-fond-fonce.png  {ff.width}x{ff.height}  (affichage {f_w}x{f_h})")

# ── 3. SPLASH : chargement-logo.png (logotype clair centré + halo) ─
S = 1500
logo = crop_content(load("Logo ZE3D - Logotype.png"))
logo = fit(logo, max_h=1020)                       # ~= ancien contenu (halo compris ~1065)
px = (S - logo.width) // 2
py = (S - logo.height) // 2
# Halo BLANC PUR, doux et étendu : on floute UNIQUEMENT le canal alpha
# (silhouette) puis on l'applique à du blanc plein (aucun mélange avec le noir).
HALO_BLUR  = 100   # rayon de flou -> plus grand = halo plus étendu
HALO_GAIN  = 1.5   # gain d'opacité
HALO_MAX   = 128   # plafond d'opacité (/255) -> 128 = 50 %
alpha_canvas = Image.new("L", (S, S), 0)
alpha_canvas.paste(logo.split()[3], (px, py))
halo_alpha = alpha_canvas.filter(ImageFilter.GaussianBlur(HALO_BLUR))
halo_alpha = halo_alpha.point(lambda a: min(HALO_MAX, int(a * HALO_GAIN)))
halo = Image.new("RGBA", (S, S), (255, 255, 255, 255)); halo.putalpha(halo_alpha)
canvas = Image.new("RGBA", (S, S), (0, 0, 0, 0))
canvas = Image.alpha_composite(canvas, halo)
canvas.paste(logo, (px, py), logo)
canvas.save(PUB / "chargement-logo.png")
print(f"✓ chargement-logo.png  {S}x{S}  (logotype centré + halo doux étendu)")

# ── 4. FAVICONS depuis Logo ZE3D - Favicon.png ─────────────────────
fav = load("Logo ZE3D - Favicon.png")              # 512x512 (ZE sur cercle blanc)

def on_white(im):
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    return Image.alpha_composite(bg, im).convert("RGB")

# PWA + Apple : aplatis sur blanc (opaques)
on_white(fit(fav, 512, 512)).save(PUB / "icon-512.png")
on_white(fit(fav, 180, 180)).save(PUB / "apple-touch-icon.png")
# Favicons PNG : on garde la transparence (cercle blanc, coins transparents)
fav.resize((32, 32), Image.LANCZOS).save(PUB / "favicon-32.png")
fav.resize((16, 16), Image.LANCZOS).save(PUB / "favicon-16.png")
# .ico multi-tailles
fav.save(PUB / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("✓ favicons            icon-512 / apple-touch-icon / favicon-32 / favicon-16 / favicon.ico")

# ── 5. CARTE OG sociale : og-ze3d-card.jpg (LNP centré sur blanc) ──
C = 1200
lnp = crop_content(load("Logo ZE3D - LNP.png"))
lnp = fit(lnp, max_w=int(C * 0.82), max_h=int(C * 0.72))
card = Image.new("RGB", (C, C), (255, 255, 255))
card.paste(lnp, ((C - lnp.width) // 2, (C - lnp.height) // 2), lnp)
card.save(PUB / "og-ze3d-card.jpg", quality=92)
print(f"✓ og-ze3d-card.jpg     {C}x{C}  (LNP {lnp.width}x{lnp.height} centré sur blanc)")

print("=" * 60)
print("Terminé.")
