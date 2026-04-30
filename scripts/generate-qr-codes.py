#!/usr/bin/env python3
"""
Génération des QR codes ZE3D — design final.

Style : barres verticales + yeux à coins arrondis (mi-doux).
Couleur : bleu accent ZE3D #4A6580 sur fond blanc.

PNG : design styled (pour usage standard, web, impression).
SVG : version vectorielle pure noir/blanc (max compatibilité scan, impression haute qualité).

Usage : python3 scripts/generate-qr-codes.py
Sortie : Sources/QR codes/<nom>.{png,svg}
"""

import os
import qrcode
from qrcode.image.svg import SvgPathImage
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import (
    RoundedModuleDrawer,
    VerticalBarsDrawer,
)
from qrcode.image.styles.colormasks import SolidFillColorMask

# === Configuration ===
URLS = {
    "ze3d-accueil":          "https://ze3d.fr",
    "ze3d-contact":          "https://ze3d.fr/contact",
    "ze3d-realisations":     "https://ze3d.fr/realisations",
    "ze3d-mentions-legales": "https://ze3d.fr/mentions-legales",
    "ze3d-cgv":              "https://ze3d.fr/cgv",
}

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR   = os.path.join(PROJECT_ROOT, "Sources", "QR codes")

ZE3D_BLUE = (74, 101, 128)   # #4A6580
WHITE     = (255, 255, 255)

# Niveau de correction d'erreur : M = 15% (suffisant sans logo central)
ERROR_LEVEL = qrcode.constants.ERROR_CORRECT_M

os.makedirs(OUTPUT_DIR, exist_ok=True)


def make_png_styled(url: str, output_path: str):
    """PNG design : barres verticales + yeux arrondis mi-doux, bleu ZE3D."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_LEVEL,
        box_size=20,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=VerticalBarsDrawer(),
        eye_drawer=RoundedModuleDrawer(radius_ratio=0.5),
        color_mask=SolidFillColorMask(
            front_color=ZE3D_BLUE,
            back_color=WHITE,
        ),
    )
    img.save(output_path, "PNG", optimize=True)


def make_svg_pure(url: str, output_path: str):
    """SVG vectoriel pur — noir sur blanc (compatibilité scan max)."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_LEVEL,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(image_factory=SvgPathImage)
    img.save(output_path)


def main():
    print(f"Output dir : {OUTPUT_DIR}\n")
    for name, url in URLS.items():
        png_path = os.path.join(OUTPUT_DIR, f"{name}.png")
        svg_path = os.path.join(OUTPUT_DIR, f"{name}.svg")
        print(f"  • {name}")
        print(f"      url : {url}")
        make_png_styled(url, png_path)
        make_svg_pure(url, svg_path)
        print(f"      PNG : design (barres verticales + yeux arrondis, bleu ZE3D)")
        print(f"      SVG : vectoriel pur (noir/blanc)\n")
    print(f"✓ {len(URLS)} QR codes générés.")


if __name__ == "__main__":
    main()
