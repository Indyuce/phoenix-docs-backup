This section lists all **BUILT-IN** compatibilities implemented into MMOItems.

## WorldGuard Flags
MythicLib implements new flags that work for both MMOCore and MMOItems. See the [full list here](https://gitlab.com/phoenix-dvpmt/mythiclib/-/wikis/Plugin-Compatibility#worldguard).

Like any other plugin, [**WorldGuard**](http://www.enginehub.org/worldguard) should be detected automatically by MMOItems when the server is booting. You can check the console when the plugin is loading to make sure it was detected.

## Custom Enchantments plugins
MMOItems is compatible with EcoEnchants, MythicEnchants and AdvancedEnchants(Not recommended). This means it is MOST LIKELY not natively compatible with other enchantment plugins tho well designed enchantment plugins should have no issues (e.g EcoEnchants). More information over [this wiki page](Enchant Plugins).

## RPG Core Plugins
MMOItems will automatically hook onto any detected RPG plugin. MMOItems can read the player level in order to apply the item level restriction, the player class for the class restriction, and the player mana & stamina/power for ability & item resource costs.\
**Supported Core Plugins:**
* **MMOCore** [Polymart](https://polymart.org/product/3412/mmocore) / [Spigot](https://www.spigotmc.org/resources/70575/)
* [**Heroes**](https://www.spigotmc.org/resources/24734/)
* [**SkillAPI**](https://www.spigotmc.org/resources/28029/)
* [**ProSkillAPI**](https://www.spigotmc.org/resources/91913/)
* [**RPGPlayerLeveling**](https://www.spigotmc.org/resources/11096/)
* [**BattleLevels**](https://www.spigotmc.org/resources/battlelevels.2218/)
* [**Skills**](https://www.spigotmc.org/resources/8981/)
* [**SkillsPro**](https://www.spigotmc.org/resources/skills-pro.8981/)
* [**AureliumSkills**](https://www.spigotmc.org/resources/81069/)
* [**mcMMO**](https://www.spigotmc.org/resources/official-mcmmo.64348/)
* [**McRPG**](https://www.spigotmc.org/resources/mcrpg.63020/)

If you need a basic mana system but don't need all that RPG stuff from other core plugins, you can just use the official [MMOItems Mana & Stamina addon](https://github.com/mmopluginteam/mmoitems-mana) available on GitHub for download.

**The 'Max Mana' item option ONLY works with MMOCore, Heroes & the MMOItems mana addon. The only way to have items give extra maximum mana is to use one of these plugins.**

## AureliumSkills
MMOItems introduces a new stat to give the player more skills as well as item restrictions which prevent players from using specific items unless they have at least X levels in a skill. In order to have these stats display in the item lore, add this to your `stats.yml` config file:
```
additional-wisdom: '&3 &7■ Extra Wisdom: &f{value}'
additional-health: '&3 &7■ Extra Health: &f{value}'
additional-regeneration: '&3 &7■ Extra Regeneration: &f{value}'
additional-luck: '&3 &7■ Extra Luck: &f{value}'
additional-toughness: '&3 &7■ Extra Toughness: &f{value}'
additional-strength: '&3 &7■ Extra Strength: &f{value}'
additional-crit-damage: '&3 &7■ Extra Crit Damage: &f{value}'
additional-crit-chance: '&3 &7■ Extra Crit Chance: &f{value}'
required-farming: '&eRequires {value} in Farming'
required-foraging: '&eRequires {value} in Foraging'
required-mining: '&eRequires {value} in Mining'
required-fishing: '&eRequires {value} in Fishing'
required-excavation: '&eRequires {value} in Excavation'
required-archery: '&eRequires {value} in Archery'
required-defense: '&eRequires {value} in Defense'
required-fighting: '&eRequires {value} in Fighting'
required-endurance: '&eRequires {value} in Endurance'
required-agility: '&eRequires {value} in Agility'
required-alchemy: '&eRequires {value} in Alchemy'
required-enchanting: '&eRequires {value} in Enchanting'
required-sorcery: '&eRequires {value} in Sorcery'
required-healing: '&eRequires {value} in Healing'
required-forging: '&eRequires {value} in Forging'
```
And then this to your `lore-format.yml`:
```
  - '#additional-wisdom#'
  - '#additional-health#'
  - '#additional-regeneration#'
  - '#additional-luck#'
  - '#additional-toughness#'
  - '#additional-strength#'
  - '#additional-crit-chance#'
  - '#additional-crit-damage#'
  - '#required-farming#'
  - '#required-foraging#'
  - '#required-mining#'
  - '#required-fishing#'
  - '#required-excavation#'
  - '#required-archery#'
  - '#required-defense#'
  - '#required-fighting#'
  - '#required-endurance#'
  - '#required-agility#'
  - '#required-alchemy#'
  - '#required-enchanting#'
  - '#required-sorcery#'
  - '#required-healing#'
  - '#required-forging#'
  - '#required-forging#'
```

## MythicMobs
MMOItems lets your mythic mobs drop items from MI. Please refer to [this wiki page](Item-Drop-Tables).

## PlaceholderAPI
PAPI placeholders let you retrieve player statistics. To get some stat value, use `%mmoitems_stat_[stat_name]%` e.g `%mmoitems_stat_critical_strike_chance%` or `%mmoitems_stat_defense_percent%`.\
You may also use PlaceholderAPI to retrieve the durability of item held by the player: more info on [this wiki page](Custom%20Durability#durability-placeholders).

## RPGInventory
MMOItems supports [**RPGInventory**](https://www.spigotmc.org/resources/12498/): players can equip items from MMOItems in their custom inventory and benefit from their stats. However since RPGInventory does not support item attribute modifiers, stats based on vanilla attribute modifiers like attack speed, max health & movement speed won't apply on non-armor/hand item slots (i.e extra slots like accessory slots). Any other item effect will work fine.

MMOInventory however works flawlessly with MMOItems.

## BossShopPro
MMOItems adds a special type of reward to BossShopPro. This reward type can be used to give players an item when they click an item. Here is the format you need to use in order to setup an MMOItem reward type:
```
RewardType: MMOITEM
Reward:
- <ITEM_TYPE>.<ITEM_ID>
- <ITEM_TYPE>.<ITEM_ID>
- etc.
```

## MythicMobs
You can add items from MI to MythicMobs drop tables: more info on [this page](Item%20Drop%20Tables#adding-mmoitems-to-mythicmobs-drop-tables).