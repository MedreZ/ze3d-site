# MEMOIRE PROJET — Site vitrine ZE3D
# Derniere mise a jour : 02 mai 2026 — Session 8 (QR codes design, page CGV, N° TVA obtenu)

---

## 1. IDENTITE DU PROJET

- **Entreprise :** ZE3D — Microentreprise
- **Fondateur :** Emmanuel Zerdoun
- **Activite :** Scan-to-BIM, Modelisation 3D, Rendu architectural
- **Date de creation EI :** 01 avril 2026 (apres la loi du 14 fevrier 2022 → separation patrimoniale automatique + residence principale insaisissable par defaut, voir notes section 15)
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
- **Coherence "Je" partout** (microentreprise solo) : ne jamais ecrire "Nous", "Notre", "Nos" pour decrire l'entreprise. Pour les boutons et titres de section : retirer le possessif (ex: "Prestations" plutot que "Mes prestations" — plus pro/neutre). Pour les textes longs : "Je", "ma", "mon" assume. Decision validee en session 7 (28 avril 2026).
- **Typographies :** DM Sans (corps) + Nasalization (marque ZE3D)
- **REGLE DE MARQUE "ZE3D" (02 juin 2026)** : TOUTE mention VISIBLE de "ZE3D" doit utiliser `<span class="brand-ze3d">ZE3D</span>` (style logo officiel centralise dans global.css : Nasalization Regular, MAJUSCULES, echelle horizontale 75% via scaleX(0.75), tracking 0, + margin-right de compensation -0.71em ; valeur ajustee 50->60->75 au fil des essais). NE PAS styliser les "ZE3D" dans les title/meta/alt/aria/JSON-LD (non stylables / accessibilite) — ils restent en texte simple. Applique partout (nav, footer, corps, pages legales). Pour toute nouvelle page/texte : penser a wrapper "ZE3D". **EXCLUSION IMPORTANTE : la regle concerne UNIQUEMENT le NOM DE MARQUE "ZE3D" (majuscules). L'adresse du site "ze3d.fr" (URL, minuscules) et l'email "contact@ze3d.fr" s'ecrivent TOUJOURS normalement, jamais en style logo.**
- **Palette SITE actuelle :** Fond clair (#FFFFFF), accent bleu ardoise (#4A6580), texte sombre (#1A2530)
- **NOUVELLE PALETTE DE MARQUE (logo refondu, 02 juin 2026)** : Jaune principal #FCC982 / Jaune sec.1 #FFDFB2 / Jaune sec.2 #DFAC65 / Bleu principal #6795BB / Bleu sec.1 #82AFD6 / Bleu sec.2 #3C5E7C. **DECISION couleurs SITE (02 juin) : bleu accent passe de #4A6580 a #3C5E7C (bleu sec.2 du logo) PARTOUT ; bleu clair footer #8FA6C0 -> #82AFD6 ; texte #1A2530 et footer inchanges.** Une tentative de touches DOREES (labels, survols) a ete faite puis RETIREE a la demande de Manu -> **le site reste en BLEU uniquement, PAS de dore** (le dore vit seulement dans le logo). QR codes : encore sur l'ancien bleu #4A6580, a regenerer si on veut aligner (pas prioritaire). Nouveaux logos verticaux dans Sources/Logo/. Voir FEUILLE_DE_ROUTE.md section 8.

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

### Pages existantes (TOUTES CREEES)
- **Accueil** (`index.astro`) — Hero, Prestations, A propos, Stats, Realisations, CTA
- **Prestations** (`prestations.astro`) — Hero + Process 4 vignettes + Slider avant/apres + 3 poles detailles + CTA
- **Realisations** (`realisations.astro`) — Hero + Filtres (Tout/2D/3D/Rendu) + Grille 22 images + Lightbox + CTA
- **A propos** (`a-propos.astro`) — Hero + Mon parcours + Expertise (2 cols) + Ma demarche (4 engagements) + CTA
- **Contact** (`contact.astro`) — Hero + Formulaire Netlify Forms (7 champs + RGPD) + Infos contact + CTA alternatif
- **Mentions legales** (`mentions-legales.astro`) — 10 sections (Editeur, Hebergeur, Assurance, PI, RGPD, Cookies, etc.)
- **CGV** (`cgv.astro`) — Conditions Generales de Vente (B2B), 42 sections. **Texte genere par ChatGPT** (pas par un juriste qualifie). Une revue juridique humaine reste recommandee a terme (notamment sur les clauses limitatives de responsabilite, sections 21-24 et 29).

### Pages a creer
Aucune — toutes les pages du site sont desormais creees.

### Composants
- Navigation.astro — Nav fixe + hamburger mobile
- Footer.astro — Footer sombre 3 colonnes
- Layout.astro — Layout principal avec SEO/OG
- SplashScreen.astro — Ecran d'accueil immersif (uniquement sur la home, voir section 11)

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
│   ├── logos/               (logos clients references : CNAV, CAF, OFII, Capgemini, Optical Center, Fujitsu)
│   ├── prestations/         (100, 201-204, 403, 506 pour la page Prestations)
│   ├── realisations/        (22 images 301-305, 401-404, 501-513 pour la galerie)
│   ├── logo-fond-clair.png
│   ├── logo-fond-fonce.png
│   ├── photo-emmanuel.JPG
│   ├── sig-ze3d-c16b6736.jpg  (image signature mail Ionos, nom obfusque)
│   └── robots.txt             (interdit l'indexation des sig-ze3d-* par les moteurs)
├── Sources/                 (images sources + ressources non servies par le site)
│   ├── (33 images numerotees pour le site)
│   ├── Signature mail ZE3D.jpg          (source originale de la signature)
│   └── Signatures mail/                  (templates HTML pour Ionos — 4 fichiers)
│       ├── signature-emmanuel.html       (rendu visuel + bandeau d'instructions)
│       ├── signature-contact.html        (rendu visuel + bandeau d'instructions)
│       ├── signature-emmanuel-CODE-HTML.txt  (code HTML brut a coller en mode <>)
│       └── signature-contact-CODE-HTML.txt   (code HTML brut a coller en mode <>)
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

### Images de la page Prestations
- Hero : pas d'image
- Process 4 vignettes : 201 (existant) → 202 (releve) → 203 (modelisation) → 204 (rendu)
- Slider avant/apres : 201 (existant) vs 204 (rendu)
- Pole 01 : 100.png (equipements regroupes : metre, telemetre, scanner)
- Pole 02 : 403.jpg (maquette BIM)
- Pole 03 : 506.jpg (rendu photorealiste)

### Images de la page Realisations (22 au total)
Categorisation :
- **2D (Releve)** : 301, 302, 303, 304, 305
- **3D (BIM)**    : 401, 402, 403, 404
- **Rendu**       : 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513

### Image Hero
- 509.jpg (object-position: 18% center)

---

## 11. DECISIONS DE DESIGN PRISES

- Hero : split 52/48 (texte/image), image 509.jpg, object-position 18% center
- Hero mobile : image non cropee affichee juste apres le titre h1
- Texte "ZE3D" dans la nav : meme hauteur que le logo (font-size 5.2rem)
- Grille realisations : systeme 4x4 (16 cellules), images de tailles variees (1x1, 2x1, 1x2, 2x2), cellules vides pour dynamisme
  - Disposition : 513 (2x2) | vide | 507 (1x1) | 503 (2x1) | 501 (1x2) | vide | 505 (1x1) | 502 (2x2)
- Stats : 5 blocs (15 ans / Revit Expert / BIM Modeleur / Releve 3D Scanner Laser / Perpignan & France entiere)
- Cartes prestations : texte en flex:1 pour aligner les separateurs et livrables, min-height 62px sur badges
- Section A propos :
  - Photo Emmanuel reduite a 0.5fr sur desktop, alignee en haut (start) avec margin-top 48px
  - Lisere autour de la photo supprime
  - Photo mobile : affichee apres le titre "15 ans d'expertise", 80% largeur, centree
  - Bloc references clients avec logos en niveaux de gris (couleur au hover)
- Logos clients references : CNAV, CAF, OFII, Capgemini, Optical Center, Fujitsu
  - Ce sont des references personnelles du fondateur (pas des clients ZE3D)
  - Formulation : "Au cours de mes 15 ans d'experience, j'ai eu l'opportunite d'intervenir sur des projets pour des acteurs tels que :"
  - Logos en grayscale 50% opacity, hauteur 42px, couleur au hover
- Palette fond clair, accent #4A6580
- Navigation : fond blanc semi-transparent avec blur
- Footer : fond sombre #1A2530 — textes en bleu clair #8FA6C0 pour lisibilite (et non #4A6580 qui serait trop sombre sur fond sombre)
- Pas de ligne decorative sur l'image hero

### Page Prestations (layout split zigzag)
- Hero simple (titre + sous-titre, pas d'image)
- Process 4 vignettes : images 201-204 reliees par des fleches bleues epaisses (stroke 2.5)
- Slider avant/apres : 201 (existant) vs 204 (rendu), curseur draggable, tags "EXISTANT" et "MODELISATION"
- 3 poles avec alternance image/texte (zigzag) : image a gauche (55%) pour 01 et 03, image a droite pour 02
- Pole 01 : bloc equipement sur fond gris degrade (#F3F5F7 -> #E9ECEF), image 100.png taille 88% largeur
- CTA final avec bouton "Demander un devis" et "Voir les realisations"
- Sur mobile : numero + titre avant l'image, puis paragraphes + livrables

### Page Realisations (grille filtrable + lightbox)
- Hero simple avec label "NOS REALISATIONS" agrandi (1.1rem)
- Filtres pill : Tout / 2D / 3D / Rendu avec compteurs entre parentheses
- Grille 3 colonnes (desktop) / 2 (tablette) / 1 (mobile) avec `grid-auto-flow: dense`
- Items "item-tall" et "item-wide" via modulo (i%7===2 / i%11===5) pour rythme visuel
- Lightbox overlay plein ecran : ESC pour fermer, fleches clavier pour naviguer
- Labels lightbox : "CATEGORIE - Titre" (avec tiret cadratin)
- Legendes uniformisees entre home et realisations (voir section 12)
- Images 503 et 504 (paire jour/nuit) : placees avant 502 dans le tableau pour qu'elles tombent naturellement cote a cote sur la meme ligne en 3 colonnes
- CTA final : "Un projet en tete ?" (coherent avec la page Prestations)

### Page A propos (5 sections, sans timeline)
- Hero split 60/40 : texte + photo Emmanuel (avec badge "15 ans d'experience")
- "Mon parcours" : 3 paragraphes narratifs + logos clients references
- "Mon expertise" (fond gris) : 2 colonnes — Savoir-faire (liste a puces) + Outils (4 tools avec badges Modelisation/Rendu/Retouche/Video)
- "Ma demarche" : 4 cartes (Proximite · Sur-mesure · Exigence · Transparence) avec icones SVG rondes
- CTA final "Parlons de votre projet" avec boutons Devis/Realisations
- **IMPORTANT — Le fondateur n'est PAS architecte (formation DPLG suivie mais memoire final non rendu, donc pas de diplome).** En consequence : ne JAMAIS utiliser le titre "Architecte" ni "Architecte DPLG" ni meme "Architecte de formation" (juge trop ambigu en contexte commercial — l'Ordre des architectes a fait retirer cette mention dans des cas similaires). Formulation validee : **"Issu d'une formation en ecole d'Architecture"** (factuel, sans usurpation de titre). Decision prise en session 7 (28 avril 2026).

### Page Contact (formulaire Netlify Forms)
- Hero simple (label CONTACT + H1 "Parlons de votre projet" + sous-titre 48 h)
- Split 60/40 : Formulaire (gauche) + Infos contact (droite, sticky)
- **Netlify Forms** active : `data-netlify="true"` + `netlify-honeypot="bot-field"`
- 7 champs : Nom* + Prenom* + Entreprise + Email* + Telephone + Type de projet* + Message (optionnel) + case RGPD*
- Select "Type de projet" : Releve numerique / Modelisation 3D & BIM / Rendu & visualisation / Plusieurs / Autre
- **Validation custom** : `novalidate` sur form, JS marque explicitement TOUS les champs invalides avec classe `.is-invalid` (bordure rouge) — fix pour que plusieurs champs soient marques simultanement
- Bouton submit visuellement inactif (opacity 0.4) tant que le formulaire n'est pas valide
- Soumission AJAX via `fetch` (pas de rechargement), message de succes avec scroll smooth
- 3 cartes infos : Email / Zone d'intervention (**"France entiere"** sans mention Perpignan sur cette page pour ne pas limiter) / Delai de reponse
- Honeypot anti-spam (champ cache off-screen)
- Lien vers `/mentions-legales` depuis la case RGPD

### Page Mentions legales (10 sections)
- Hero simple avec date de mise a jour
- 10 sections : Editeur / Hebergeur / Assurance / PI / RGPD / Cookies / Responsabilite / Liens externes / Droit applicable / Contact
- `<dl>` pour infos structurees (fond gris clair `#F3F5F7`)
- Max-width 820px pour lisibilite texte long
- Pas de CTA (page legale, pas de conversion)
- Accessible via footer (lien sur toutes les pages)

### Modifications globales recentes
- **`.section-label` globalement agrandi** : font-size 1.1rem, letter-spacing 0.22em (auparavant 0.7rem / 0.2em). Impact sur tous les labels de section du site.
- **Footer bottom bar** : contrastes renforces (0.75 / 0.6 alpha au lieu de 0.4 / 0.3) pour meilleure lisibilite sur fond sombre
- **Mentions legales** ajoutees au footer bottom (visible sur toutes les pages)
- **Titres "Mes outils"** : 4 outils (Revit, Enscape, Photoshop/Lightroom, After Effects) avec badges — Faro Scene et AutoCAD retires
- **Corrections legales** sur l'ensemble du site :
  - "garantissant" -> "assurant" (pole 01)
  - "Pas de sous-traitance" / "sans intermediaire ni sous-traitance" supprimes (engagement trop fort)
  - "Des delais tenus / Pas de surprise en cours de route" -> formulation plus souple
  - Mention "48 h" conservee (risque faible, usage courant)

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

### Texte references clients
"Au cours de mes 15 ans d'experience, j'ai eu l'opportunite d'intervenir sur des projets pour des acteurs tels que :"
Note : ces references sont liees a l'experience personnelle du fondateur, pas a ZE3D.

### Page A propos — Hero accroche
"Specialiste en modelisation 3D et BIM Architecture depuis plus de 15 ans, je mets mon expertise technique au service des professionnels du batiment. Installe a Perpignan, j'interviens en Occitanie et dans toute la France."

### Page A propos — Mon parcours (3 paragraphes)
**P1 (formulation legale validee — voir section 11) :**
"**Issu d'une formation en ecole d'Architecture**, j'ai debute ma carriere en cabinet de maitrise d'oeuvre parisien ou j'ai occupe pendant plus de 15 ans les fonctions de dessinateur projeteur, puis de Responsable du pole 3D et de BIM Coordinateur. J'y ai pilote des projets d'envergure pour des acteurs tels que la CNAV, la CAF, l'OFII, Capgemini ou Optical Center."

**P2 (sans "sans intermediaire ni sous-traitance") :**
"Aujourd'hui, je cree ZE3D pour mettre cette experience a disposition des professionnels du batiment de maniere independante. Installe a Perpignan, je privilegie une relation directe et sur-mesure avec chaque client."

**P3 :**
"Ce qui me passionne : transformer les releves terrain en Maquettes Numeriques precises, aider les architectes et bureaux d'etudes a visualiser et coordonner leurs projets, et livrer des images qui donnent vie aux projets avant meme leur construction."

### Page A propos — 4 engagements
1. **Proximite** : "Un seul interlocuteur, du releve sur site jusqu'au rendu final — votre projet passe par une seule paire de mains."
2. **Sur-mesure** : "Chaque projet est aborde selon ses specificites. Le niveau de detail, les livrables et la methode sont adaptes a vos besoins reels, pas a une offre standardisee."
3. **Exigence** (renomme depuis "Rigueur") : "La rigueur technique est non-negociable : des releves precis jusqu'aux maquettes BIM LOD 400 si le projet le requiert."
4. **Transparence** (reformulee pour moins d'engagement legal) : "Un devis clair et detaille avant engagement. Un planning partage et tenu. Des livrables conformes au contrat. Une communication ouverte en cas d'evolution du projet."

### Page Contact — Textes valides
- H1 : "Parlons de votre projet"
- Sous-titre : "Je vous reponds sous 48 h avec un devis personnalise adapte a vos besoins."
- Titre colonne formulaire : "Demandez un devis"
- Hint sous titre : "Les champs marques d'un * sont obligatoires."
- Placeholder message : "Decrivez votre projet : type de batiment, surface, delai souhaite, niveau de detail attendu..."
- Message validation : "Merci de remplir les champs obligatoires mis en evidence."
- Message succes : "Merci pour votre message ! Votre demande a bien ete envoyee. Je vous reponds sous 48 h."
- Message erreur : "Une erreur est survenue lors de l'envoi. Merci de reessayer ou de m'ecrire directement a contact@ze3d.fr."
- RGPD : "J'accepte que mes donnees soient utilisees pour me recontacter dans le cadre de ma demande. En savoir plus [lien mentions legales]"
- Carte Zone d'intervention : **"France entiere"** + "Deplacement possible selon le projet" (sans mention Perpignan pour ne pas limiter)

### Informations legales du fondateur (pour mentions-legales.astro)
- Nom : Emmanuel Zerdoun
- Denomination : Emmanuel Zerdoun EI
- Nom commercial : ZE3D
- Siege : 47 rue Vivienne, 75002 Paris
- SIRET : 812 525 103 00022
- Telephone : 06 73 04 21 28
- Email : contact@ze3d.fr
- TVA intracommunautaire : FR 47812525103 (obtenue, session 8 — 02 mai 2026 ; format avec espace selon PDF officiel)
- Assurance RC Pro : en cours d'obtention
- Hebergeur : Netlify, Inc. (44 Montgomery Street, Suite 300, San Francisco, CA 94104, USA)

### Page Prestations — Hero
H1 : "3 poles d'expertise complementaires"
Sous-titre : "De la capture terrain a la maquette numerique et jusqu'aux rendus graphiques — une expertise complete, un seul interlocuteur pour l'ensemble de votre projet."

### Page Prestations — Pole 01 (Releve & Capture numerique)
"Le releve numerique est la premiere etape essentielle de tout projet de modelisation. Selon la complexite du batiment, je m'adapte a vos besoins : mesures traditionnelles au metre et telemetre pour les petits releves, ou scanner laser / LiDAR derniere generation pour les projets complexes et les batiments patrimoniaux."
"Chaque intervention est realisee sur site avec une precision adaptee au niveau de detail requis par votre projet. Les donnees capturees servent ensuite de base fiable pour la modelisation, garantissant la coherence entre le bati existant et la Maquette Numerique."
Moyens : scanner laser 3D, LiDAR, telemetre laser, metre, photographie 360°.

### Page Prestations — Pole 02 (Modelisation 3D & BIM)
"A partir du releve realise ou de vos sources (plans DAO, plans papier, documents techniques), je realise la Maquette Numerique 3D de votre batiment sous Autodesk Revit."
"De la maquette 3D simple destinee a la visualisation et aux etudes d'esquisse, jusqu'a la maquette BIM structuree selon les standards internationaux (LOD 100 a 400, export IFC pour l'interoperabilite) : j'adapte la modelisation a vos besoins et au niveau d'exigence de votre projet."
Note importante : le BIM est presente comme UNE OPTION, pas comme une obligation. Certains clients veulent juste une maquette 3D simple.

### Page Prestations — Pole 03 (Rendu & Visualisation)
"La mise en image de votre Maquette Numerique permet de valoriser votre projet, de convaincre vos clients et de presenter votre travail de maniere professionnelle. Integration des materiaux, textures, eclairages et mise en scene : je transforme la maquette technique en visuel impactant."
"Du rendu 3D photorealiste a la video d'architecture, en passant par les panoramas 360° immersifs, j'adapte le livrable a votre contexte de presentation : dossier d'etude, concours, promotion immobiliere, communication client."
Outils : Enscape, Adobe Photoshop, Adobe Lightroom, Adobe After Effects.

### Page Realisations — Hero
H1 : "Une selection de projets"
Sous-titre : "Scanner 3D, maquettes numeriques, rendus architecturaux — un echantillon des projets auxquels j'ai contribue au fil des 15 dernieres annees."

### Page Realisations — Titres des images (validés par le fondateur)
- **301** : Elevation facade haussmannienne
- **302** : Plans et coupes — longere renovee
- **303** : Plan d'amenagement tertiaire
- **304** : Plan d'appartement — duplex
- **305** : Plan de masse
- **401** : Complexe tertiaire
- **402** : Complexe tertiaire
- **403** : Immeuble de bureaux
- **404** : Complexe scolaire
- **501** : Immeuble de bureaux
- **502** : Complexe tertiaire (retire le "Galilee")
- **503** : Coupe — Immeuble de bureaux (vue de jour)
- **504** : Coupe — Immeuble de bureaux (vue de nuit)
- **505** : Vue aerienne — complexe scolaire
- **506** : Complexe scolaire
- **507** : Cour interieure — residence
- **508** : Complexe tertiaire
- **509** : Coupe — Immeuble de bureaux
- **510** : Complexe tertiaire (de la 3D au rendu graphique)
- **511** : Interieur plateau de bureau
- **512** : Facade et details batiment haussmannien
- **513** : Complexe scolaire (vue de nuit)

Ces legendes sont repercutees aussi sur la grille de la page d'accueil pour coherence.

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
90de168 CGV V2 + N° TVA intracommunautaire obtenu (FR47812525103)                 ← session 8
8facf37 Ajout page CGV (Conditions Generales de Vente)                            ← session 8
afeafff Page A propos : majuscule a "Architecture" ("ecole d'Architecture")       ← session 7
35a0494 Coherence editoriale : nettoyage complementaire (occurrences manquees)   ← session 7
c622d09 Coherence editoriale : suppression des "Nous / Nos / Notre"               ← session 7
ff2c87b Correction legale : retrait de "Architecte de formation"                  ← session 7
4f1d002 Ajout splash screen immersif sur la page d'accueil                        ← session 7
7974480 Ajout image signature mail (hebergée pour signatures Ionos)               ← session 6
392bf95 Ajout page 404 personnalisée
eed0dc4 Délai de réponse Contact : "48 h ouvrées" au lieu de "48 h en général"
deeff19 chore: redeploy to activate Netlify Forms detection
21c96c1 Ajout pages Prestations, Realisations, A propos, Contact et Mentions legales
5c6ed93 Ajout logos clients, image mobile hero/apropos, stats enrichies, textes prestations
e299b5a Refonte page accueil : textes, grille realisations 4x4, stats 5 blocs
a6f80f1 Refonte design : palette Encre & Ardoise, logos, contenu editorial
2f213f7 init: projet Astro ZE3D
```

Deploiements effectues sur https://ze3d-test.netlify.app :
- 3 avril 2026 : premier deploiement (session 3)
- 21 avril 2026 : deploiement complet avec toutes les pages (session 5)
- 23 avril 2026 : ajout image signature mail Ionos (session 6, commit 7974480)
- 28-29 avril 2026 : splash screen + corrections legales + harmonisation Je (session 7)
- 30 avril & 02 mai 2026 : QR codes design + page CGV + N° TVA obtenu (session 8)
- 01 juin 2026 : audit juridique CGV + date creation EI + **PREMIER DEPLOIEMENT PROD** (merge develop -> main)
- 01 juin 2026 (session 9) : **AUDIT + OPTIMISATION SEO/GEO** (5 lots, voir section 18) + **2e DEPLOIEMENT PROD** (merge develop -> main, cfd8292) + feuille de route partagee (FEUILLE_DE_ROUTE.md)
- 02 juin 2026 (session 10) : **REFONTE IDENTITE** (nouveaux logos nav/footer/splash + favicon + typo de marque ZE3D scaleX 0.75 + couleurs site bleu #3C5E7C + nouvelle signature mail) + **3e DEPLOIEMENT PROD** (merge develop -> main, f36ab70, 18 commits). Domaine ze3d.fr actif (DNS Ionos + HTTPS OK depuis le 01/06).

**Site TEST desormais fonctionnel a 100%** :
- Toutes les pages accessibles
- Formulaire de contact operationnel avec notification email vers contact@ze3d.fr (configure sur Netlify)
- Formulaire teste par le fondateur avec succes

**PREMIER DEPLOIEMENT PROD effectue le 01 juin 2026** : merge `develop` -> `main` (fast-forward 2f213f7..f48fc82, 18 commits, tout le site) puis push origin main. Deploiement auto declenche sur Netlify (site ze3d-prod). Domaine `ze3d.fr` pas encore actif a date.

**ACTIONS POST-PROD A FAIRE (voir section 17) :** verifier build Netlify ze3d-prod / RECONFIGURER notifications Netlify Forms sur le site prod (sites separes, non herite) / mettre a jour URL image signatures Ionos (ze3d-test -> ze3d-prod puis ze3d.fr) + remplacer signatures temporaires par versions definitives / connecter domaine ze3d.fr (les QR codes pointent deja vers ze3d.fr).

### Session 8 — 30 avril & 02 mai 2026 (QR codes design, page CGV, N° TVA obtenu)

**Realisations :**

**1. QR codes generes** pour les 5 URLs principales :
- `ze3d-accueil` (https://ze3d.fr)
- `ze3d-contact` (https://ze3d.fr/contact)
- `ze3d-realisations` (https://ze3d.fr/realisations)
- `ze3d-mentions-legales` (https://ze3d.fr/mentions-legales)
- `ze3d-cgv` (https://ze3d.fr/cgv)
- **Style design** : barres verticales (modules) + yeux arrondis mi-doux (radius_ratio=0.5) + bleu accent ZE3D #4A6580
- **Format double** : PNG (design colore, ~80-100 Ko) + SVG (vectoriel pur noir/blanc, ~7 Ko)
- Niveau correction d'erreur : M (15%, sans logo central)
- Script reutilisable : `scripts/generate-qr-codes.py` (Python + lib `qrcode[pil]`)
- Stockage : `Sources/QR codes/` (non commite, comme le reste de Sources/)
- Note : `ze3d.fr` pas encore actif → les QR fonctionneront des activation du domaine

**2. Page CGV creee** (`/cgv`)
- 42 sections juridiques B2B
- **Texte genere par ChatGPT (pas par un juriste qualifie)** — revue juridique humaine recommandee a terme
- Structure et style identiques a `mentions-legales.astro` (hero + sections numerotees + listes a puces)
- Apostrophes typographiques appliquees partout
- Email `contact@ze3d.fr` cliquable (sections RGPD et Reclamation)
- Lien "CGV" ajoute au footer (a cote de "Mentions legales")
- 2 versions : V1 (30 avril, commit 8facf37) puis V2 (02 mai, commit 90de168 — 10 ameliorations)
- Cle de coherence : section 22 declare explicitement que le Prestataire **n'est pas architecte** (entre autres metiers) → coherent avec la decision legale prise en session 7

**3. N° TVA intracommunautaire obtenu** : `FR47812525103`
- Format administratif (sans espace)
- Mis a jour dans CGV (sections 1 et 8) ET mentions legales
- Date de mise a jour mentions legales : 02 mai 2026
- Note section 8 CGV : ajout "a la date des presentes CGV" pour le regime fiscal (anticipe un eventuel changement sans rendre les CGV obsoletes)

**Modifications cles V2 des CGV (commit 90de168) :**
- Section 8 : N° TVA renseigne + "a la date des presentes CGV"
- Section 10 : "60 % de solde sauf echeance differente prevue dans le devis"
- Section 18 : ajout "la remise de fichiers natifs ne modifie pas la nature des livrables"
- Section 21 : "plans visuels" → "plans, visuels" (separation)
- Section 22 : "a partir des livrables" → "en lien avec les livrables" (plus protecteur)
- Section 23 : "dans le cadre des presentes CGV" + "stipulation contraire dans le devis"
- Section 24 : ajout final sur les releves indicatifs (pas certifies ni geometre-expert)
- Section 29 : ajout "utilisation chantier sans validation" + "disposition legale imperative contraire"
- Section 37 : ajout du droit de portabilite (article 20 RGPD)

**Reste a faire :**
- **Assurance RC Pro** : toujours mentionnee "en cours de souscription" dans CGV (section 30) et mentions legales. A mettre a jour des souscription effective avec : nom assureur, n° contrat, plafonds, franchises, exclusions.

---

### Session 7 — 28-29 avril 2026 (splash screen, corrections legales, harmonisation Je)

**Realisations :**

**1. Splash screen immersif sur la page d'accueil** (composant `SplashScreen.astro`) :
- Overlay plein ecran fond bleu accent #4A6580
- Logo PNG transparent centre (`/chargement-logo.png`, 1500x1500, version "fond fonce")
- Jauge circulaire SVG blanche se remplissant en 1750 ms (sens horaire depuis 12h)
- Transition de sortie : **dissolve digital** par grille de cellules ~45 px, delais aleatoires sur 800 ms
- Affiche a CHAQUE chargement de la home (pas de memorisation par session)
- Respect de `prefers-reduced-motion`
- Image source `Sources/Chargement.jpg` (fournie par fondateur, fond bleu) → finalement remplacee par PNG transparent (fond bleu de l'image causait un carre visible au dissolve)

**2. Correction legale critique sur le titre "Architecte"** :
- Page A propos : "Architecte de formation" → "Issu d'une formation en ecole d'Architecture"
- **Le fondateur n'est PAS architecte** : formation DPLG suivie mais memoire final non rendu, donc pas de diplome. Le titre est protege par la loi du 3 janvier 1977.
- Memoire persistante creee : `legal-titre-architecte.md` pour rappel cross-conversation
- Voir section 11 et section 12 (P1 page A propos)

**3. Harmonisation editoriale "Je"** (microentreprise solo, eviter les "Nous" trompeurs) :
- 2 passes de nettoyage (10 + 8 occurrences) sur 7 fichiers
- Strategie B validee : pas de possessif sur les boutons/titres, "Je" dans les textes redactionnels
- Boutons : "Nous contacter" → "Contact", "Nos prestations/realisations" → "Prestations/Realisations"
- Labels CTA : "CONTACTEZ-NOUS" → "CONTACT" sur 4 pages (Home, A propos, Prestations, Realisations)
- Mentions legales : "vous nous transmettez/contacter" → "vous me transmettez/contacter"
- Aria-labels et titres meta SEO egalement nettoyes
- Verification finale : `grep -rniE "\b(nous|notre|nos)\b" src/` → 0 resultat

**4. Bug technique notable identifie** :
- **Astro scoped CSS ne s'applique PAS aux elements crees dynamiquement en JavaScript** (ils n'ont pas le `data-astro-cid-xxx` que le selecteur attend). Symptome : background transparent + transition 0s sur les cellules de la grille du splash, donc dissolve invisible.
- **Solution :** appliquer tous les styles necessaires en INLINE via `element.style.cssText = '...'` lors de la creation JS. Voir SplashScreen.astro pour exemple.
- A retenir pour tout futur composant Astro avec des elements crees dynamiquement.

**Commits + push develop :**
- `4f1d002` Ajout splash screen immersif sur la page d'accueil
- `ff2c87b` Correction legale : retrait de "Architecte de formation"
- `c622d09` Coherence editoriale : suppression des "Nous / Nos / Notre"
- `35a0494` Coherence editoriale : nettoyage complementaire (occurrences manquees)

---

### Session 6 — 23 avril 2026 (signatures mail Ionos)

**Realisations :**
- Creation d'une image de signature mail commune aux 2 boites (logo picto + "ZE3D" en Nasalization + baseline "Scan-to-BIM · Modélisation 3D · Rendus")
- Image fournie par le fondateur : `Sources/Signature mail ZE3D.jpg` (600x180 px, 68 Ko, JPG, couleur bleu accent harmonisee)
- Hebergee dans `public/sig-ze3d-c16b6736.jpg` (nom obfusque pour discretion)
- `public/robots.txt` cree pour bloquer l'indexation des fichiers `sig-ze3d-*` par Google
- 2 templates HTML de signature dans `Sources/Signatures mail/` :
  - `signature-emmanuel.html` : image + Emmanuel Zerdoun + tel + email + site (option C "epuree", pas de titre car "Fondateur" jugé trop pompeux pour une microentreprise solo)
  - `signature-contact.html` : image + email contact@ + site (ultra epure, pas de nom ni tel ni redondance avec l'image)
- Templates faits en HTML table inline-styles (compatible Outlook desktop), polices Arial/Helvetica fallback
- URL d'image dans les templates : `https://ze3d-test.netlify.app/sig-ze3d-c16b6736.jpg` (TEMPORAIRE — voir section 17.2)

**Commit + push develop : 7974480** ("Ajout image signature mail")

### Detail des sessions 4 et 5 — 21 avril 2026 (deja commitees)

- **Session 4** :
  - Creation de la page `/prestations` (layout split zigzag, process, slider avant/apres)
  - Creation de la page `/realisations` (grille filtrable + lightbox)
  - Ajout des images 100, 201-204, 301-305, 401-404, 502, 504, 506, 508, 510 dans public/
  - Corrections orthographiques et typographiques sur l'ensemble du site
  - Uniformisation des legendes entre home et realisations
  - Textes des poles 01, 02, 03 etoffes
  - Footer : couleurs plus lisibles sur fond sombre (#8FA6C0 au lieu de #4A6580)
- **Session 5** :
  - Creation de la page `/a-propos` (5 sections : Hero, Parcours, Expertise, Demarche, CTA)
  - Creation de la page `/contact` avec Netlify Forms (7 champs + RGPD + validation custom multi-champs)
  - Creation de la page `/mentions-legales` (10 sections legales)
  - `.section-label` globalement agrandi (0.7rem -> 1.1rem)
  - Footer bottom bar : contraste renforce + ajout du lien "Mentions legales"
  - Corrections legales : formulations adoucies (sous-traitance, garantie, delais tenus)
  - Titre engagement "Rigueur" renomme en "Exigence"
  - Carte Zone d'intervention Contact : "Perpignan" supprime pour ne pas limiter geographiquement
  - Toutes les pages du site sont desormais creees — prochaine etape : commit + push + test Netlify

---

## 17. A FAIRE LORS DU DEPLOIEMENT EN PRODUCTION

**Rappels importants a transmettre au fondateur lors du merge develop -> main :**

### 17.1 Notifications Netlify Forms (a refaire sur le site prod)

Le site prod (`ze3d-prod.netlify.app`) est un site Netlify SEPARE du site test. La configuration des notifications email Netlify Forms doit etre refaite sur le site prod :

1. Aller sur https://app.netlify.com > site **ze3d-prod**
2. Onglet **Forms** (ou Site settings > Forms)
3. Cliquer sur le formulaire **contact**
4. **Notifications** > **Add notification** > **Email notification**
5. Destinataire : `contact@ze3d.fr`
6. Save

Sans cette etape, les demandes envoyees via le formulaire de la prod iront dans le dashboard mais pas dans la boite mail.

Le fondateur a deja fait cette manipulation sur le site TEST (fonctionnel).

### 17.2 Mise a jour des signatures mail Ionos (IMPORTANT)

**Etat actuel (session 6, 23 avril 2026) :**

Le fondateur a installe **une version TEMPORAIRE TRONQUEE** de ses signatures dans Ionos :
- L'image pointe vers `https://ze3d-test.netlify.app/sig-ze3d-c16b6736.jpg` (URL test temporaire)
- **La ligne "Site : ze3d.fr" a ete SUPPRIMEE manuellement** par le fondateur dans Ionos, car le site prod n'est pas encore en ligne sur ze3d.fr

**Lors du passage en prod, IL FAUT remplacer les signatures Ionos par la version DEFINITIVE :**

1. Ouvrir les fichiers HTML deja prets : `Sources/Signatures mail/signature-emmanuel.html` et `signature-contact.html` (ou les versions `.txt` "CODE-HTML" pour copier le code brut)
2. Mettre a jour les URLs de l'image dans ces fichiers : remplacer `ze3d-test.netlify.app` par la nouvelle URL (`ze3d-prod.netlify.app` puis `ze3d.fr` quand le domaine sera actif)
3. Pour CHAQUE boite mail Ionos (emmanuel.zerdoun@ et contact@) :
   - Se reconnecter a https://mail.ionos.fr
   - Parametres > Email > Signatures
   - **SUPPRIMER la signature temporaire actuelle** (sans la ligne site)
   - **COLLER la signature definitive complete** (avec la ligne "Site : ze3d.fr") en mode "Source HTML" / `<>` (le copier-coller direct ne marche pas, il faut passer par le code source)
   - Enregistrer
4. Tester en s'envoyant un mail depuis chaque boite

**Methode validee pour coller dans Ionos** : utiliser le bouton `<>` / "Source HTML" de l'editeur de signature, puis coller le contenu du fichier `.txt` "CODE-HTML". Le copier-coller depuis le rendu HTML dans le navigateur ne fonctionne pas dans Ionos.

**Le fondateur a explicitement demande qu'on lui rappelle cette etape lors du passage en prod (session 6, 23 avril 2026).**

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
- Pour acceder au site depuis un iPhone sur le meme Wi-Fi : http://192.168.0.13:4321 (avec --host)
- Le dossier Sources/ n'est PAS commite dans git (trop volumineux), seuls les fichiers dans public/ le sont
- Compte Netlify : MedreZ's team, authentification via npx netlify login dans le terminal Mac
- **Netlify Forms sur plan gratuit** : inclut les notifications email vers 1 ou 2 destinataires (pas besoin de Pro qui coute ~20$/mois). Seules les fonctionnalites avancees (Slack, webhooks multiples, etc.) sont payantes. Ne pas suggerer au fondateur de payer pour les notifications email basiques.
- La configuration des notifications email est a refaire sur chaque site Netlify (TEST et PROD sont des sites separes) — voir section 17
- **Bug Astro scoped CSS** : le scoped CSS d'Astro (selecteurs `[data-astro-cid-xxx]`) ne s'applique PAS aux elements crees dynamiquement en JavaScript car ils n'ont pas l'attribut data-astro-cid. Symptome typique : styles invisibles, transitions a 0s. **Solution :** appliquer tous les styles necessaires en INLINE via `element.style.cssText = '...'` lors de la creation JS. Voir `SplashScreen.astro` pour exemple complet (bug rencontre en session 7).

### Notes juridiques importantes (audit CGV session 8)

- 🔴 **MENTION OBLIGATOIRE SUR CHAQUE DEVIS (decision 02 juin 2026, reperage CGV)** — pour rendre les CGV OPPOSABLES au client, inscrire sur TOUT devis la mention exacte :
  > « Le Client reconnaît avoir pris connaissance et accepté sans réserve les Conditions Générales de Vente du Prestataire, disponibles sur ze3d.fr/cgv et jointes au présent devis. »
  Ideale + case « Bon pour accord, lu et approuvé » datee/signee. **Sans cette mention, toutes les clauses protectrices des CGV (§21-30) risquent d'etre INOPPOSABLES** — c'est le point juridique n°1 (le reperage a confirme que les CGV elles-memes sont bien redigees ; la faille est l'acceptation).
- **Protection patrimoniale acquise par defaut** : EI creee le 01 avril 2026 → loi du 14 fevrier 2022 applicable → separation patrimoniale automatique (patrimoine perso protege des creanciers pros). Residence principale insaisissable (loi Macron 2015, automatique). **Ne jamais signer de renonciation a cette protection** (banquier, assureur, client).
- **Pas de RC Pro souscrite a date** : aucun assureur n'a propose de RC Pro adaptee — uniquement de la decennale (refusee). Pistes a re-explorer : Hiscox / April / AssurUp / Verspieren (courtiers specialises digital, pas BTP). Bien se presenter comme "prestataire de services numeriques / production graphique", pas "ingenierie BTP" (le code APE 71.12B oriente faussement vers le BTP).
- **Code APE 71.12B (Ingenierie, etudes techniques)** : positif pour la credibilite technique, negatif pour les assureurs qui assimilent au BTP. Eventuellement a reevaluer si necessite.
- **Risques residuels CGV** :
  - §29 — plafond au montant HT pourrait etre ecarte par juge (art. 1170 Code civil) si dommage >> prestation
  - §23 — refus decennale pourrait etre ecarte si requalification en "MOE de fait" (art. 1792). Eviter dans les devis : "validation technique", "plans d'execution", "DCE"
  - Acceptation CGV faible si pas de signature explicite client → renforcer via mention "Bon pour accord / lu et approuve CGV" sur chaque devis
- **Recommandations CGV** (a appliquer si voulu) :
  - §40 : specifier Tribunal de commerce de Paris (juridiction d'attache)
  - Ajouter clause non-retractation B2B (article L.221-3 Code conso)
- ~~**Assurance RC Pro** : actuellement mentionnee "en cours d'obtention" dans les CGV (section 30) ET dans les mentions legales. Lors de la souscription effective, mettre a jour les 2 pages avec les references (assureur, n° contrat, plafonds, franchises).~~ **CHANGEMENT DE POSITION (PDF du 02 mai, integre session 8)** : la position juridique a ete revue. CGV section 30 et mentions legales section 3 declarent maintenant explicitement que "les prestations ne sont pas couvertes par une assurance RC Pro specifique" et que le Prestataire "ne dispose pas d'assurance decennale". C'est une position plus transparente juridiquement. Si une RC Pro est souscrite ulterieurement, modifier les 2 pages pour mettre a jour.
- ~~**TVA intracommunautaire** : meme remarque, "en cours d'obtention" mentionne dans CGV (section 1) et mentions legales. A mettre a jour des attribution.~~ **OBTENUE en session 8 (02 mai 2026) : FR47812525103**. Mise a jour effectuee dans CGV (sections 1, 8) et mentions legales.

---

## 16. REGLE — CORRECTION AUTOMATIQUE DES TEXTES

**A chaque fois que le fondateur fournit un texte destine a etre integre au site** (titre,
paragraphe, legende, bouton, meta-description, etc.), Claude DOIT :

1. **Verifier systematiquement** :
   - Orthographe (accents, lettres manquantes, fautes frappe)
   - Accords (genre, nombre, conjugaison)
   - Syntaxe (structure de phrase, clarte)
   - Ponctuation (virgules, points, points-virgules)
   - Typographie francaise :
     - Apostrophes typographiques (' et non ')
     - Espaces insecables avant `: ; ! ?` et `«»`
     - Tirets cadratins `—` pour les incises (pas `-` simple)
     - Guillemets francais `« »` plutot qu'anglais `" "`
     - Majuscules accentuees (À, É, etc.) si necessaire
   - Fluidite / naturel (eviter les lourdeurs, redondances)

2. **Si des corrections sont necessaires** :
   - Presenter la version corrigee au fondateur AVANT d'appliquer
   - Expliquer brievement les corrections (ex: "\"retro ingineering\" -> \"retro-ingenierie\"")
   - Attendre la validation du fondateur avant de modifier le fichier

3. **Si le texte est parfait** :
   - L'appliquer directement sans friction

**Exceptions** (ne PAS corriger) :
- Choix stylistiques volontaires deja identifies (ex: "Maquettes Numeriques" en majuscules)
- Termes techniques BIM/3D specialises (Revit, BIM, LOD, IFC, Enscape, etc.)
- Noms propres d'entreprises (meme si orthographe inhabituelle)

**Important :** Cette regle s'applique a TOUS les textes destines au site, meme les petites
modifications ponctuelles (une phrase changee dans un titre, un mot ajoute dans un badge, etc.).


---

## 19. 🔴 REGLE — COHERENCE AVEC LES MENTIONS LEGALES & LES CGV (demande explicite 04/06/2026)

**AVANT de mettre en place QUOI QUE CE SOIT** sur le site, dans les outils ou dans la
communication (script tiers, cookie, outil de mesure, integration externe, nouvelle fonctionnalite,
formulaire, paiement, partenaire, mention marketing, etc.), Claude DOIT **systematiquement
verifier que cela ne contredit PAS** ce qui est ecrit dans :
- `src/pages/mentions-legales.astro`
- `src/pages/cgv.astro`

C'est une **responsabilite de Claude, pas du fondateur** (« ta memoire est censee etre meilleure
que la mienne »). Le fondateur n'a pas a se souvenir de chaque clause — Claude doit faire le
controle de coherence **de lui-meme** et alerter AVANT d'agir.

**Points de vigilance connus a re-verifier a chaque fois :**
- **§6 Cookies (mentions legales)** : le site declare « **n'utilise aucun cookie de tracage, de
  mesure d'audience ou de publicite. Aucun outil d'analyse tiers (Google Analytics, Meta Pixel,
  etc.) n'est integre** ». → Interdit d'ajouter GA4, Meta Pixel, Hotjar, ou tout tracker/cookie
  sans **reformuler cette section ET** prevoir le consentement RGPD si besoin.
- **§ RGPD / collecte de donnees** : tout nouveau champ de formulaire ou nouvelle finalite de
  traitement doit etre couvert par la politique RGPD affichee.
- **CGV** : tout nouveau service, mode de paiement, delai, garantie ou clause commerciale annoncee
  sur le site doit etre coherent avec les CGV (et inversement).

**Procedure si conflit detecte :** STOP → expliquer le conflit au fondateur (citer le passage exact)
→ proposer les options (renoncer / choisir une alternative conforme / modifier la page legale) →
attendre sa decision AVANT d'implementer.

**Cas resolu (04/06/2026) :** demande GA4 → conflit avec §6 Cookies detecte → GA4 **abandonne pour
l'instant**. On reste sur **Google Search Console** (deja en place, aucun cookie, aucune modif
legale). Si mesure d'audience souhaitee plus tard → outil **sans cookie** (Plausible/Netlify) +
reformulation legale, PAS GA4 standard (qui imposerait un bandeau de consentement).

---

## 18. SEO / GEO (session 9 — 01 juin 2026)

**Audit complet (13 agents) puis optimisation en 5 lots, PERIMETRE STRICTEMENT INVISIBLE/TECHNIQUE** (jamais de modif du contenu visible, de l'UX ni du visuel). 5 commits sur develop (836c631 -> 6a457a3).

### Ce qui a ete fait
- **Lot 1 — Config technique** : `site: 'https://ze3d.fr'` + `@astrojs/sitemap` (sitemap auto, exclut cgv/mentions/404) ; prop `noindex` dans Layout -> CGV + mentions + 404 en `noindex,follow` ; `Sitemap:` dans robots.txt ; **`netlify.toml`** (cache assets/polices + en-tetes securite, PAS de CSP pour eviter tout blocage).
- **Lot 2 — JSON-LD (GEO)** : socle global via Layout (`ProfessionalService` + `WebSite`) sur pages indexables uniquement ; par page : Prestations = BreadcrumbList + 3 Service ; Realisations = BreadcrumbList + CollectionPage/ItemList (22 projets) ; A propos = BreadcrumbList + Person (jobTitle **"Expert BIM"**, JAMAIS "Architecte") + AboutPage ; Contact = BreadcrumbList + ContactPage. Tout aligne sur le contenu visible, rien d'invente. Prop `schemas` du Layout.
- **Lot 3 — Perf polices** : preconnect Google Fonts + preload Nasalization.otf (display:swap deja en place, pas touche au CSS).
- **Lot 4 — Images anti-CLS** : width/height (dimensions reelles) + decoding="async" partout. Sans risque car toutes les images concernees sont en `object-fit:cover` (taille pilotee par CSS).
- **Lot 5 — WebP** : 31 images de contenu converties en WebP q82 via `scripts/generate-webp.mjs` (sharp), originaux JPG/PNG **conserves** en repli. Wrapping `<picture><source webp>`. `global.css : picture { display: contents }` = wrapper transparent (verifie au rendu : layout intact, webp bien servi). **Poids images 89,6 Mo -> 15,8 Mo (-82%)**. + **`og-default.jpg` 1200x630** creee depuis le rendu 509 (aperçus sociaux repares).

### Decisions du fondateur (session 9)
- JSON-LD adresse = **Perpignan** (zone reelle), pas Paris.
- WebP haute qualite **autorise** (originaux conserves).
- og:image = derivee d'un **rendu existant** (509).

### ⚠️ POINTS EN ATTENTE / A SURVEILLER (SEO)
1. **ADRESSE : RESOLU (01/06/2026)** — Le **siege social declare = "47 rue Vivienne, 75002 Paris"** (domiciliation legitime, affiche dans mentions-legales + CGV). Le **lieu d'activite = Perpignan** (utilise dans le JSON-LD LocalBusiness pour le SEO local). Le double affichage (legal = Paris / SEO = Perpignan) est **VOLONTAIRE et valide par le fondateur** — ce n'est PAS une incoherence a corriger. NE PAS modifier les pages legales. (Pour memoire : SIRET 812 525 103 00022, tel +33 6 73 04 21 28.)
2. **Code postal Perpignan dans le JSON-LD = "66000" — CONFIRME par le fondateur le 01/06/2026** (orgLd.address.postalCode dans Layout.astro). OK definitif.
3. **Telephone +33673042128 expose** dans le JSON-LD (le fondateur a valide "oui"). C'est son numero perso/pro.
4. **sameAs (reseaux sociaux) = VIDE** : a ajouter dans orgLd (Layout) quand les comptes existeront.
5. **AggregateRating (avis) = ABSENT** : a ajouter quand des avis verifiables existeront (societe en creation).
6. **Analytics = AUCUN** : prevoir GA4 + Google Search Console + Bing Webmaster ulterieurement (le fondateur n'a rien pour l'instant).
7. **A l'activation du domaine ze3d.fr** : soumettre le sitemap (`https://ze3d.fr/sitemap-index.xml`) a Google Search Console + Bing.
8. Le script `scripts/generate-webp.mjs` est a relancer si de nouvelles images sont ajoutees a public/realisations ou public/prestations.

---

## 20. REFONTE CHARTE GRAPHIQUE (05/06/2026)

### Source canonique UNIQUE de l'identite
**`Sources/Charte graphique/`** est desormais la **seule source de verite** graphique (site, cartes de visite, factures, signatures). Contenu :
- **4 elements de base** : `Logo ZE3D - Logotype.png` (fond clair, liseré noir) · `Logo ZE3D - Logotype FF.png` (fond fonce, liseré blanc) · `Logo ZE3D - Nom.png` (« ZE3D » Nasalization, tracking 0, V100/H75, #3C5E7C) · `Logo ZE3D - Phrase.png` (« Scan-to-BIM · Modélisation · Rendus »).
- **Assemblages** : `LN` (logotype+nom) · `LNP` (logotype+nom+phrase) (+ versions FF).
- **Favicon** : `Logo ZE3D - Favicon.png` (recadrage « ZE » sur cercle blanc) — NOUVEAU favicon (remplace l'ancien monogramme cartouche).
- **Signature** : `Logo ZE3D - Signature.jpg` (1500x550, = LNP HD).

### Generation des assets du site
**`scripts/rebuild-brand-assets.py`** (Python/PIL) regenere TOUT depuis Charte graphique, a dimensions calees (rendu identique) :
- `public/logo-ln.png` (header, depuis LN) · `public/logo-fond-fonce.png` (footer, depuis Logotype FF) · `public/chargement-logo.png` (splash : logotype centre 1500x1500 + **halo blanc doux** flou=100 / opacite plafond=128 ≈ 50%).
- Favicons (favicon.ico 16/32/48, favicon-16/32.png, apple-touch-icon 180, icon-512) depuis Favicon.png.
- `public/og-ze3d-card.jpg` (1200x1200, LNP centre sur blanc).
- **Relancer ce script apres toute modif des sources Charte graphique.**

### Modifs site (sur develop, NON encore deployees au 05/06)
- **Header** (`Navigation.astro`) : montage (img logotype + texte) remplace par 1 seule image `/logo-ln.png` (h 68px). Span `.nom-brand-name` + son CSS supprimes. `.brand-ze3d` conservee (utilisee ailleurs).
- **Footer** : `logo-fond-fonce.png` (nouveau logotype FF), attrs 63x120.
- **JSON-LD** (`Layout.astro`) : `logo` -> `/logo-ln.png`.
- **Signature** : nouveau fichier `public/sig-ze3d-886c4914.jpg` (490x180, affichage 245x90). Les 4 fichiers `Sources/Signatures mail/` mis a jour.
- **Favicon change** (ancien monogramme -> nouveau « ZE »).

### Menage effectue (05/06)
Supprime : `Sources/Logo/` (entier), anciennes sources racine (`ZE3D logo - pour fond clair/fonce.png`, `favicon.png`, `512x512.png`, `ze3d-card.png`, `Chargement.jpg`, `simulation-google-serp.png`, anciennes signatures), `Sources/GBP photos/logo-gbp*`, `public/logo-fond-clair.png`, anciens `public/sig-ze3d-9f8c8305.jpg` + `-c16b6736.jpg`. `CLAUDE_2.md` (brief initial, dépassé) supprime. `.DS_Store` + `start-dev.sh` (cassé) supprimes.
`Sources/` reorganise : `Charte graphique/` · `Rendus/` (30 rendus numerotes) · `GBP photos/` · `QR codes/` · `Signatures mail/` · `Photos/`.

### Document charte graphique
- **`Sources/Charte graphique/charte-graphique-ZE3D.html`** = source du document (12 pages : couverture + sommaire cliquable + Partie A identite + Partie B charte du site, extraite de `global.css`). Police = **DM Sans** (comme le site) ; « ZE3D » en `.ze3d` (Nasalization H75) ; `ze3d.fr` = texte normal.
- **PDF** : `Sources/Charte graphique/Charte graphique - ZE3D.pdf` — genere via Chrome headless :
  `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="Charte graphique - ZE3D.pdf" "file://.../charte-graphique-ZE3D.html"` (liens du sommaire cliquables dans le PDF).
- **Hebergement** : fichier LOCAL uniquement (choix fondateur, pas de page en ligne).
- 🔴 **REGLE DE MISE A JOUR** : a CHAQUE modif d'identite (sources) ou de design du site (global.css), **mettre a jour le HTML de charte + regenerer le PDF**. C'est la version « dynamiquement a jour » en mode local.

### 🔵 RAPPELS MANUELS pour le fondateur (apres deploiement)
1. **Reuploader le nouveau logo** sur la fiche Google Business (l'ancien `logo-gbp.jpg` a ete supprime ; repartir de `Sources/Charte graphique/`).
2. **Recoller les 2 signatures** dans Ionos (nouvelle image `sig-ze3d-886c4914.jpg`) — uniquement APRES deploiement prod (sinon l'image n'existe pas encore en ligne).

---

## 21. PDF JURIDIQUES OFFICIELS — mentions légales + CGV (06/06/2026)

- **Script** : `scripts/generate-legal-pdfs.py`. Genere les PDF officiels des **Mentions legales** et **CGV** depuis le texte EXACT des `.astro` (`src/pages/mentions-legales.astro`, `src/pages/cgv.astro`), mis en page sur l'identite du site (DM Sans, logo LN, `.brand-ze3d` Nasalization, accent #3C5E7C) : en-tete logo + identite societe, dates (Version du / Document genere le), pied de page + **numerotation** sur chaque page (via `@page` margin boxes, rendu par Chrome headless).
- **Sortie (Synology)** sous `…/00 - SOCLE/02 - JURIDIQUE/` :
  - `03 - MENTIONS LEGALES/Mentions légales ZE3D - AA-MM.pdf`
  - `02 - CGV/CGV ZE3D - AA-MM.pdf`  *(AA=annee 2 chiffres, MM=mois ; ex. `26-06`)*
- **Archivage automatique** : a chaque regeneration, l'ancien fichier du dossier principal est deplace dans `00 - ARCHIVES/` (avec un indice ` (n)` si collision de nom — ex. plusieurs versions le meme mois). Le dossier principal contient TOUJOURS la derniere version.
- 🔴 **REGLE** : a CHAQUE modif de `mentions-legales.astro` et/ou `cgv.astro`, relancer **`python3 scripts/generate-legal-pdfs.py`** → regenere le PDF + archive l'ancienne version automatiquement.
- **« ZE3D » en typo de marque partout** : en-tete/corps via `.brand-ze3d` (Nasalization + ratio H75) ; pied de page via une **image tamponnee** (PyMuPDF) derivee de `Sources/Charte graphique/Logo ZE3D - Nom.png` (proportions exactes), car Chrome ne rend pas d'image dans les margin-boxes. Reste du pied en **DM Sans**.
- **Dependances du script** : Pillow (PIL) + PyMuPDF (`fitz`) — `pip3 install pillow pymupdf`.
- Verifie le 06/06/2026 : Mentions 4 p., CGV 18 p., mise en page officielle OK (en-tete logo, dates, pied + numerotation).

### Automatisation (mise a jour + archivage auto) — 06/06/2026
- **Hook `Stop`** (`.claude/settings.local.json`) → `scripts/auto-legal-pdf.sh` : a la fin de chaque tour, SI `mentions-legales.astro` ou `cgv.astro` a ete modifie (compare au marqueur `scripts/.legal-pdf.stamp`), relance `generate-legal-pdfs.py`.
- Le script ne regenere QUE le document dont la source a change (mtime source > mtime PDF), et **archive automatiquement** la version precedente dans `00 - ARCHIVES` (indice ` (n)` si collision). `--force` pour tout regenerer.
- Regeneration manuelle : `python3 scripts/generate-legal-pdfs.py`.
- Note : le hook se declenche dans une session Claude Code ; si la source est editee hors session, la regeneration aura lieu au tour suivant (auto-rattrapage).
- **CGV telechargeable sur le site (06/06)** : bouton « Telecharger les CGV (PDF) » sur `/cgv` → `/cgv-ze3d.pdf`. Le script publie une copie a NOM STABLE dans `public/cgv-ze3d.pdf` (rafraichie a chaque regen CGV). ⚠️ La version EN LIGNE ne se met a jour qu'au prochain **deploiement** (commit + merge main). Les **mentions legales** restent en HTML seul (pas de PDF telechargeable — choix fondateur, suffisant legalement).

---

## 22. 🎨 STANDARD DE PRESENTATION DES DOCUMENTS OFFICIELS ZE3D

**Tout document officiel genere pour ZE3D (mentions, CGV, et a venir : devis, factures, attestations, courriers…) DOIT suivre cette presentation** (reference : `scripts/generate-legal-pdfs.py`) :

- **Police** : **DM Sans** (corps + titres), comme le site. Mono `SF Mono/Menlo` uniquement pour code/valeurs techniques.
- **« ZE3D »** : TOUJOURS en typo de marque (Nasalization, MAJ, ratio **H 75 %**, tracking 0). Jamais en police normale.
  - En-tete / corps / titres → classe `.brand-ze3d` (Nasalization + `scaleX(.75)` + `margin-right:-.71em`).
  - Pieds de page / zones « margin-box » PDF (ou le CSS transform est impossible) → **image** tamponnee via PyMuPDF depuis `Sources/Charte graphique/Logo ZE3D - Nom.png` (proportions exactes).
  - **`ze3d.fr`** (URL) et e-mails = **texte normal**, jamais le style logo.
- **Couleurs** : accent **`#3C5E7C`** (filets, titres de section, kicker) ; texte `#1A2530`/`#26323f` ; gris secondaire `#6b7682` ; gris pied `#9aa3ad` ; fonds doux `#F3F5F7`.
- **En-tete (letterhead)** : logo **`public/logo-ln.png`** a gauche + bloc identite a droite (`ZE3D — Emmanuel Zerdoun EI`, SIRET 812 525 103 00022, TVA FR47812525103, 47 rue Vivienne 75002 Paris, ze3d.fr, contact@ze3d.fr) + filet accent dessous.
- **Bloc titre** : kicker MAJ accent (« Document … officiel ») · titre DM Sans 700 · sous-titre `ZE3D — Emmanuel Zerdoun EI` · meta = **« Version du [date d'effet] » UNIQUEMENT** (PAS de date de generation : figee/trompeuse sur un PDF statique ; le mois de production reste dans le nom du fichier d'archive). Date en francais.
- **Pied de page (chaque page)** : gauche = image **ZE3D** (Nom.png) · centre = « {type} · Document officiel » · droite = « Page X / Y ». Tout en DM Sans gris `#9aa3ad`, numerotation via `@page` margin boxes.
- **Format** : A4, marges ~18mm. Genere via **Chrome headless** (HTML → PDF) + tampon image (PyMuPDF) pour le ZE3D du pied.
- **Nommage / archivage** : `{Type} ZE3D - AA-MM.pdf` ; ancienne version → `00 - ARCHIVES` (indice si collision).

---

## 23. SAUVEGARDE AUTO DE `Sources/` (06/06/2026)

- **But** : le code est deja sauvegarde sur GitHub ; `Sources/` (gitignore, ~94 Mo : rendus, charte, GBP, QR, signatures, photos) est le SEUL element non versionne → copie miroir sur le serveur pro Synology (sauvegarde auto).
- **Script** : `scripts/backup-sources.sh` → `rsync -a --delete` de `Sources/` vers `SynologyDrive-ZE3D/05 - SITE/01 - CLAUDE CODE/Sources/` (vrai miroir ; Synology garde ses propres versions).
- **Auto** : 2ᵉ commande du hook `Stop` (`.claude/settings.local.json`) — ne resynchronise que si `Sources/` a change (marqueur `scripts/.sources-backup.stamp`). Lancable a la main : `bash scripts/backup-sources.sh`.
- Le projet **reste** dans `~/Documents/SITE WEB` (pas de deplacement — choix fondateur : dev local + GitHub + cette sauvegarde Sources).
- NB : l'ancien dossier doublon `05 - SITE/00 - SOURCES - IMAGES/` (82 Mo de rendus) a ete **supprime par le fondateur** le 06/06 ; le miroir ci-dessus est desormais l'**unique** copie des sources sur le serveur.
- Option launchd (sauvegarde quotidienne planifiee par macOS) **ecartee** : bloquee par la protection de confidentialite macOS (TCC) sur Documents/CloudStorage (« Operation not permitted ») sauf a accorder l'Acces complet au disque a /bin/bash. Choix fondateur = rester sur le hook Claude (qui herite des autorisations de Claude Code).
