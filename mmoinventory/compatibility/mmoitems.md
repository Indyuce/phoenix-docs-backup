---
order: 1
---

# ⚔️ MMOItems

This page explains how to configure MMOInventory to work with [MMOItems](https://www.spigotmc.org/resources/39267/).

## Configurating MMOInventory

The default custom inventory that comes with MMOInventory contains vanilla armor and hand slots as well as extra accessory slots such as rings, amulet, bracelet, gloves and artifact slots. These _accessory slots_ are configured to only accept MMOItems items of specific types.

For instance, the following code snippet shows how to configure the _Left Ring_ and _Right Ring_ slots to only accept MMOItems items of type `RING`.
```yml
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
```

## Configurating MMOItems

The code snippet from previous section only registers custom slots inside the custom inventory of MMOInventory. For that code to work, you will also need to register the corresponding item types in the MMOItems registry. MMOItems comes with the corresponding _accessory item types_ already registered, so you do not need to create them from scratch.

::: warning
All MMOItems item types that correspond to custom accessory slots (rings, bracelets, amulets...) in MMOInventory **MUST** have their parent type set to `ACCESSORY`. This is mandatory for MMOItems to properly register stats of items placed inside the custom inventory GUI.
:::

For example, the following code snippet registers the `RING` item type for the two _Left Ring_ and _Right Ring_ slots we configured in the previous section.
```yml
RING:
    display: EMERALD
    name: 'Artifact'
    parent: 'ACCESSORY' # Parent type set to ACCESSORY
    unident-item:
        name: '&f#prefix#Unidentified Ring'
        lore:
        - '&7This item is unidentified. I must'
        - '&7find a way to identify it!'
        - '{tier}'
        - '{tier}&8Item Info:'
        - '{range}&8- &7Lvl Range: &e#range#'
        - '{tier}&8- &7Item Tier: #prefix##tier#'

```

### Important Note

