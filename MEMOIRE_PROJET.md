# MEMOIRE PROJET — Site vitrine ZE3D
# Derniere mise a jour : 3 avril 2026 — Session 2

---

## 1. IDENTITE DU PROJET

- **Entreprise :** ZE3D — Microentreprise
- **Fondateur :** Emmanuel Zerdoun
- **Activite :** Scan-to-BIM, Modelisation 3D, Rendu architectural
- **Localisation :** Perpignan (66), Occitanie
- **Zone d'intervention :** Occitanie (terrain) + France entiere (teletravail)
- **Objectif de revenu :** 3 000 EUR net/mois sous 6 a 8 mois
- **Email :** contact@ze3d.fr
- **Site futur :** ze3d.fr

---

## 2. OFFRE — 3 POLES DE PRESTATIONS

### Pole 1 — Releve & Capture numerique
- Releve sur site : techniques traditionnelles (metre, telemetre) ou scanner laser / LiDAR
- Metres de precision adaptes aux besoins du projet
- **Livrables :** Nuage de points, RCP, E57, Panoramas 360, Autres

### Pole 2 — Modelisation 3D & BIM (Scan-to-BIM)
- Realisation de la Maquette Numerique 3D (Autodesk - Revit)
- A partir du releve realise ou des sources client (plans DAO, autres)
- Integration BIM et LOD selon besoins
- **Livrables :** Maquette Revit (.rvt), Export IFC, Plans DWG, Plans PDF, Autres

### Pole 3 — Rendu & Visualisation
- Mise en image de la Maquette Numerique
- Integration des materiaux et textures
- **Livrables :** Rendus 3D photorealistes, Videos, Panoramas 360, Autres

---

## 3. COMPETENCES TECHNIQUES

| Logiciel               | Niveau                    |
|------------------------|---------------------------|
| Autodesk Revit         | Expert (15+ ans)          |
| Enscape                | Maitrise                  |
| Adobe Photoshop        | Maitrise                  |
| Adobe Lightroom        | Maitrise                  |
| Adobe After Effects    | Debutant intermediaire    |
| Autodesk Autocad       | Maitrise                  |
| Faro Scene             | Maitrise                  |
| Scanner laser          | Maitrise operationnelle   |

---

## 4. CIBLES CLIENTS

- Cabinets d'architecture / Agences de maitrise d'oeuvre
- Bureaux d'etudes (structure, fluides, economistes)
- Promoteurs immobiliers
- Maitres d'ouvrage publics et prives
- Entreprises generales du batiment
- Gestionnaires de patrimoine immobilier
- Collectivites territoriales

---

## 5. IDENTITE & TON EDITORIAL

