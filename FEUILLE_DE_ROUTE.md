# Feuille de route — ZE3D

> Suivi partagé Manu ⇄ Claude. On coche au fur et à mesure.
> Légende : `[ ]` à faire · `[~]` en cours · `[x]` fait

Dernière mise à jour : **01 juin 2026**

---

## 🚀 1. Déploiement PROD

- [x] Merge `develop → main` (mise en ligne du chantier SEO/GEO)
- [x] Vérifier que le build **ze3d-prod** passe au vert sur [app.netlify.com](https://app.netlify.com)
- [x] **Notifications Netlify Forms** sur ze3d-prod : email → `contact@ze3d.fr`
      (créée via l'API Netlify le 01/06/2026, réplique de la config test validée)
- [ ] Test final : soumettre une fois le formulaire de contact en prod et vérifier la réception de l'email

## 🌐 2. Domaine ze3d.fr

- [x] Côté Netlify : `ze3d.fr` ajouté comme domaine principal de ze3d-prod + alias `www.ze3d.fr` (via API, 01/06/2026)
- [x] Côté Ionos (DNS) : **A `@` → 75.2.60.5** + **CNAME `www` → ze3d-prod.netlify.app** (fait par Manu, propagé)
- [x] DNS résout correctement + **certificat HTTPS émis** (ze3d.fr + www), renouvellement auto
- [x] Forme principale = apex `ze3d.fr` ; www → 301 → apex ; http → 301 → https
- [x] **ze3d.fr EN LIGNE** ✅ (site servi, sitemap accessible, canonical OK) — 01/06/2026

## ✉️ 3. Signatures mail Ionos *(rappel explicite demandé)*

- [x] URL de l'image mise à jour dans les 4 fichiers `Sources/Signatures mail/`
      (`ze3d-test.netlify.app` → `ze3d.fr`) — image vérifiée accessible (01/06/2026)
- [ ] **Manu** : remplacer dans Ionos les 2 signatures par les **versions définitives
      complètes** (fichiers `*-CODE-HTML.txt`), via le mode Source HTML `<>`
      — `signature-emmanuel-CODE-HTML.txt` pour emmanuel.zerdoun@ze3d.fr
      — `signature-contact-CODE-HTML.txt` pour contact@ze3d.fr

## 🔍 4. Référencement *(une fois ze3d.fr actif)*

- [ ] Créer / valider **Google Search Console** → soumettre `https://ze3d.fr/sitemap-index.xml`
- [ ] Créer **Bing Webmaster Tools** → soumettre le sitemap
- [ ] Tester le JSON-LD (Google Rich Results Test + validator.schema.org)
- [ ] Vérifier les **QR codes** (ils pointent déjà vers `ze3d.fr`)
- [ ] (option) Créer une fiche **Google Business Profile** (Perpignan) — booste fort le SEO local

## 📊 5. Analytics & mesure

- [ ] Créer un compte **GA4** → me communiquer l'ID `G-XXXXXXX` → je l'intègre proprement
- [ ] (option) Google Tag Manager si besoin de plusieurs tags
- [ ] Lier GA4 ↔ Search Console

## 🧩 6. Enrichissement SEO / GEO *(quand les éléments existeront)*

- [ ] **Réseaux sociaux** créés → ajouter `sameAs` dans le JSON-LD (Layout.astro)
- [ ] **Premiers avis clients** vérifiables → ajouter `AggregateRating`
- [ ] (option) Chargement **non-bloquant des polices** (gain perf, déjà évalué sûr)
- [ ] Relancer `node scripts/generate-webp.mjs` à chaque ajout d'images dans `public/`

## 🛡️ 7. Sécurité & juridique

- [ ] **Révoquer le token GitHub** exposé en clair dans l'URL du remote git
      → repasser par `gh auth login` ou le trousseau macOS
- [ ] Explorer une **RC Pro** (Hiscox / April / AssurUp / Verspieren) —
      se présenter comme « prestataire de services numériques », pas « ingénierie BTP »
- [ ] (rappel) **Revue juridique humaine des CGV** (rédigées par ChatGPT, pas un juriste)

## 🎨 8. Refonte logo & charte couleurs *(en cours, 02/06/2026)*

**Nouvelle palette de marque** (fournie par Manu) :
| Rôle | Hex |
|---|---|
| Jaune principal | `#FCC982` |
| Jaune secondaire 1 | `#FFDFB2` |
| Jaune secondaire 2 | `#DFAC65` |
| Bleu principal | `#6795BB` |
| Bleu secondaire 1 | `#82AFD6` |
| Bleu secondaire 2 | `#3C5E7C` |

- [x] Nouveaux logos verticaux fournis (`Sources/Logo/logo-new-fond-clair.png` + `-fonce.png`, 608×1105, transparents)
- [x] **nav** (`logo-fond-clair.png`) + **footer** (`logo-fond-fonce.png`) + **splash** (`chargement-logo.png` recomposé) → mis à jour et déployés sur develop
- [ ] **Favicon** : en attente d'un **symbole carré** de Manu (specs données) → je génère favicon.svg + .ico + apple-touch-icon
- [ ] **Signature mail** : **Manu refait l'image lui-même** (specs : 600×180, JPG fond blanc < 100 Ko). Ensuite : soit Option A = il me donne l'image → je l'héberge sous un nouveau nom + maj des 4 fichiers + il recolle dans Ionos ; soit Option B = il l'uploade directement dans Ionos (les 4 fichiers du repo deviennent alors obsolètes). Choix à confirmer.
- [ ] **Couleur du site (CSS) + QR codes** : à revoir ensuite (décision Manu) — actuellement le site reste en bleu ardoise `#4A6580`

---

### Notes de contexte
- **main = production**, **develop = test (ze3d-test)**. Ne jamais merger vers main sans validation.
- **Adresse** : siège déclaré = 47 rue Vivienne, 75002 Paris (domiciliation, pages légales) /
  activité = Perpignan 66000 (JSON-LD SEO local). Double affichage **volontaire**, ne pas « corriger ».
- Détails techniques complets dans `MEMOIRE_PROJET.md` (section 18 pour le SEO/GEO).
