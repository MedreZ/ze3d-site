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
- [x] Test final : formulaire de contact en prod testé, email bien reçu (02/06/2026)

## 🌐 2. Domaine ze3d.fr

- [x] Côté Netlify : `ze3d.fr` ajouté comme domaine principal de ze3d-prod + alias `www.ze3d.fr` (via API, 01/06/2026)
- [x] Côté Ionos (DNS) : **A `@` → 75.2.60.5** + **CNAME `www` → ze3d-prod.netlify.app** (fait par Manu, propagé)
- [x] DNS résout correctement + **certificat HTTPS émis** (ze3d.fr + www), renouvellement auto
- [x] Forme principale = apex `ze3d.fr` ; www → 301 → apex ; http → 301 → https
- [x] **ze3d.fr EN LIGNE** ✅ (site servi, sitemap accessible, canonical OK) — 01/06/2026

## ✉️ 3. Signatures mail Ionos *(rappel explicite demandé)*

- [x] URL de l'image mise à jour dans les 4 fichiers `Sources/Signatures mail/`
      (`ze3d-test.netlify.app` → `ze3d.fr`) — image vérifiée accessible (01/06/2026)
- [x] **Les 2 signatures Ionos mises à jour et VÉRIFIÉES (04/06/2026)** : versions définitives
      complètes collées (image cliquable → ze3d.fr, libellés #3C5E7C) pour emmanuel.zerdoun@ze3d.fr
      et contact@ze3d.fr. ✅ Plus rien à faire côté signatures.

## 🔍 4. Référencement *(une fois ze3d.fr actif)*

- [x] **Google Search Console** : déjà configuré par Yoan (ami, hébergement). Sitemap `sitemap-index.xml` soumis (2 juin), lu (3 juin), état « Opération effectuée », **5 pages découvertes** (= les 5 pages indexables ; noindex bien exclues). Données structurées détectées (Fils d'Ariane, Métadonnées image). Google explore activement (165 demandes/90j). **Manu = utilisateur ajouté par Yoan, PAS propriétaire confirmé.**
- [ ] (option, autonomie) **Manu devenir propriétaire confirmé** de la propriété GSC → via DNS TXT chez Ionos. Pas urgent.
- [x] **Bing Webmaster Tools créé (04/06/2026)** : site `ze3d.fr` importé en 1 clic depuis Google Search Console (compte Google `zerdoun.emmanuel@gmail.com`, rôle Lire/Modifier — pas de vérification technique nécessaire) + **sitemap `https://ze3d.fr/sitemap-index.xml` soumis** (statut « Traitement »). Compte Microsoft `emmazer@gmail.com`. Couvre aussi l'indexation pour les IA (ChatGPT Search, Copilot, DuckDuckGo) → renforce le volet GEO. Aucun cookie/script ajouté au site (conforme mentions légales).
- [x] **Google Business Profile CRÉÉE (02/06/2026) + FINALISÉE (04/06/2026)** : entreprise de zone de service (Perpignan/66/Occitanie), catégorie principale « Agence de design » **+ secondaire « Graphiste »**, 8 services (Modélisation 3D, BIM, Scan to BIM, relevé, nuage de points, rendu 3D, visualisation, plans 2D), description optimisée, horaires L-V, photos = rendus optimisés (`Sources/GBP photos/`). Tél NON renseigné (perso). Validée auto. **Logo ajouté** (logo ZE3D vertical complet, `Sources/GBP photos/logo-gbp.jpg` = copie de `Sources/Logo/logo-new-fond-clair.jpg`, 1200×1200 fond blanc) + **photo de couverture** ajoutée. Catégorie « Graphiste » + logo + bannière **en attente de validation Google** (normal, qq heures à 2-3 j). **RESTE le levier n°1** : collecter des **avis clients** (bouton « Demander des avis » → lien court à envoyer après chaque mission).
- [x] Vérifier les **QR codes** (pointent vers `ze3d.fr`) — OK
- [x] **og:image dédiée par page (02/06)** : carte de marque carrée 1200×1200 (`og-ze3d-card.jpg`, depuis `Sources/ze3d-card.png`) pour accueil/à-propos/contact + rendus 509/502 (1200×630) pour prestations/réalisations. URL absolue. LIVE. *(Google rafraîchit les miniatures sous quelques jours.)*

## 📊 5. Analytics & mesure

- [x] **GA4 : décision 04/06/2026 → ABANDONNÉ pour l'instant.** Conflit avec les mentions légales §6 Cookies (« aucun outil d'analyse tiers… GA4 »). GA4 imposerait aussi un bandeau de consentement (non exempté CNIL). On reste sur **Google Search Console** (déjà en place, 0 cookie, 0 modif légale).
- [ ] (plus tard, SI besoin de voir le trafic) Outil de mesure **SANS cookie** (Plausible / Netlify Analytics) + reformulation légère des mentions légales. **Jamais GA4 standard.**

## 🧩 6. Enrichissement SEO / GEO *(quand les éléments existeront)*

- [ ] **Réseaux sociaux** créés → ajouter `sameAs` dans le JSON-LD (Layout.astro)
- [ ] **Premiers avis clients** vérifiables → ajouter `AggregateRating`
- [ ] (option) Chargement **non-bloquant des polices** (gain perf, déjà évalué sûr)
- [ ] Relancer `node scripts/generate-webp.mjs` à chaque ajout d'images dans `public/`

## 🛡️ 7. Sécurité & juridique

- [x] **Token GitHub SÉCURISÉ (02/06/2026)** : migré en **SSH** (clé ed25519 « Mac ») + **ancien token « Mac mini ZE3D » révoqué** sur GitHub. Plus aucun token en clair ; auth par clé SSH (trousseau). Vérifié OK après révocation.
- ℹ️ **RC Pro : ÉTAT DE FAIT, pas un chantier.** Manu a exploré à fond → aucun assureur ne propose de RC Pro pour cette activité (uniquement décennale, refusée). Position assumée et déclarée dans les CGV/mentions. Ne PAS remettre ce sujet sur la liste.
- ℹ️ **Revue juridique CGV : Manu a décidé de NE PAS la faire** (sauf nécessité absolue). CGV rédigées par ChatGPT. Risque résiduel concentré sur les clauses limitatives de responsabilité — à reconsidérer uniquement en cas de litige ou de gros contrat.

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
- [x] **Favicon** : monogramme (`Sources/favicon.png`, choix final 02/06) — favicon.ico (16/32/48) + favicon-32/16.png + apple-touch-icon (180) + icon-512 (PWA). LIVE sur ze3d.fr. Ancien favicon.svg supprimé.
- [x] **Signature mail** : nouvelle image fournie par Manu (`Signature mail ZE3D new.jpg`, 420×180), hébergée sous `sig-ze3d-ab24dbed.jpg`, 4 fichiers mis à jour (affichage **210×90**, aligné à gauche). Ancienne image conservée.
- [x] **PROD déployée le 02/06/2026** (refonte identité complète) — image signature `sig-ze3d-9f8c8305.jpg` LIVE sur ze3d.fr (vérifié HTTP 200).
- [x] **Signatures Ionos collées (02/06/2026)** : les 2 boîtes mises à jour (image cliquable → ze3d.fr, libellés en #3C5E7C). Testées OK.
- [x] **Typographie de marque** : style du logo (Nasalization, scaleX 0.6, tracking 0, MAJ) appliqué à toutes les mentions visibles « ZE3D » (classe `.brand-ze3d`) — nav, footer, corps, pages légales. 02/06/2026
- [x] **Couleur du site (CSS)** : bleu accent `#4A6580` → **`#3C5E7C`** (bleu du logo) partout + footer `#8FA6C0` → `#82AFD6`. Doré testé puis **retiré** (site en bleu uniquement, choix Manu). 02/06/2026
- [x] **QR codes** : régénérés en `#3C5E7C` (02/06/2026) — 5 × PNG (bleu) + SVG (noir/blanc) dans `Sources/QR codes/`. Pas sur le site (fichiers externes : impression, carte de visite…).

---

## 🎨 9. Refonte charte graphique (05/06/2026)

- [x] **Sources canoniques** : `Sources/Charte graphique/` (logotype, logotype FF, nom, phrase, LN, LNP, favicon, signature) = seule source de vérité.
- [x] **Assets site régénérés** (`scripts/rebuild-brand-assets.py`) : header `logo-ln.png`, footer logotype FF, splash (halo doux), favicon « ZE », `og-ze3d-card` (LNP), signature `sig-ze3d-886c4914.jpg`. Dimensions calées = **aucun changement visible** (hors favicon/og/splash, voulus).
- [x] **Ménage** sources/projet obsolètes + `Sources/` réorganisé + `CLAUDE_2.md` supprimé.
- [x] **Document charte graphique** (identité + site, 12 p., sommaire cliquable) : `Sources/Charte graphique/charte-graphique-ZE3D.html` → **PDF** `Charte graphique - ZE3D.pdf`. Fichier **local**. *(Règle : régénérer à chaque modif d'identité/site — voir MEMOIRE §20.)*
- [ ] **DÉPLOYER** la refonte (dev puis prod) — en attente du feu vert.
- [ ] 🔵 **Manu — après prod** : **réuploader le nouveau logo** sur la fiche Google Business.
- [ ] 🔵 **Manu — après prod** : **recoller les 2 signatures** dans Ionos (image `sig-ze3d-886c4914.jpg`).

### Notes de contexte
- **main = production**, **develop = test (ze3d-test)**. Ne jamais merger vers main sans validation.
- **Adresse** : siège déclaré = 47 rue Vivienne, 75002 Paris (domiciliation, pages légales) /
  activité = Perpignan 66000 (JSON-LD SEO local). Double affichage **volontaire**, ne pas « corriger ».
- Détails techniques complets dans `MEMOIRE_PROJET.md` (section 18 pour le SEO/GEO).
