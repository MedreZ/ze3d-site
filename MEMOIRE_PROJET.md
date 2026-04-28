# MEMOIRE PROJET — Site vitrine ZE3D
# Derniere mise a jour : 23 avril 2026 — Session 6 (signatures mail Ionos)

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

### Pages existantes (TOUTES CREEES)
- **Accueil** (`index.astro`) — Hero, Prestations, A propos, Stats, Realisations, CTA
- **Prestations** (`prestations.astro`) — Hero + Process 4 vignettes + Slider avant/apres + 3 poles detailles + CTA
- **Realisations** (`realisations.astro`) — Hero + Filtres (Tout/2D/3D/Rendu) + Grille 22 images + Lightbox + CTA
- **A propos** (`a-propos.astro`) — Hero + Mon parcours + Expertise (2 cols) + Ma demarche (4 engagements) + CTA
- **Contact** (`contact.astro`) — Hero + Formulaire Netlify Forms (7 champs + RGPD) + Infos contact + CTA alternatif
- **Mentions legales** (`mentions-legales.astro`) — 10 sections (Editeur, Hebergeur, Assurance, PI, RGPD, Cookies, etc.)

### Pages a creer
Aucune — toutes les pages du site sont desormais creees.

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
- **Mention "Architecte de formation"** dans le paragraphe 1 (formulation legale OK car "de formation" = non protege)

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
**P1 (avec mention legale "Architecte de formation") :**
"**Architecte de formation**, j'ai debute ma carriere en cabinet de maitrise d'oeuvre parisien ou j'ai occupe pendant plus de 15 ans les fonctions de dessinateur projeteur, puis de Responsable du pole 3D et de BIM Coordinateur. J'y ai pilote des projets d'envergure pour des acteurs tels que la CNAV, la CAF, l'OFII, Capgemini ou Optical Center."

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
- TVA intracommunautaire : en cours d'obtention
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
7974480 Ajout image signature mail (hebergée pour signatures Ionos)   ← session 6
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

**Site TEST desormais fonctionnel a 100%** :
- Toutes les pages accessibles
- Formulaire de contact operationnel avec notification email vers contact@ze3d.fr (configure sur Netlify)
- Formulaire teste par le fondateur avec succes

Aucun deploiement prod effectue pour le moment.

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
