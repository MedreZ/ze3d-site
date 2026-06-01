/**
 * generate-webp.mjs — Génère les variantes WebP des images de contenu
 * et l'image Open Graph par défaut (1200×630).
 *
 * Utilise `sharp` (déjà présent via Astro). Les fichiers JPG/PNG d'origine
 * sont CONSERVÉS : le WebP vient en complément (servi via <picture>).
 *
 * Lancement : node scripts/generate-webp.mjs
 */
import sharp from 'sharp';
import { readdir, stat } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const PUBLIC = fileURLToPath(new URL('../public/', import.meta.url));
const QUALITY = 82; // haute qualité, visuellement identique

/* Images de contenu à convertir (chemins relatifs à /public). */
const singles = [
  '509.jpg',
  'photo-emmanuel.JPG',
  'prestations/201.jpg',
  'prestations/202.jpg',
  'prestations/203.jpg',
  'prestations/204.jpg',
  'prestations/403.jpg',
  'prestations/506.jpg',
  'prestations/100.png',
];

/* Toutes les images de la galerie réalisations. */
const realisationsDir = path.join(PUBLIC, 'realisations');
const realisations = (await readdir(realisationsDir))
  .filter((f) => /\.(jpe?g|png)$/i.test(f))
  .map((f) => path.join('realisations', f));

const targets = [...singles, ...realisations];

let totalJpg = 0;
let totalWebp = 0;

for (const rel of targets) {
  const src = path.join(PUBLIC, rel);
  if (!existsSync(src)) {
    console.log(`  ⚠️  introuvable : ${rel}`);
    continue;
  }
  const out = src.replace(/\.(jpe?g|png)$/i, '.webp');
  await sharp(src).webp({ quality: QUALITY, effort: 5 }).toFile(out);

  const inSize = (await stat(src)).size;
  const outSize = (await stat(out)).size;
  totalJpg += inSize;
  totalWebp += outSize;
  const pct = Math.round((1 - outSize / inSize) * 100);
  console.log(
    `  ✓ ${rel.padEnd(28)} ${(inSize / 1024).toFixed(0).padStart(5)} Ko → ${(outSize / 1024).toFixed(0).padStart(5)} Ko webp (-${pct}%)`
  );
}

/* Image Open Graph par défaut : 1200×630 dérivée du rendu 509.jpg. */
const ogOut = path.join(PUBLIC, 'og-default.jpg');
await sharp(path.join(PUBLIC, '509.jpg'))
  .resize(1200, 630, { fit: 'cover', position: 'centre' })
  .jpeg({ quality: 85, mozjpeg: true })
  .toFile(ogOut);
const ogSize = (await stat(ogOut)).size;
console.log(`\n  ✓ og-default.jpg créée (1200×630, ${(ogSize / 1024).toFixed(0)} Ko)`);

console.log(
  `\n  Total : ${(totalJpg / 1024 / 1024).toFixed(1)} Mo (orig.) → ${(totalWebp / 1024 / 1024).toFixed(1)} Mo (webp) — économie ${Math.round((1 - totalWebp / totalJpg) * 100)} %`
);
