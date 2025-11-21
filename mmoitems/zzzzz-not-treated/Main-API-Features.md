Join the Discord support channel if you need further info about MMOItems API.

## Checking if an ItemStack is from MI
First, get the NBTItem of your ItemStack using `NBTItem.get(ItemStack)`. This class lets you manipulate NBTTags from your item easily (1.14 has a new API which lets you do that using the ItemMeta, but for <1.14 support MI handles NBTs using NMS code). Use `nbtItem.hasType()` to see if the NBTItem can find the tag which corresponds to an MMOItems type. This method basically checks whether or not the plugin is from MI.

You can get the item type using `nbtItem.getType()`. This method calls a map checkup through all the plugin item types, so save its result in a field to save calculations.

## Checking if an MI item is a specific item
Again, get the NBTItem of your ItemStack using `NBTItem.get(ItemStack)`. You can then easily run `nbtItem.hasType()` to check if it's an MMOItem and then `nbtItem.getType()` and `nbtItem.getString("MMOITEMS_ITEM_ID")` to get the ID of the said item. You can compare the type and ID with whatever you'll need to check if an item is a specific one.

## Generating an item
Since 6.0 all items are now _ItemTemplates_. You can get an _MMOItem_ instance from a template by using `itemTemplate.newBuilder(RPGPlayer).build()` or `itemTemplate.newBuilder(level, tier).build()`.
Templates can be retrieved from the _TemplateManager_ by using `MMOItems.plugin.getTemplates.getTemplate(type, id)`
By using the `newBuilder()` method (from the _MMOItem_ class), you can create an _MMOItemBuilder_ which can build an ItemStack instance out of an _MMOItem_.
```
MMOItem mmoitem = MMOItems.plugin.getMMOItem(MMOItems.plugin.getTypes().get("SWORD"), "CUTLASS");
ItemStack item = mmoitem.newBuilder().build();
```
Make sure you don't use the same _MMOItemBuilder_ twice to build an _ItemStack_ using the `build()` method. This method scrambles a lot of item data and thus can't be used twice. However you can use the same _MMOItem_ instance to generate as many _MMOItemBuilders_ as you want.

The following method directly returns the ItemStack instance:\
`MMOItems.plugin.getItem(MMOItems.plugin.getTypes().get("SWORD"), "CUTLASS")`
<br>Note however, that using this method will return an item that is
<br>not scaled with the player level and without a randomized tier.
<br>If you want to get an item that is scaled and with a randomized tier use:\
`MMOItems.plugin.getItem(type, id, level, tier)` or `MMOItems.plugin.getItem(type, id, playerdata)`

## Retrieving item tier instances
You can get item tiers by retrieving the _TierManager_ class from the plugin.
```
TierManager tiers = MMOItems.plugin.getTiers();
boolean exists = tiers.has("RARE");
ItemTier rare = tiers.get("RARE");
Collection<ItemTier> all = tiers.getAll();
```

## Retrieving item type instances
Since 4.6, types are not stored in an enum anymore since you can add as many as you want. Type instances are now stored in a _TypeManager_ class instance, which can be accessed using the following method:
```
TypeManager types = MMOItems.plugin.getTypes();
boolean exists = types.has("SWORD");
Type sword = types.get("SWORD"); // e.g get the type which ID is SWORD
Collection<Type> all = types.getAll(); // get all loaded types
```

## Opening plugin GUIs
```
new AdvancedTypeList(player, 1).open(); // opens the recipe list at type selection
new AdvancedRecipeList(player, MMOItems.plugin.getTypes().get("SWORD")).open(); // opens the recipe list (after selecting item type)
new AdvancedRecipeWorkbench(player).open(); // opens the advanced workbench
new ItemEdition(player, MMOItems.plugin.getTypes().get("STAFF"), "EARTH_STAFF").open(); // opens the edition gui for a specific item
```

## Checking if a GUI is from MI
Every GUI from MMOItems is created used a custom inventory holder which extends _PluginInventory_. To check if a GUI is a GUI for MI, just retrieve the inventory holder and check if it's an instance of that class: `inventory.getHolder() instanceof PluginInventory`