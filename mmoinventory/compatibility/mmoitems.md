---
sidebar_position: 1
---

# ⚔️ MMOItems

<Warning title="Important">
This page is subject to change in the future as MMOInventory 2 introduced multiple custom inventories (as well as an option to simultaneously use the vanilla player inventory). This page will be updated when MMOInventory 2 is released.
</Warning>

## Configurating MMOInventory

This is the default `MMOInventory/items.yml` config setup for MMOInventory when used with MMOItems. This config file registers new slots for accessories such as ring, bracelet and artifact slots. Using the `mmoitemstype` slot restriction you can restrict this slot to a specific MMOItems item type.

```yml title="MMOInventory/items.yml"
# Vanilla Slots
HELMET:
    type: helmet
    material: DIAMOND_HOE
    durability: 1
    name: '&6Helmet Slot'
    slot: 4
    lore:
    - Drag & drop an item to equip it.
CHESTPLATE:
    type: chestplate
    material: DIAMOND_HOE
    durability: 2
    name: '&6Chestplate Slot'
    slot: 13
    lore:
    - Drag & drop an item to equip it.
LEGGINGS:
    type: leggings
    material: DIAMOND_HOE
    durability: 3
    name: '&6Leggings Slot'
    slot: 22
    lore:
    - Drag & drop an item to equip it.
BOOTS:
    type: boots
    material: DIAMOND_HOE
    durability: 4
    name: '&6Boots Slot'
    slot: 31
    lore:
    - Drag & drop an item to equip it.
OFF_HAND:
    type: off_hand
    material: DIAMOND_HOE
    durability: 14
    name: '&6Off Hand Slot'
    slot: 12
    lore:
    - Drag & drop an item to equip it.
 
# Ring slots
RIGHT_RING:
    type: accessory
    material: DIAMOND_HOE
    durability: 7
    name: '&6Right Ring Slot'
    slot: 25
    restrictions:
    - 'mmoitemstype{type=RING}'
    lore:
    - Drag & drop an item to equip it.
LEFT_RING:
    type: accessory
    material: DIAMOND_HOE
    durability: 8
    name: '&6Left Ring Slot'
    slot: 34
    restrictions:
    - 'mmoitemstype{type=RING}'
    lore:
    - Drag & drop an item to equip it.
 
# Extra accessories
AMULET:
    type: accessory
    material: DIAMOND_HOE
    durability: 5
    name: '&6Amulet Slot'
    slot: 7
    restrictions:
    - 'mmoitemstype{type=AMULET}'
    lore:
    - Drag & drop an item to equip it.
BRACELET:
    type: accessory
    material: DIAMOND_HOE
    durability: 6
    name: '&6Bracelet Slot'
    slot: 16
    restrictions:
    - 'mmoitemstype{type=BRACELET}'
    lore:
    - Drag & drop an item to equip it.
GLOVES:
    type: accessory
    material: DIAMOND_HOE
    durability: 9
    name: '&6Gloves Slot'
    slot: 1
    restrictions:
    - 'mmoitemstype{type=GLOVES}'
    lore:
    - Drag & drop an item to equip it.
 
# Artifact slots
ARTIFACT_1:
    type: accessory
    material: DIAMOND_HOE
    durability: 10
    name: '&6Artifact Slot I'
    slot: 10
    restrictions:
    - 'mmoitemstype{type=ARTIFACT}'
    - 'unique{enabled=true}'
    lore:
    - Drag & drop an item to equip it.
ARTIFACT_2:
    type: accessory
    material: DIAMOND_HOE
    durability: 11
    name: '&6Artifact Slot II'
    slot: 19
    restrictions:
    - 'mmoitemstype{type=ARTIFACT}'
    - 'unique{enabled=true}'
    lore:
    - Drag & drop an item to equip it.
```

## Configurating MMOItems

The previous config file snippet only registers custom slots inside the custom RPG inventory of MMOInventory. For that code to work, you will also need to register the corresponding item types in the MMOItems registry, which you can do by adding this code snippet to your `MMOItems/item-types.yml` config:

```yml title="MMOItems/item-types.yml"
RING:
    display: DIAMOND
    name: 'Artifact'
    parent: 'ACCESSORY'
    unident-item:
        name: '&f#prefix#Unidentified Artifact'
        lore:
        - '&7This item is unidentified. I must'
        - '&7find a way to identify it!'
        - '{tier}'
        - '{tier}&8Item Info:'
        - '{range}&8- &7Lvl Range: &e#range#'
        - '{tier}&8- &7Item Tier: #prefix##tier#'
AMULET:
    display: DIAMOND
    name: 'Amulet'
    parent: 'ACCESSORY'
    unident-item:
        name: '&f#prefix#Unidentified Amulet'
        lore:
        - '&7This item is unidentified. I must'
        - '&7find a way to identify it!'
        - '{tier}'
        - '{tier}&8Item Info:'
        - '{range}&8- &7Lvl Range: &e#range#'
        - '{tier}&8- &7Item Tier: #prefix##tier#'
BRACELET:
    display: DIAMOND
    name: 'Bracelet'
    parent: 'ACCESSORY'
    unident-item:
        name: '&f#prefix#Unidentified Bracelet'
        lore:
        - '&7This item is unidentified. I must'
        - '&7find a way to identify it!'
        - '{tier}'
        - '{tier}&8Item Info:'
        - '{range}&8- &7Lvl Range: &e#range#'
        - '{tier}&8- &7Item Tier: #prefix##tier#'
GLOVES:
    display: DIAMOND
    name: 'Gloves'
    parent: 'ACCESSORY'
    unident-item:
        name: '&f#prefix#Unidentified Gloves'
        lore:
        - '&7This item is unidentified. I must'
        - '&7find a way to identify it!'
        - '{tier}'
        - '{tier}&8Item Info:'
        - '{range}&8- &7Lvl Range: &e#range#'
        - '{tier}&8- &7Item Tier: #prefix##tier#'
ARTIFACT:
    display: DIAMOND
    name: 'Artifact'
    parent: 'ACCESSORY'
    unident-item:
        name: '&f#prefix#Unidentified Artifact'
        lore:
        - '&7This item is unidentified. I must'
        - '&7find a way to identify it!'
        - '{tier}'
        - '{tier}&8Item Info:'
        - '{range}&8- &7Lvl Range: &e#range#'
        - '{tier}&8- &7Item Tier: #prefix##tier#'
```

### Important Note

Make sure the corresponding item type from `MMOItems/item-types.yml` has its subtype/parent set to `ACCESSORY`, which is **MANDATORY** to have MMOItems register stats of items placed inside the custom inventory GUI!! In other words, you can equip an item using the MMOInventory GUI and not get any stats from it. To avoid that, you need to make sure that the MI item types have their parent type set to the Accessory item type, otherwise MMOItems will just ignore these items.