- **Positionnement :** Expert technique, precis, fiable, innovant
- **Ton :** Professionnel, direct, sobre. Pas de jargon inaccessible.
- **Langue :** Francais uniquement
- **Pas d'humour**, pas de formules marketing creuses
- **Typographies :** DM Sans (corps) + Nasalization (marque ZE3D)
- **Palette :** Fond clair (#FFFFFF), accent bleu ardoise (#4A6580), texte sombre (#1A2530)

---

## 6. STACK TECHNIQUE

- **Framework :** Astro 6.1.2
- **Node :** >= 22.12.0
- **Pas de framework JS** (vanilla)
- **Polices :** DM Sans (Google Fonts) + Nasalization (locale, .otf)
- **Deploiement :** Netlify (test + prod)
- **Repo GitHub :** github.com/MedreZ/ze3d-site

---

## 7. ARCHITECTURE DE DEPLOIEMENT

```
Localhost (develop)  -->  GitHub  -->  Netlify TEST  -->  Netlify PROD
```

| Environnement | Branche  | URL                           |
|---------------|----------|-------------------------------|
| Dev (local)   | develop  | http://localhost:4321         |
| Test          | develop  | https://ze3d-test.netlify.app |
| Production    | main     | https://ze3d-prod.netlify.app |

- Push sur `develop` --> deploiement auto sur ze3d-test
- Merge `develop` --> `main` --> deploiement auto sur ze3d-prod
- **Ne jamais merger vers main sans validation prealable sur test**

---

## 8. STRUCTURE DU SITE

### Pages existantes
- **Accueil (index.astro)** — Hero, Prestations, A propos, Stats, Realisations, CTA

### Pages a creer
- /prestations — Detail des 3 poles
- /realisations — Galerie complete
- /a-propos — Parcours du fondateur
- /contact — Formulaire de devis
- /mentions-legales — Obligations legales (SIRET, hebergeur, RGPD)

### Composants
- Navigation.astro — Nav fixe + hamburger mobile
- Footer.astro — Footer sombre 3 colonnes
- Layout.astro — Layout principal avec SEO/OG

### Styles
- global.css — Design system, variables, reset, utilitaires

---

## 9. STRUCTURE DES FICHIERS

```
/Users/emmanuelzerdoun/Documents/SITE WEB/
├── src/
│   ├── pages/index.astro
│   ├── components/Navigation.astro, Footer.astro
│   ├── layouts/Layout.astro
│   └── styles/global.css
├── public/                  (assets servis : images, fonts, logos)
│   ├── fonts/Nasalization.otf
│   ├── realisations/        (images de la galerie)
│   ├── logo-fond-clair.png
│   ├── logo-fond-fonce.png
│   └── photo-emmanuel.JPG
├── Sources/                 (toutes les images sources — 33 fichiers)
├── dist/                    (build)
├── .git/                    (historique)
├── CLAUDE_2.md              (contexte initial du projet)
├── MEMOIRE_PROJET.md        (ce fichier)
├── package.json
└── astro.config.mjs
```

---

## 10. IMAGES SOURCES (dossier Sources/)

| Prefix | Categorie                          |
|--------|------------------------------------|
| 1xx    | Logos / identite visuelle          |
| 2xx    | Rendus exterieurs                  |
| 3xx    | Scans / releves                    |
| 4xx    | Modelisations BIM                  |
| 5xx    | Rendus 3D / visualisations         |

### Images selectionnees pour la page d'accueil (grille realisations)
- 501, 502, 503, 505, 507, 513

### Image Hero
- 509.jpg (object-position: 18% center)

---

## 11. DECISIONS DE DESIGN PRISES

- Hero : split 52/48 (texte/image), image 509.jpg, object-position 18% center
- Texte "ZE3D" dans la nav : meme hauteur que le logo (font-size 4.2rem)
- Grille realisations : systeme 4x4 (16 cellules), images de tailles variees (1x1, 2x1, 1x2, 2x2), cellules vides pour dynamisme
  - Disposition : 513 (2x2) | vide | 507 (1x1) | 503 (2x1) | 501 (1x2) | vide | 505 (1x1) | 502 (2x2)
- Stats : 5 blocs (15 ans / Revit Expert / BIM Modeleur / Releve 3D Scanner Laser / Perpignan & France entiere)
- Cartes prestations : texte en flex:1 pour aligner les separateurs et livrables, min-height 62px sur badges
- Palette fond clair, accent #4A6580
- Navigation : fond blanc semi-transparent avec blur
- Footer : fond sombre #1A2530
- Pas de ligne decorative sur l'image hero

---

## 12. TEXTES VALIDES

### Hero subtitle
"Specialiste en modelisation 3D et BIM Architecture depuis plus de 15 ans, je vous accompagne dans la realisation des Maquettes Numeriques de vos batiments - depuis le releve sur site jusqu'aux rendus graphiques."

Note : "Maquettes Numeriques" en majuscules = choix volontaire du fondateur.

### Texte Pole 01
"Releve sur site de vos batiments a l'aide de techniques traditionnelles (metre, telemetre) ou de scanner laser / LiDAR derniere generation. Metres de precision adaptes a vos besoins et votre projet."

### Texte Pole 02
"Realisation de la Maquette Numerique 3D (Autodesk - Revit) de vos batiments a partir du releve realise ou de vos sources (plans DAO, autres). Integration BIM et LOD selon vos besoins."

### Texte Pole 03
"Mise en image de votre Maquette Numerique. Integrations des materiaux et textures. Creation de vos elements graphiques : Vues 3D photorealistes, integration dans le site, videos, panorama a 360, autres."

### Texte A propos
"Responsable du pole 3D et BIM Coordinateur pendant plus de 15 ans dans un cabinet de maitrise d'oeuvre parisien, je cree aujourd'hui ZE3D pour mettre cette expertise au service des professionnels du batiment en Occitanie et dans toute la France."

"Base a Perpignan, j'interviens sur site pour vos metres et releves numeriques et accompagne vos projets de modelisation 3D et de rendus graphiques sur toute la France."

---

## 13. OBLIGATIONS LEGALES (A IMPLEMENTER)

Page mentions legales a creer avec :
- Identite : Nom, prenom, adresse, SIRET, statut
- Hebergeur : Netlify (coordonnees completes)
- Email de contact
- Directeur de publication
- Politique de confidentialite / RGPD (formulaire de contact)
- Assurance RC Pro (si applicable)

---

## 14. HISTORIQUE GIT

```
e299b5a Refonte page accueil : textes, grille realisations 4x4, stats 5 blocs
a6f80f1 Refonte design : palette Encre & Ardoise, logos, contenu editorial
2f213f7 init: projet Astro ZE3D
```

Premier deploiement test effectue le 3 avril 2026 sur https://ze3d-test.netlify.app

---

## 15. NOTES POUR CLAUDE CODE

- Le fondateur est expert BIM mais pas developpeur web : code lisible et explique
- Solutions simples et robustes > solutions complexes
- Chaque composant facile a modifier (textes, images, couleurs)
- Expliquer les decisions techniques importantes
- Ne jamais push sur main sans validation du fondateur
- Toujours travailler sur la branche `develop`
- "Maquettes Numeriques" toujours avec majuscules (choix du fondateur)
- Le fondateur prefere valider les textes avant application
- Pour lancer le dev server : export PATH="/usr/local/bin:$PATH" && cd "/Users/emmanuelzerdoun/Documents/SITE WEB" && npm run dev
- npm se trouve dans /usr/local/bin/npm (pas dans le PATH par defaut du shell Claude Code)
