**Make sure you read [this paragraph](Item Creation#how-items-work-very-important) first. The MMOItems item generation system is pretty complex and needs some time to be fully understood.**

Item templates are the most fundamental tool to generate random items. They are defined by a list of **default item stats** which the resulting item will have no matter what, and a list of **item modifiers** which will be randomly picked and applied to the resulting item to impact its rarity.

```
LONG_SWORD:
    
    # Basic template options
    option:
        tiered: true
        level-item: true
        roll-modifier-check-order: false
        capacity:
            base: 10
            scale: 3

    # Base item data
    base:
        material: IRON_SWORD
        name: '&fLong Sword'
        attack-speed: 1.6
        attack-damage:
            base: 6
            scale: 1.2
        required-level:
            base: 0
            scale: 1

    # Template modifiers
    modifiers: 
        sharp:
            chance: 0.3
            prefix: '&fSharp'
            stats:
                attack-damage: 3
                lore:
                - '&7Much sharper!'
```
The `base` config section corresponds to the base item stats. For example, the base item is an iron sword which name is `Long Sword`. The default attack speed is 1.6 and the weapon has 6 Atk damage increased by 1.5 point for every item level.

The `option` config section is used to configure a few additional options for your template. See next paragraph for more information.

Item generation templates can be found under the `/MMOItems/items` folder. You may add as many YML configs as you want in that folder to sort your templates.

## Item Template Options
A small list of extra options for your item template. Except capacity set them to `true` to enable them

| Template Option           | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| roll-modifier-check-order | Scrambles the item modifiers list on item generation    |
| tiered                    | A random tier will be picked for your item if none is specified when generating the item.  This accounts for the `/mi generate` command, but also for station crafting recipes! |
| level-item                | A random item level will be picked for your item if none is specified when generating the item. |
| capacity                | `capacity` can be used to impose a formula for modifier capacity to your item without having to use an item tier. It overrides both the default modifier capacity formula as well as the formula provided by the tier of the generated item. |