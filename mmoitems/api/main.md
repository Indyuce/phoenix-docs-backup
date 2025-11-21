# 🔧 Plugin API

::: warning
Subject to big changes in MI7
:::

Join the Discord support channel if you need further info about the MMOItems API. Please use the `#developers` channel for questions!

## Checking if an ItemStack is from MI
First, get the NBTItem of your ItemStack using `NBTItem.get(ItemStack)`. This class lets you manipulate NBTTags from your item easily (1.14 has a new API which lets you do that using the ItemMeta, but for <1.14 support MI handles NBTs using NMS code). Use `nbtItem.hasType()` to see if the NBTItem can find the tag which corresponds to an MMOItems type. This method basically checks whether or not the plugin is from MI.

You can get the item type using `nbtItem.getType()`. This method calls a map checkup through all the plugin item types, so save its result in a field to save calculations.

## Checking if an MI item is a specific item
Again, get the NBTItem of your ItemStack using `NBTItem.get(ItemStack)`. You can then easily run `nbtItem.hasType()` to check if it's an MMOItem and then `nbtItem.getType()` and `nbtItem.getString("MMOITEMS_ITEM_ID")` to get the ID of the said item. You can compare the type and ID with whatever you'll need to check if an item is a specific one.

## Generating an item
Since 6.0 all items are now _item templates_. You can build an instance of `MMOItem` from a template by using one of the following methods:
```java
itemTemplate.newBuilder(RPGPlayer).build()
itemTemplate.newBuilder(level, tier).build()
```

Templates can be retrieved from the plugin `TemplateManager` by using `MMOItems.plugin.getTemplates.getTemplate(type, id)`. By using the `MMOItem#newBuilder()` method, you can create an `MMOItemBuilder` which can build an ItemStack instance out of an `MMOItem`.

```java
MMOItem mmoitem = MMOItems.plugin.getMMOItem(MMOItems.plugin.getTypes().get("SWORD"), "CUTLASS");
ItemStack item = mmoitem.newBuilder().build();
```
Make sure you don't use the same `MMOItemBuilder` twice to build an `ItemStack` using the `build()` method. This method scrambles a lot of item data and thus can't be used twice. However you can use the same `MMOItem` instance to generate as many instances of `MMOItemBuilder` as you want.

The following method directly returns the ItemStack instance:
```java
MMOItems.plugin.getItem(MMOItems.plugin.getTypes().get("SWORD"), "CUTLASS")
```
Note however, that using this method will return an item that is not scaled with the player level and without a randomized tier. If you want to get an item that is scaled and with a randomized tier use:
```java
MMOItems.plugin.getItem(type, id, level, tier) // fixed level and tier
MMOItems.plugin.getItem(type, id, playerdata) // scale on player data
```

## Retrieving item tiers

You can get item tiers by retrieving the `TierManager` class from the plugin.
```java
TierManager tiers = MMOItems.plugin.getTiers();
boolean exists = tiers.has("RARE");
ItemTier rare = tiers.get("RARE");
Collection<ItemTier> all = tiers.getAll();
```

## Retrieving item type instances
Since 4.6, types are not stored in an enum anymore since you can add as many as you want. Type instances are now stored in a ``TypeManager`` class instance, which can be accessed using the following method:
```java
TypeManager types = MMOItems.plugin.getTypes();
boolean exists = types.has("SWORD");
Type sword = types.get("SWORD"); // e.g get the type which ID is SWORD
Collection<Type> all = types.getAll(); // get all loaded types
```

## Opening plugin GUIs

```java
new AdvancedTypeList(player, 1).open(); // opens the recipe list at type selection
new AdvancedRecipeList(player, MMOItems.plugin.getTypes().get("SWORD")).open(); // opens the recipe list (after selecting item type)
new AdvancedRecipeWorkbench(player).open(); // opens the advanced workbench
new ItemEdition(player, MMOItems.plugin.getTypes().get("STAFF"), "EARTH_STAFF").open(); // opens the edition gui for a specific item
```

## Checking if a GUI is from MI

Every GUI from MMOItems is created used a custom inventory holder which extends ``PluginInventory``. To check if a GUI is a GUI for MI, just retrieve the inventory holder and check if it's an instance of that class:
```java
boolean isMMOItemsUi = inventory.getHolder() instanceof PluginInventory
```