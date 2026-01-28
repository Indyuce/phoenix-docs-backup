---
order: 5
---

# 🦾 Compatibility

The main feature of this plugin is to enable other plugins to use its API and also have profile-based data. A plugin that supports MMOProfiles will have its data saved for the profile and not for the player, and changing profile will be as if you logged in with a different account. 

## MMO Plugins

The full MMO plugin suite ([MMOCore](../../mmocore/), [MMOInventory](../../mmoinventory/), [MMOItems](../../mmoitems/), [MythicLib](../../mythiclib/)) **FULLY SUPPORTS** profile-based data storage.

## Vault Economy

MMOProfiles saves the player's Vault balance. This way, any Vault-based economy plugin is supported by MMOProfiles.

## CoreTools <Badge type="tip" text="new" />

CoreTools ([SpigotMC](https://www.spigotmc.org/resources/coretools.125126) - [Wiki](https://gitlab.com/Tanerx/CoreTools/-/wikis/home)) fully supports profile-based data storage. 

## BeautyQuests <Badge type="tip" text="new" />

[BeautyQuests](https://www.spigotmc.org/resources/beautyquests.39255) is known to support MMOProfiles profiles, enabling for profile-specific quest progression. To enable compatibility with BeautyQuests, download the following plugins.
- [AccountsHook](https://www.spigotmc.org/resources/accountshook.59491/) which exposes the BeautyQuests profile API to other plugins.
- [AccountsHook-MMOProfiles](https://github.com/SkytAsul/AccountsHook-MMOProfiles/releases) which implements support for MMOProfiles in AccountsHook.

In the future we will shade the AccountsHook-MMOProfiles plugin hook directly into MMOProfiles to make it easier to install and use.

## BetonQuest

BetonQuest are on their way to supporting MMOProfiles natively. The plugin already has a profile system ready for players to have multiple profiles, so MMOProfiles integration is on its way!