#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate-legal-pdfs.py
Génère les PDF officiels des Mentions légales et des CGV de ZE3D,
mis en page sur l'identité graphique du site, et les place dans Synology
avec archivage automatique de l'ancienne version.

  → Mentions légales ZE3D - AA-MM.pdf  dans .../03 - MENTIONS LEGALES
  → CGV ZE3D - AA-MM.pdf               dans .../02 - CGV

RÈGLE : à chaque modification de mentions-legales.astro ou cgv.astro,
relancer ce script. L'ancienne version du fichier est déplacée dans
"00 - ARCHIVES" (avec un indice si un fichier du même nom existe déjà).

Usage : python3 scripts/generate-legal-pdfs.py
"""
import re, shutil, subprocess, datetime, sys
from pathlib import Path
from PIL import Image
import fitz  # PyMuPDF

ROOT   = Path("/Users/emmanuelzerdoun/Documents/SITE WEB")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FONT   = ROOT / "public/fonts/Nasalization.otf"
LOGO   = ROOT / "public/logo-ln.png"
SYN    = Path("/Users/emmanuelzerdoun/Library/CloudStorage/SynologyDrive-ZE3D"
              "/00 - SOCLE/02 - JURIDIQUE")
TMP    = Path("/tmp")

# Marque « ZE3D » du pied de page : dérivée de la source canonique "Logo ZE3D - Nom.png"
# (police Nasalization + ratio H 75 % + couleur d'origine), redimensionnée pour le pied.
NOM      = ROOT / "Sources/Charte graphique/Logo ZE3D - Nom.png"
FOOTMARK = TMP / "ze3d-footmark.png"
_n = Image.open(NOM).convert("RGBA")
_bb = _n.getbbox()
if _bb:
    _n = _n.crop(_bb)
_h = 160
_n = _n.resize((round(_n.width * _h / _n.height), _h), Image.LANCZOS)
_n.save(FOOTMARK)
NW, NH = _n.size   # proportions exactes du nom (pour le tampon)

def furl(p: Path) -> str:
    return "file://" + str(p).replace(" ", "%20")

now    = datetime.datetime.now()
YYMM   = now.strftime("%y-%m")
MOIS   = ["janvier","février","mars","avril","mai","juin","juillet","août",
          "septembre","octobre","novembre","décembre"]
GENDATE = f"{now.day} {MOIS[now.month-1]} {now.year}"

DOCS = [
    dict(astro=ROOT/"src/pages/mentions-legales.astro",
         kicker="Document juridique officiel", title="Mentions légales",
         foot="Mentions légales",
         folder=SYN/"03 - MENTIONS LEGALES", base=f"Mentions légales ZE3D - {YYMM}"),
    dict(astro=ROOT/"src/pages/cgv.astro",
         kicker="Document juridique officiel", title="Conditions Générales de Vente",
         foot="CGV",
         folder=SYN/"02 - CGV", base=f"CGV ZE3D - {YYMM}"),
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&display=swap');
@font-face{font-family:'Nasalization';src:url('%%FONT%%') format('opentype');font-weight:normal;font-style:normal}
@page{
  size:A4; margin:18mm 17mm 17mm;
  @bottom-center{content:"%%FOOT%% · Document officiel";font-family:'DM Sans',system-ui,sans-serif;font-size:8pt;color:#9aa3ad;}
  @bottom-right{content:"Page " counter(page) " / " counter(pages);font-family:'DM Sans',system-ui,sans-serif;font-size:8pt;color:#9aa3ad;}
}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'DM Sans',system-ui,Arial,sans-serif;color:#1A2530;font-size:10.5pt;line-height:1.6;margin:0}
/* En-tête */
.letterhead{display:flex;align-items:center;justify-content:space-between;border-bottom:2px solid #3C5E7C;padding-bottom:12px}
.letterhead img{height:40px;display:block}
.letterhead .id{text-align:right;font-size:7.5pt;color:#6b7682;line-height:1.55}
.letterhead .id b{color:#3C5E7C;font-weight:700}
.titleblock{margin:22px 0 26px}
.kicker{font-size:8pt;letter-spacing:.22em;text-transform:uppercase;color:#3C5E7C;font-weight:700}
.doc-title{font-size:23pt;font-weight:700;color:#1A2530;margin:7px 0 8px;line-height:1.1}
.doc-sub{font-size:10pt;color:#1A2530;margin:0 0 6px}
.doc-meta{font-size:9pt;color:#6b7682}
.doc-meta b{color:#3C5E7C;font-weight:700}
/* Contenu légal */
.legal-section{margin:0 0 20px}
.legal-section h2{font-size:13pt;font-weight:700;color:#1A2530;margin:0 0 11px;padding-bottom:7px;border-bottom:2px solid #3C5E7C;break-after:avoid}
.legal-section h3{font-size:10.5pt;font-weight:700;color:#1A2530;margin:15px 0 6px;break-after:avoid}
.legal-section p{margin:0 0 9px;color:#26323f}
.legal-section a{color:#3C5E7C;text-decoration:underline;text-underline-offset:2px;word-break:break-word}
.legal-section strong{color:#1A2530;font-weight:700}
.legal-list{display:grid;grid-template-columns:190px 1fr;gap:7px 18px;margin:0;padding:14px 18px;background:#F3F5F7;border-radius:8px;break-inside:avoid}
.legal-list dt{font-size:7.5pt;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#3C5E7C;padding-top:2px}
.legal-list dd{font-size:9.5pt;color:#1A2530;margin:0;line-height:1.5}
.legal-list dd a{color:#3C5E7C;text-decoration:none}
.legal-bullets{list-style:none;padding:0;margin:0 0 9px}
.legal-bullets li{position:relative;padding:3px 0 3px 18px;color:#26323f}
.legal-bullets li::before{content:'';position:absolute;left:2px;top:9px;width:6px;height:6px;background:#3C5E7C;border-radius:50%}
.legal-section ul:not(.legal-bullets){list-style:disc;padding-left:20px;margin:0 0 9px}
.legal-section ol{list-style:decimal;padding-left:22px;margin:0 0 9px}
.legal-section li{margin:3px 0}
.brand-ze3d{font-family:'Nasalization',sans-serif;font-weight:normal;text-transform:uppercase;letter-spacing:normal;display:inline-block;transform:scaleX(.75);transform-origin:left center;margin-right:-.71em;vertical-align:baseline}
"""

