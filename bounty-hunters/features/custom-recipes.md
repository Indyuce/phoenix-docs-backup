---
order: 10
---

# 🥘 Crafting Recipes

![javaw_1vPf59c1Ob](uploads/ba7ef6268a5ebe6019c1f79c4af69c4e/javaw_1vPf59c1Ob.gif)

MMOItems allows you to register custom recipes where you can use blocks such as crafting tables, furnaces and even campfires to craft MMOItems. Items can have multiple recipes both in the same crafting type or in different crafting types entirely. For example, if you wanted the player to be able to cook a Gourmet Steak you can register that item's recipe under either a furnace, a smoker, a campfire or all three. You would simply have to create a recipe for all three crafting types. Recipes support both vanilla items and MMOItems. In addition, any recipe you create that would have a vanilla equivalent such as crafting a stone block into a stone button will be overridden by the custom recipe. Remember that everytime you create a new recipe or edit an existing one, you must do /mi reload recipes

There are 9 different crafting types that you can assign to an item and each type corresponds to the crafting block or command.

The initial set-up for creating a craftable item is the same as any other MMOItem, where you define its stats, name, lore, etc. However, under the base level, you add a crafting option and beneath that option, you add the crafting type. The 9 crafting types currently available are: smithing, supershaped, smoker, furnace, shaped, megashaped, campfire, shapeless, blast. The names are fairly self-explanatory.

**The use of the GUI Item Editor is HIGHLY RECOMMENDED as it makes visualizing these recipes a lot easier.**

```
#This is an unfinished item that doesn't have an actual recipe linked to it, just a crafting type.
SMOKERRECIPE:
  base:
    name: Smoker
    material: WATER_BUCKET
    crafting:
      smoker: #This is what defines your crafting type.
```

If you want to assign multiple recipes to a single crafting type, you do so like this:

```
SMOKERMULTIPLERECIPES:
  base:
    name: Smoker
    material: WATER_BUCKET
    crafting:
      smoker: #This is what defines your crafting type.
        '1': #This lets MMOItems know that there are multiple recipes registered to the crafting type (smoker in this case).
          input: #explained later
        '2':
          input:
```

If you want to assign multiple recipes to different crafting types, you just add another crafting type on the level beneath crafting.

```
SMOKERANDFURNACERECIPE:
  base:
    name: Smoker
    material: WATER_BUCKET
    crafting:
      smoker: #This is what defines your crafting type.
        '1': #This lets MMOItems know that there are multiple recipes registered to the crafting type (smoker in this case).
          input: #explained later
        '2':
          input:
      furnace:
        '1': 
          input:
```

## Smithing Table Recipes

Smithing table recipes are the way you would want to upgrade your items. To set an item's recipe under a smithing table, set the crafting type as smithing. Smithing table recipes have several options.

input are what items the player must **"input"** or insert into the slots. You can define these items as either MMOItems or Vanilla items. At its base, it looks like this.

```
SMITHINGTABLERECIPE:
  base:
    name: Smithing Table
    material: WATER_BUCKET
    crafting:
      smithing:
          input: m EXAMPLE_MMOITEM_TYPE EXAMPLE_MMOITEM_ID 1.0..|v STONE - 1.0..
                 #The m defines this item as an mmoitem. the v defines it as a vanilla item.
```

input also determines which slot the items go into. The slot on the left corresponds to the first input and the slot on the right corresponds to the second input. The GUI is highly recommended for this as it makes viewing the recipe much easier.

**drop-gems:** makes any gems that are slotted into an MMOItem to be dropped and thus recoverable when the player crafts the item. Can be true or false.

**upgrades:** dictates what happens to any upgrades (the +X you see when an item gets upgraded) that may have been present on the MMOItems used as ingredients. You have several options: ADDITIVE, MAXIMUM, EVEN, MINIMUM and NONE. ADDITIVE adds the upgrade levels up, so a +1 item and a +3 item will return a +4 item. MAXIMUM will give the higher upgrade level. So a +1 item and a +3 item will return a +3 item. EVEN will average the upgrade levels. So a +1 item and a +3 item will return a +2 item. Minimum will give the lower upgrade level. So a +1 item and a +3 item will return a +1 item. NONE does not retain any upgrade levels.

**enchantments:** dictates what happens to any enchantment on the ingredients when you craft the item. It has the same options as upgrades and they do the exact same thing.

