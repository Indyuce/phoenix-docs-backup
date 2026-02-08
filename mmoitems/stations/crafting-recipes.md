---
order: 2
---

# 🥘 Crafting Recipes

Crafting stations can have an unlimited number of crafting recipes. Every recipe has its own configuration subsection under the ``recipes`` config section. The string key that you will use for the subsection name is only used internally by MMOItems, so you can use anything as long as it is unique. It should be something like `<item_type>_<item_id>_recipe`.

For this guide, we will be creating a recipe for the _Steel Sword_ item, with the following requirements

* the player to be at least level 5
* the player needs a specific permission to use the recipe
* the recipe should take 1 stick and a few steel ingots


## Recipe Output

This is where you define what item the player will be given when using the recipe. The recipe output is placed under the output `subsection`. As usual, you need to provide the item type and ID. Use the following syntax to set the recipe output to a MMOItems item.

```yaml
# crafting-stations/cs_example.yml

recipes:
    steel-sword:
        output: 'mmoitems{type=SWORD,id=STEEL_SWORD,amount=1} # Recipe output
```

The `amount` field is optional, MMOItems will use 1 if you do not provide any.

Here is a table indicating all the possible recipe outputs that you can use.

| Output Type | Format | Comments |
|-------------|--------|----------|
| Vanilla Item | `vanilla{type=DIAMOND_HELMET}` | A vanilla item |
| MMOItem | `mmoitem{type=SWORD,id=KATANA,level=7-9}` | You may define a range for the required item level |
| MythicMobs/Crucible | `mythic{id=KingsCrown}` |  |
| Oraxen | `oraxen{id=SomeItemId}` |  |
| Nexo | `nexo{id=SomeItemId}` |  |
| ItemsAdder | `itemsadder{id=SomeItemId;display="Item Name"}` | Due to IA using components for display names and MMOItems not supporting them as of right now, some items generated through IA appear with no name. Use the `display` option to override the item display names. |

## Crafting Time

Recipes have a crafting time, which is the time in seconds players spend crafting the item. If set to zero (which is the default value), the player will be instantly given the crafted item. If it is non-zero, the ingredients will still be taken away from the player's inventory, and the item will be sent to the _Crafting Queue_, which is the line of items at the bottom of the station UI. From there, players can see the progression of the recipe.

Clicking a recipe/item in the crafting queue which is not completed yet will _cancel_ the recipe: the ingredients will be returned to the player. Clicking a recipe/item which is complete will give the player the recipe output.

```yaml
recipes:
    steel-sword:
        output: 'mmoitems{type=SWORD,id=STEEL_SWORD,amount=1}'
        crafting-time: 10 # time in seconds
```

## Perform specific actions when using/claiming/canceling the recipe

Please read [this wiki page](triggers.md) first to learn about crafting triggers. Using triggers you can perform specific actions when interacting with a recipe.

When setting up these triggers, there are three types of interactions that you can listen to, in order to modify the behaviour of your recipe. If your recipe is not instantaneous, you have to interact with it twice: first when clicking the recipe (which has the effect of consuming all the ingredients and placing the recipe in the crafting queue for some period of time - this interaction is refered as `use`), and then when claiming the recipe output in the crafting queue once (has the effect of giving the recipe output to the player - refered as `claim`). `cancel` is when clicking on a recipe in the crafting queue when it's not complete yet (ingredients are given back to the player).

```yaml
recipes:
    steel-sword:
        output: 'mmoitems{type=SWORD,id=STEEL_SWORD,amount=1}
        crafting-time: 10 # time in seconds
        on-use: # Optional - called when USING the recipe
        - 'message{format="You are crafting a steel sword"}'
        - ...
        triggers: # Optional - called when obtaining the item
        - 'message{format="You just claimed a steel sword"}'
        - ...
        on-cancel: # Optional - called when CANCELING any craft from that recipe
        - 'message{format="You are no longer crafting a steel sword"}'
        - ...
```

Be careful, don't mistake the `triggers` option for the `on-use` option. Some recipes have delays, therefore you don't obtain the item right away after using the recipe, but rather X seconds later. Instantaneous recipes trigger both lists at the same time though.

Triggers can be used along with [recipe conditions](conditions.md) to handle fictive ingredients, like a currency. You can have some placeholder condition like `%yourplugin_coins% >= 50` which checks if a player has at least 50 of some currency, and have a trigger that is called when the player uses the recipe that would have the effect of taking off the 50 currency from the player. In that case, you will also have to give the player his money back if we wants to cancel the craft.

These triggers are fully optional. If you don't want to use them, do not add any to the recipe config section. By using the output-item: false (see below)

## Extra Options

Recipe options are unique settings you can setup for each recipe.

```yaml
recipes:
    steel-sword:
        options:
            output-item: false
            hide-when-locked: false
            hide-when-no-ingredients: false
            silent-craft: true
```

| Option | Config Key | Description |
|--------|------------|-------------|
| Output Item | `output-item` | If the output item will be given to the player. |
| Hide When Locked | `hide-when-locked` | If the player doesn't meet the conditions the recipe will not show. |
| Hide When No Ingredients | `hide-when-no-ingredients` | If the player doesn't have the all the resources for the recipe, it will not be shown. |
| Silent Craft | `silent-craft` | When the item is crafted no noise will be made. |