ID_BLOCK = ('<b><span class="brand-ze3d">ZE3D</span></b> — Emmanuel Zerdoun EI<br>'
            'SIRET 812&nbsp;525&nbsp;103&nbsp;00022 · TVA FR47812525103<br>'
            '47 rue Vivienne, 75002 Paris<br>'
            'ze3d.fr · contact@ze3d.fr')

def extract(astro: Path):
    src = astro.read_text(encoding="utf-8")
    m = re.search(r"const lastUpdate = '([^']+)'", src)
    lastupd = m.group(1) if m else "—"
    marker = '<div class="container legal-content-inner">'
    start = src.index(marker) + len(marker)
    end = src.index('</article>', start)
    content = src[start:end].rstrip()
    if content.endswith('</div>'):
        content = content[:-len('</div>')].rstrip()
    content = content.replace('href="/', 'href="https://ze3d.fr/')
    return lastupd, content

FORCE = "--force" in sys.argv

def latest_pdf(folder: Path):
    pdfs = list(folder.glob("*.pdf"))
    return max(pdfs, key=lambda p: p.stat().st_mtime) if pdfs else None

def archive_all(folder: Path):
    """Déplace toutes les versions actuelles du dossier vers 00 - ARCHIVES (indice si collision de nom)."""
    arch = folder / "00 - ARCHIVES"; arch.mkdir(exist_ok=True)
    moved = []
    for p in list(folder.glob("*.pdf")):
        target = arch / p.name
        if target.exists():
            n = 1
            while (arch / f"{p.stem} ({n}){p.suffix}").exists():
                n += 1
            target = arch / f"{p.stem} ({n}){p.suffix}"
        shutil.move(str(p), str(target)); moved.append(target.name)
    return moved

for d in DOCS:
    folder = d["folder"]; folder.mkdir(parents=True, exist_ok=True)
    cur = latest_pdf(folder)
    if cur and not FORCE and d["astro"].stat().st_mtime <= cur.stat().st_mtime:
        print(f"• {d['base']}.pdf : déjà à jour — ignoré")
        continue
    lastupd, content = extract(d["astro"])
    css = (CSS.replace("%%FONT%%", furl(FONT))
              .replace("%%FOOTMARK%%", furl(FOOTMARK))
              .replace("%%FOOT%%", d["foot"]))
    html = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<style>{css}</style></head><body>
<div class="letterhead">
  <img src="{furl(LOGO)}" alt="ZE3D">
  <div class="id">{ID_BLOCK}</div>
</div>
<div class="titleblock">
  <div class="kicker">{d['kicker']}</div>
  <div class="doc-title">{d['title']}</div>
  <div class="doc-sub"><span class="brand-ze3d">ZE3D</span> — Emmanuel Zerdoun EI</div>
  <div class="doc-meta">Version du <b>{lastupd}</b> · Document généré le {GENDATE}</div>
</div>
{content}
</body></html>"""
    html_path = TMP / f"legal-{d['base']}.html"
    pdf_tmp   = TMP / f"legal-{d['base']}.pdf"
    html_path.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                    "--no-pdf-header-footer", f"--print-to-pdf={pdf_tmp}",
                    furl(html_path)], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Tampon de la marque ZE3D (image, proportions exactes) en bas à gauche de chaque page,
    # aligné verticalement sur la ligne de pied (texte "Document officiel").
    pdf = fitz.open(str(pdf_tmp))
    x0 = 17 / 25.4 * 72   # marge gauche 17mm en points
    for page in pdf:
        hits = page.search_for("Document officiel")
        if not hits:
            continue
        r = hits[0]; cy = (r.y0 + r.y1) / 2; th = r.y1 - r.y0
        mh = th * 1.02; mw = mh * (NW / NH)
        page.insert_image(fitz.Rect(x0, cy - mh/2, x0 + mw, cy + mh/2),
                          filename=str(FOOTMARK), keep_proportion=True)
    final = folder / f"{d['base']}.pdf"
    moved = archive_all(folder)
    pdf.save(str(final)); pdf.close()
    pdf_tmp.unlink(missing_ok=True)
    print(f"✓ {final.name}")
    print(f"   → {final}")
    for m in moved:
        print(f"   ↪ archivé : {m}")
print("Terminé.")