**output:** dictates what ingredients will not be consumed upon crafting the item (Like a bucket of milk becoming an empty bucket in a cake recipe). It's defined the same way as input. The items here do not have the be the same as in input however and can be something entirely different.

**amount** defines how many items this recipe will create.

This is what a full config should look like.

```
SMITHINGTABLERECIPE:
  base:
    name: Smithing Table
    material: WATER_BUCKET
    crafting:
      smithing:
          input: m EXAMPLE_TYPE EXAMPLE_ID 1.0..|v STONE - 1.0..
          drop-gems: true
          upgrades: ADDITIVE
          enchantments: ADDITIVE
          output: v diamond - 1.0..|v AIR - 1..
          amount: 10
```

This recipe takes an MMOItem on the left slot, a stone block on the right and will drop gems and add up the upgrades and enchantments of the ingredients. It will also output 10 of the items and will return 1 diamond on craft.

## Furnace/Blast Furnace/Smoker/Campfire Recipes

These four crafting types have the same options and the same general idea. You insert the ingredient where you would any ore/food and add fuel. For campfires, simply right click the campfire with the ingredient in your hand.

At its base, these crafting types will look like this:

```
COOKINGRECIPE:
  base:
    name: COOKING RECIPES
    material: WATER_BUCKET
    crafting:
      campfire: #This would be for a campfire, replace with furnace/smoker/blast as needed
        input: []
```

These are the options available to these crafting recipes.

**input:** is not needed and should be defined as \[\].

**hidden:** dictates if the item should be hidden from the player's recipe book even if they've unlocked it. Uses MMOItem Recipe Books, coming soon? Can be true or false.

**item:** dictates what the ingredient will be. Use m MMOITEM_TYPE MMOITEM_ID AMOUNT for an mmoitem or v VANILLA_ID AMOUNT for a vanilla item.

**exp:** dictates how much exp the recipe should give you.

**time:** dictates how long it takes to cook/smelt the ingredients in ticks.

A complete config would look like this:

```
COOKINGRECIPE:
  base:
    name: Cooking Recipe
    material: WATER_BUCKET
    crafting:
      smoker:
          input: []
          hidden: true
          item: v STONE_BRICKS - 1.0..
          exp: 10.0
          time: 10.0
```

In this example, cooking one stone brick in a smoker will return 10 exp and take 10 ticks to smelt.

## Shaped/Super Shaped/Mega Shaped/Shapeless Recipes
![Crafting](uploads/5a2b56120739a8764bd4226a75cdbbff/Crafting.png)
Shaped, Super Shaped and Mega Shaped recipes all share the same options. However, Shaped recipes can be hidden from the recipe book. Shaped simply means that the ingredients must be in a specific layout in order for the item to be craftable, a bit like how you can only craft a stone pickaxe one way. Super Shaped and Mega Shaped are the same thing but bigger. You access these crafting tables by doing /superworkbench or /swb and /megaworkbench or /mwb respectively. Super Shaped is a 5x5 grid and Mega Shaped is a 6x6 grid.

All shaped recipes have these options:

input: dictates what ingredients must be placed in what slot in order to craft the item.

This is what a normal shaped recipe would look like:

```
SHAPEDRECIPE:
  base:
    name: Shaped
    material: WATER_BUCKET
    crafting:
      shaped:
        '1':
          input:
          - v stone - 1.0..|v AIR 0 1..|v AIR 0 1..
          - v AIR 0 1..|v AIR 0 1..|v AIR 0 1..
          - v AIR 0 1..|v AIR 0 1..|v stone - 1.0..
```

Another way to view it is like this:

```
SHAPEDRECIPE:
  base:
    name: Shaped
    material: WATER_BUCKET
    crafting:
      shaped:
        '1':
          input:
          - Slot 1|Slot 2|Slot 3
          - Slot 4|Slot 5|Slot 6
          - Slot 7|Slot 8|slot 9
```

Super Shaped and Mega Shaped crafting recipe inputs are the exact same, just with more columns and rows to reflect the larger crafting grids. In order for an slot to be empty, you must specify this with v AIR 0 1..

**output:** is the exact same layout as input except it dictates what items will not be consumed upon crafting the item. You can also use it to give players a new, "downgraded" ingredient if you wanted to.

hidden dictates if the item will be hidden from the recipe book.

Shapeless crafting recipes are the exact same as shaped recipes, except the exact layout does not matter.