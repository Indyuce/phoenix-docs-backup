# 🛡️ Guilds

Guilds (also called factions, kingdoms...) are a common feature for RPG servers. They allow players to team up, share resources, and work together toward common goals.

MMOCore does not provide a guild system, but is compatible with the following guild plugins:

- Any plugin supported by [FactionsBridge](https://www.spigotmc.org/resources/factionsbridge.89716/) (>15 plugins)
- [UltimateClans V6](https://polymart.org/resource/ultimate-clans-v6.1162)
- [Guilds](https://www.spigotmc.org/resources/guilds-30-sale.66176/)
- [KingdomsX](https://www.spigotmc.org/resources/kingdomsx.77670/)

Note that you need FactionsBridge installed when running MMOCore with any guild plugin supported by FactionsBridge.

## Choosing your guild plugin

Go to `MMOCore/config.yml` and set `guild-plugin` to whatever plugin you want to use. Make sure you restart your server when editing this option.

```yml
# Edit the plugin handling guilds here.
# Supported values (just copy and paste):
# - FACTIONSBRIDGE (and any supported Factions/Guild plugin)
# - MMOCORE (Default built-in guild system)
# - NONE (Used to fully disable guilds)
# - GUILDS (by Glare)
# - ULTIMATE_CLANS
guild-plugin: MMOCORE
```

Using any guild plugin that is not MMOCore will disable all guild features from MMOCore, including the guild registry and the `/guild` command.

## MMOCore Guilds

Note that MMOCore does technically have a dummy guild system implemented, though it has little to no features, and we do not have any plans of pursuing its development.