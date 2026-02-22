---
order: 7
---

# 🎨 GUI Syntax

MythicLib provides unifixed syntax for chest UI inventories. This includes MMOItems crafting stations, the MMOProfiles profile selection UI, and all MMOCore UIs including player stats, waypoints, party & friends, class selection, etc.

GUI plugin configs are located inside the `gui` or `language/gui` folder.

In this tutorial, we will be focusing on the MMOCore attributes menu.

::: details Original Config
```yml

# GUI display name
name: Player Attributes

# Number of slots in your inventory. Must be
# between 9 and 54 and must be a multiple of 9.
slots: 27

items:
  reallocate:
    slots: [26]
    function: reallocation
    item: CAULDRON
    name: '&aReallocate Skill Points'
    lore:
    - ''
    - 'You have spent a total of &6{total}&7 skill points.'
    - '&7Right click to reallocate them.'
    - ''
    - '&eCosts 1 attribute reallocation point.'
    - '&e◆ Attribute Reallocation Points: &6{points}'
  str:
    slots: [11]
    function: attribute_strength
    name: '&a{name}'
    item: GOLDEN_APPLE
    lore: # {buffs} returns amount of buffs
    - ''
    - '&7Points Spent: &6{spent}&7/&6{max}'
    - '&7Current {name}: &6&l{current}'
    - ''
    - '&8When Leveled Up:'
    - '&7  +{buff_weapon_damage}% Weapon Damage (&a+{total_weapon_damage}%&7)'
    - '&7  +{buff_max_health} Max Health (&a+{total_max_health}&7)'
    - ''
    - '&eClick to level up for 1 attribute point.'
    - '&e◆ Current Attribute Points: {attribute_points}'
  dex:
    slots: [13]
    function: attribute_dexterity
    name: '&a{name}'
    item: LEATHER_BOOTS
    hide-flags: true
    lore:
    - ''
    - '&7Points Spent: &6{spent}&7/&6{max}'
    - '&7Current {name}: &6&l{current}'
    - ''
    - '&8When Leveled Up:'
    - '&7  +{buff_physical_damage}% Physical Damage (&a+{total_physical_damage}%&7)'
    - '&7  +{buff_projectile_damage}% Projectile Damage (&a+{total_projectile_damage}%&7)'
    - '&7  +{buff_attack_speed} Attack Speed (&a+{total_attack_speed}&7)'
    - ''
    - '&eClick to level up for 1 attribute point.'
    - '&e◆ Current Attribute Points: {attribute_points}'
  int:
    slots: [15]
    function: attribute_intelligence
    name: '&a{name}'
    item: BOOK
    lore:
    - ''
    - '&7Points Spent: &6{spent}&7/&6{max}'
    - '&7Current {name}: &6&l{current}'
    - ''
    - '&8When Leveled Up:'
    - '&7  +{buff_magic_damage}% Magic Damage (&a+{total_magic_damage}%&7)'
    - '&7  +{buff_cooldown_reduction}% Cooldown Reduction (&a+{total_cooldown_reduction}%&7)'
    - ''
    - '&eClick to level up for 1 attribute point.'
    - '&e◆ Current Attribute Points: {attribute_points}'
```
:::

## General Options

You can edit the general GUI settings like its name and slots.

```yml
name: 'Player Attributes'
slots: 27
```

Notice how the config sections that fall under the `items` section share very similar properties: `name` (the item display name), `lore` (the item description/lore), `item` (the item material), `slots` (where the item is placed in the inventory, it can be a list) and `function` (what the item does). These can (and should) all be edited to your needs.

### Editing Item Slots

If you want to have your item displayed on multiple slots, use the following syntax:

```yml
slots: [1, 2, 3, 4]
#slots: 1 # This won't work
#slot: 1  # This won't work
```

## Item Functions

`function` tells MythicLib what the item does when clicked, and what placeholders to apply in the item lore. A function that works inside the MMOCore attribute menu will not work inside the MMOProfiles profile selection menu. Each GUI comes with its own set of built-in item functions.

In general, you don't really want to change it, unless you are adding a generic item function like a _Go Back_ or _Close_ button. You can edit the item visuals as much as you want, but changing the function will change the item behavior and the placeholders that are applied to it, so make sure you know what you are doing before editing it.

In the following example, the item uses a builtin `attribute_<attribute_name>` function that applies placeholders and click handlers related to the MMOCore player attribute.
```yml
# [...]
items:
# [...]
  item_strength:
    slots: [15]
    function: attribute_strength
    name: '&a{name}'
    item: BOOK
    lore:
      #.....
      - '&8When Leveled Up:'
      - '&7  +{buff_weapon_damage}% Weapon Damage (&a+{total_weapon_damage}%&7)'
      - '&7  +{buff_max_health} Max Health (&a+{total_max_health}&7)'
      #.....
```

## Lore Placeholders

Choosing the item function unlocks specific placeholders that you can use inside the item name and lore. For instance, the `attribute_<attribute_name>` function inside the MMOCore attribute menu unlocks the following placeholders:

| Placeholder | Description |
|-------------|-------------|
| `{spent}` | Amount of attribute points spent by the player in that attribute |
| `{max}` | Maximum amount of attribute points you may spend in that attribute |
| `{name}` | Attribute name |
| `{current}` | The current attribute of the player. Takes into account modifiers from MMOItems and other plugins. |
| `{buff_<stat>}` | Buff granted for each point spent in that attribute. |
| `{total_<stat>}` | Total buff granted by all the points spent in that attribute (the product of `{spent}` and `{buff_xxx}`). |

## Clickable Items

If you don't specify any function for an item, you can provide a [MythicLib script](../scripts/intro.md) to be executed when the item is clicked, using the following syntax:

```yml
items:
  log_out:
    slots: [ 44 ]
    item: BELL
    name: "&cLog Out"
    script:
      - command{format="kick %player_name% You successfully logged out"}
```

Instead of a list of mechanics, you can also provide the name of a MythicLib script.

```yml
items:
  log_out:
    # [...]
    script: my_custom_kick_mythiclib_script
```
