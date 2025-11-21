## Keep your items up-to-date using the RevID stat

When you increase this number in the editor, all the copies of this item in the world will update to match the template:![image](uploads/a22041c8f8ae7bdfb4851b0e8ef25750/image.png)

When 'updating' an item, the goal is essentially to regenerate it, as if it was freshly obtained with the `/mi give` command, having the latest lore format and the same stats as the template:![image](uploads/dc4c308365f5bdd62857204d8e3b455a/image.png)

## Advanced Configuration

There are a lot of options for this revision system, which you can tweak in the `item-revision` section of the config.

```
item-revision:
  keep-data:
    display-name: true
    enchantments: true
    soulbound: true
    gems: true
    upgrades: true
    lore: false
    kept-lore-prefix: '&7'
    external-sh: true
    reroll: false
    modifications: true
    skins: true
    tier: true

  drop-extra-gems: true
```

Some options have more complicated mechanics, but the rest of these options are self-explanatory.

### Reroll RNG Stats `reroll`

This option has some very complicated behaviour, stats may reroll even if you specified false, and this is desirable. It is important to understand that all numeric stats are RNG — even if you did not specify a spread, they just have 100% chance of the same value.

Suppose this is _enabled_, then all of the numeric stats of the item will be rerolled.

Suppose this is _disabled_, then each numeric stat will calculate the probability of it being generated again under the current mean and spread settings, if it is too rare then it will update/reroll even though this option was disabled:

1. If the new value has a spread of 0 and has changed, the old value will be lost as it would be 0% of generating.
2. If the value was removed entirely from the item, the old value will be lost.
3. If the spread of the value has changed such that the old value is exceedingly rare (1 in 4200) then the old value will be lost.
4. If the max spread value has changed, and the old value is outside this range, the old value will be constrained to the max spread.

As you can see, RNG will be rerolled if this item would be unobtainable under the new conditions, which is healthy game design.

### Keep Enchantments `enchantments`

The old enchantments of the item will be compared to the enchantments in the template to decide if the enchantment will be kept or updated:

1. Any old enchantment that is worse than that of the template will update to the better value
2. If an old enchantment is better than that of the template, it will be kept as long as it is obtainable in vanilla minecraft.
3. If the template has the `disable-enchanting` and `disable-repairing` stats enabled, no old enchantments will be kept _even if this option is enabled_, all enchantments will be updated to match the template.

As you can see, the aim is that players who enchant their items do not lose their enchantments, but if the item is updated in the template to have even better enchantments, these players will get the better enchantments. Essentially, attempts to remember the enchantments the player put in the item, and apply them again, if the player could still apply them.

### Keep Gemstones `gemstones`, `drop-extra-gems`

Its important to note the `drop-extra-gems` option, if any gemstones would be deleted due to the RevID updater, setting this option to true will cause them to be given back to the player / dropped nearby if their inventory is full. This option is global to all item revision operations (see next section on more RevID system applications).

If this option is _disabled_, all old gems in the item will be deleted (\~ or dropped if the `drop-extra-gems` option is enabled).

If this option is _enabled_, it is still possible for old gems to be deleted:

1. If the template had its gem sockets removed or decreased in amount, gems that dont fit will be deleted
2. If the color of the gem sockets changed, gems that do not fit anymore will be deleted

### Keep Name `display-name`

If this is enabled, then the old name of the item will be kept, regardless of what the template currently has.

### Keep Soulbound `soulbound`

If the old item is soulbound, this soulbound will be kept.

### Keep Upgrades `upgrades`

The upgrade level of the old item will be kept, however this will fail if the item template has no upgrade template anymore. If the max upgrades of the item were decreased, the extra upgrade levels will be lost.

### Keep Lore `lore`, `kept-lore-prefix`

From the old item, all the lines of lore that begin with the <span dir="">`kept-lore-prefix`</span> (commonly a color code) will be kept. Be warned that this can cause duplicate lore if the template has any lore that begins with this prefix, it will be kept every time the item is updated.

### Keep External SH `external-sh`

External stat history data is added by third-party plugins to modify stats of the item. Enabling this will keep all this data, with the exception of enchantments.

### Keep Modifications `modifications`

All item modifiers will be kept if this is enabled, even if they cannot be obtained anymore, and even if the modifier weights changed.

### Keep Skins `skins`

If this is enabled, changes made by a _skin-type_ item will be kept.

### Keep Tier `tier`

If the old item has a tier, this tier will be preserved, even if the template has now a different tier.

## Other Applications of the RevID system

### Updating gemstones inside items

The RevID system supports updating gemstones while they are inserted in items. This does not happen automatically when increasing the RevID of the gemstone template, you must increase the parent item's RevID and have the _keep gemstones_ option enabled.

You can use the `item-revision.keep-gem-data` field to specify the RevID options of gemstones updated this way:
```
item-revision:
  keep-gem-data:
    display-name: true
    enchantments: true
    ...
```

## Third Party Plugin Compatibilities

### Keep Advanced Enchantments `advanced-enchantments`

All of the advanced enchantments in the item will be kept.

### Update PhatLoots loot as it generates

PhatLoots does not have special support for MMOItems, such that after a few months, your MMOItem loot drops can become quite unupdated! Specify in MMOItems' config.yml in the section `item-revision.phat-loots` the revision options to update these items as they are generated:

```
item-revision:
  phat-loots:
    display-name: true
    enchantments: true
    ...
```


----


TODO include info about item updater

- - -
Once items are generated using drop tables or the give command, they become independant of the /item config. Therefore the only way to directly update items in the player's inventories is to use the **Item Updater**. You can either directly update the item you are holding using **/updateitem**, or enable the item updater for a specific item using `/updateitem <type> <id>`.

### Updating physical items
Once the item updater is enabled for a specific item, every physical instance of that item is considered _outdated_ and will be updated. An outdated item can only be updated **once** (performance save) when enabling the item updater, unless you apply further changes to the item. Every change you apply in the item edition GUI will make physical item instances _outdated_ again till they are updated.

MMOItems updates every item in the players inventories whenever they log in. Furthermore any item clicked in a non-creative inventory undergoes an update check.

### Enabling the updater for every item
If you do not want to worry about players having outdated items here and there on your server, you might want to enable the item updater for every item in the plugin. **This is possible however strongly not recommended.**\
The item updater was designed to hot-nerf items in players' inventories once they have been generated. It is not designed to mass-update every item on your server. The more items you have, the higher the performance the plugin will need in order to keep them updated.

The item updater is **100% useless** for items which have not been changed after they are generated. In order to save performance, MI first checks if a physical item has some non-applied item change, and then updates the item if it is considered outdated. Enabling the item updater for all of your items generates useless update checks.

You can manually enable the item updater for every item in your server using the following command: `/mi update apply 2 2`. This loops through every item in your config files and registers them in the item updater list.