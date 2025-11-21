Upgrading recipes are a specific type of station recipes. They allow any player to upgrade a specific items, using ingredients. These recipes do also support recipe conditions and other recipe options like `hide-when-locked`. You should consider learning about [crafting stations](Crafting-Stations) before reading how to setup upgrading recipes.

Upgrading recipes cannot have a crafting time yet.

![](https://i.imgur.com/F1ugbnJ.png)

## Recipe Example

```
recipes:
    steel-sword-upgrade:
        item: # Use 'item' instead of 'output' to switch to an upgrading recipe
            type: SWORD
            id: STEEL_SWORD
        conditions:
        - 'level{level=5}'
        ingredients:
        - 'mmoitem{type=MATERIAL,id=STEEL_INGOT,amount=4}'
```

This upgrade recipe allows players to upgrade the item `Steel Sword`. Upgrading recipes **NOT** support crafting time, therefore they must all be instant, as if you used a consumable. In order to use this recipe, the player must be at least level 5, and must have 4 steel ingots in his inventory.

The major syntax difference with a crafting recipe, is that you need to use `item` instead of `output` (see first line of recipe config).\
The player must have, when using the recipe, the item they are trying to upgrade(it's animplicit ingredient, although not shown in the ingredient list), otherwise they will be prompted an error message.