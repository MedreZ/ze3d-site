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
- [~] Côté Ionos (DNS) : enregistrement **A `@` → 75.2.60.5** + **CNAME `www` → ze3d-prod.netlify.app** *(en cours, fait par Manu)*
- [ ] Vérifier la résolution DNS + provisioning du certificat HTTPS (Netlify, auto)
- [x] Forme principale = apex `ze3d.fr` (cohérent avec canonical/sitemap/JSON-LD déjà en `https://ze3d.fr`), www redirige vers apex

## ✉️ 3. Signatures mail Ionos *(rappel explicite demandé)*

- [ ] Mettre à jour l'URL de l'image dans les 4 fichiers `Sources/Signatures mail/`
      (`ze3d-test.netlify.app` → `ze3d.fr`)
- [ ] Remplacer dans Ionos les signatures temporaires par les **versions définitives
      complètes** (avec la ligne « Site »), via le mode Source HTML `<>`

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

---

### Notes de contexte
- **main = production**, **develop = test (ze3d-test)**. Ne jamais merger vers main sans validation.
- **Adresse** : siège déclaré = 47 rue Vivienne, 75002 Paris (domiciliation, pages légales) /
  activité = Perpignan 66000 (JSON-LD SEO local). Double affichage **volontaire**, ne pas « corriger ».
- Détails techniques complets dans `MEMOIRE_PROJET.md` (section 18 pour le SEO/GEO).
