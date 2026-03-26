import { generatedSidebars } from "./sidebars.js";

// Must pass array arguments!!!!
// Option: when true, use the page's markdown title (frontmatter `title` or inferred)
// as the sidebar item text instead of the raw filename.

export default {
  /* ... */
  title: "Phoenix Wiki",
  description: "Documentation for Phoenix Devt plugins",

  // [GITHUB PAGES PATCH BEGIN]
  base: '/phoenix-docs-backup/',
  // [GITHUB PAGES PATCH END]

  // Browser tab logo
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/favicon.png' }],
    ['link', { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    ['link', { rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png' }],
    ['link', { rel: 'manifest', href: '/site.webmanifest' }]
  ],

  themeConfig: {

    // Logo of navbar
    logo: "/favicon.ico",

    // footer
    footer: {
      message: 'Powered by <a href="https://vitepress.dev/" target="_blank" rel="noopener noreferrer">VitePress</a>',
      copyright: `Copyright © ${new Date().getFullYear()} Phoenix Development`,
    },

    // Custom sidebars
    sidebar: generatedSidebars,

    // social links
    socialLinks: [
      // You can add any icon from simple-icons (https://simpleicons.org/):
      { icon: 'discord', link: 'https://phoenixdevt.fr/discord' },
      { icon: 'spigotmc', link: 'https://phoenixdevt.fr/spigot' },
      // You can also add custom icons by passing SVG as string:
      {
        icon: {
          svg: '<svg role="img" viewBox="0 0 24 24" xmlns="polymary.png"><title>Dribbble</title><path d="M12...6.38z"/></svg>'
        },
        link: '...',
        // You can include a custom label for accessibility too (optional but recommended):
        ariaLabel: 'cool link'
      }
    ],

    search: {
     provider: 'local'
    },

    // edit link
    editLink: {
      pattern: 'https://gitlab.com/phoenix-dvpmt/phoenix-docs/-/tree/master/:path'
    },

    // navigator bar links
    nav: [
      // { text: "Home", link: "/" },
      { text: "MMOItems", link: "/mmoitems/" },
      { text: "MMOCore", link: "/mmocore/" },
      { text: "MMOInventory", link: "/mmoinventory/" },
      { text: "MMOProfiles", link: "/mmoprofiles/" },
      { text: "MythicLib", link: "/mythiclib/" },
      {
        text: 'Other',
        items: [
          { text: 'BountyHunters', link: '/bounty-hunters/' },
          { text: 'Contracts', link: '/contracts/' },
        ]
      }
    ],
  },
};
