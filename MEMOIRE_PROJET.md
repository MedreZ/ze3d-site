# MEMOIRE PROJET — Site vitrine ZE3D
# Derniere mise a jour : 3 avril 2026

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

### Pole 1 — Capture & Releve numerique
- Scanner laser 3D, telemetre, metre classique
- **Livrables :** Nuage de points (RCP, E57, PTX), Panoramas 360

### Pole 2 — Modelisation 3D & BIM (Scan-to-BIM)
- Maquettes Revit depuis nuages de points, plans DAO, plans papier
- LOD 100 a 400
- **Livrables :** Maquette Revit (.rvt), Export IFC, Plans DWG, Plans PDF

### Pole 3 — Rendu & Visualisation
- Rendus photorealistes, videos, panoramas 360, visites VR
- **Livrables :** Images 3D, Videos archi, Panoramas 360, Visites virtuelles/VR

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

- Hero : split 52/48 (texte/image), image 509.jpg
- Grille realisations : systeme 4x4 (16 cellules), images de tailles variees (1x1, 2x1, 1x2, 2x2), cellules vides pour dynamisme
- Stats : 5 blocs (15 ans / Revit Expert / BIM Modeleur / Releve 3D Scanner Laser / Perpignan & France entiere)
- Palette fond clair, accent #4A6580
- Navigation : fond blanc semi-transparent avec blur
- Footer : fond sombre #1A2530
- Pas de ligne decorative sur l'image hero

---

## 12. TEXTES VALIDES

### Hero subtitle
"Specialiste en modelisation 3D et BIM Architecture depuis plus de 15 ans, je vous accompagne dans la realisation des Maquettes Numeriques de vos batiments - depuis le releve sur site jusqu'aux rendus graphiques."

Note : "Maquettes Numeriques" en majuscules = choix volontaire du fondateur.

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
a6f80f1 Refonte design : palette Encre & Ardoise, logos, contenu editorial
2f213f7 init: projet Astro ZE3D
```

---

## 15. NOTES POUR CLAUDE CODE

- Le fondateur est expert BIM mais pas developpeur web : code lisible et explique
- Solutions simples et robustes > solutions complexes
- Chaque composant facile a modifier (textes, images, couleurs)
- Expliquer les decisions techniques importantes
- Ne jamais push sur main sans validation du fondateur
- Toujours travailler sur la branche `develop`
