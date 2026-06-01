// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  // Domaine canonique : sert aux URLs <link rel="canonical"> absolues
  // et à la génération du sitemap.
  site: 'https://ze3d.fr',

  integrations: [
    sitemap({
      // On exclut du sitemap les pages mises en noindex
      // (pages légales + 404) — inutile de les proposer à l'indexation.
      filter: (page) =>
        !page.includes('/cgv') &&
        !page.includes('/mentions-legales') &&
        !page.includes('/404'),
    }),
  ],
});
