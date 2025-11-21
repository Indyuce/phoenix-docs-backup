Blocks or monsters may sometimes **drop unidentified items**. These items have their data completely hidden and will require the player to identify it in order to be used. The only actual info players have on unidentified items is the item material, type, item level range (more or less 3 levels) and tier.

A special property is available to consumables to have them able to identify items. If a consumable has the _Can Identify_ option toggled on, they can be drag and dropped onto an item to identify them. Item identification is confirmed by a chat message & sound effect.

![](https://i.imgur.com/JU1MI08.gif)

## Commands

The following commands identifies/unidentifies the item that you are holding in hand.

```
/mi item identify
/mi item unidentify
```

## Translation
You can change the way unidentified items look inside the `item-types.yml` config file. Every item type has a different template for unidentified items:
```yaml
DAGGER:
    # ...
    unident-item:
        name: '&f#prefix#Unidentified Dagger'
        lore:
        - '&7This item is unidentified. I must'
        - '&7find a way to identify it!'
        - '{tier}'
        - '{tier}&8Item Info:'
        - '{range}&8- &7Lvl Range: &e#range#'
        - '{tier}&8- &7Item Tier: #prefix##tier#'
```