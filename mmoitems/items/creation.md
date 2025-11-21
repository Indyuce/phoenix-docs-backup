This wiki page explains the two methods you can use to create item templates in MMOItems and briefly goes over how items are generated.

## Item Edition GUI
The item editor lets you create and edit items directly in-game without having to tamper with config files. This is a powerful and easy-to-understand method although we recommend advanced users to directly go for manual config file edits which is much faster if you know how all the stats are formatted.

![](https://i.imgur.com/GtRzKfH.gif)

1. Open the game and create an item using via this command: `/mi create <ITEM_TYPE> <YOUR_ITEM_ID>`
    1. You may use /mi list type to check all the available item types (Sword, Axe, Tool...).
    2. The item ID will be used in every command/config file to identify the item. It should be something like STEEL_DAGGER to make config setup cleaner.
2. The edition menu should open up after performing the create command. If you close it, you can still access it using this command: `/mi edit <ITEM_TYPE> <YOUR_ITEM_ID>`
    1. On the 5th slot of the inventory, you can see your item and its current stats. You can click the chest item to add it to your inventory.
    2. Every other item corresponds to an item stat that you can edit. Instructions on how to edit them are displayed directly in-game.
    3. Once you added all the stats you wanted, get your item and have fun!

## Manual Config File Edition
Advanced users should consider using this method as it is way faster if you already know the item options you'd like to use and how to format them.
1. Open up the /MMOItems/item/ folder.
2. Select your item type and open the corresponding .yml file using your favourite text editor.
3. Here is the default item config template:
```yaml
YOUR_ITEM_ID:
  base:
    material: YOUR_ITEM_MATERIAL
```
4. All materials can be found [here](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html). The item material is the first thing to add since it is the only real option an item needs to be able to be generated.
5. Add as much item options (Abilities, Attack Damage....) as you want. You can see 'all' of the available item options (and how to configure them) on [this wiki page](Item-Stats-and-Options).
6. Save the file and get back on Minecraft. Use /mi reload to let MMOItems load the item you just added to your config file, and use `/mi give <ITEM_TYPE> <YOUR_ITEM_ID>` to get your item!

## How Items Work (Very important!)
When creating an item in MMOItems, you are actually creating an item **template**. An item template is composed of a set of **default** item options (display name, material, enchants, attack damage..), and a **set of item modifiers** which are chosen randomly and applied to the base item data when the item is given to a player.

The objective of this system is to make **ONE item template** able to generate **MULTIPLE versions/instances** of the same item, just like in any RPG game. The item modifiers are what makes every version of the item unique: an OP version of the item would have many OP modifiers whereas the newbie instance of the item would have 1-2 smaller modifiers.

When being generated, items all have an **item level** which directly determines how strong the item stats are and a **modifier capacity** which determines how many modifiers the item can have. MMOItems item generator hooks onto the MMOItems tier system. The higher the item tier, the more modifiers the item has. In other words, the item tier determines the item **modifier capacity**.

The two options that are the item tier and the item level are our **"randomness cursors"**. That means they determine alone how powerful an instance of an item is. And they're totally independant, which means you can have high level weapons, with little to no modifiers, and conversely a newbie item with a lot of modifiers.

We'll be going over a few examples to understand the basic concept of the MMOItems item generator.

### Example I
![](https://i.imgur.com/UFjM4d9.png)    ![](https://i.imgur.com/HF4FEOm.png)

These items use the same template, which is an item called `Long Sword`. However, the right one has a `Sharp` modifier which gives him +3 Atk Damage while the left one has no modifier.

These two items have the same attack speed because it was chosen not to scale with the item level. However the attack damage does scale with the item level: although the first item has got a higher level, the second item has a `Sharp` modifier and therefore has more attack damage.

The `Sharp` modifier gives the second item the `Sharp` prefix and adds an extra line of text in the item lore.

### Example II
![](https://i.imgur.com/HF4FEOm.png)    ![](https://i.imgur.com/YA6g1Bd.png)

The item at the right has a much higher item level and therefore his attack damage is much higher. It also has two modifiers: `Sharp` and `Fiery`. `Sharp` still gives the item +3 Atk Damage but it's pretty useless given its level. `Fiery` gives the item a nice red name prefix and an on-hit burn ability.

The second item has the `Rare` item tier, therefore has much more modifier capacity than the non-tiered sword, which explains why it received two modifiers. Non-tiered items also have a modifier capacity, but it is much lower.

You can only see the `Fiery` prefix because this modifier has a higher priority (although you can configure the modifiers so that all the prefixes show, and have funny item names with 10 suffixes or prefixes at the same time!).

Last but not least, a higher level does not mean more modifiers (hence the last remark of the [this paragraph](Item-Creation#how-items-work-very-important)): the modified weapon has a lower level than the one with no modifier.

### Example III
![](https://i.imgur.com/gf9cHBH.png)\
The default item is a bow with some attack damage and crit chance. The first `Heavy` modifier makes it two-handed, adds a few attack points and some critical strike power. The second modifier which has a suffix adds an on-hit ability.

### Item Template Config
This is how an item template looks in the MMOItems config files.
```yaml
LONG_SWORD:
    base:
        material: IRON_SWORD
        attack-damage:
            base: 10
            scale: 1
        critical-strike-chance: 30
        # More item stats here...
    modifiers:
        first-modifier:
            prefix: 'Modifier Prefix'
            stats:
                attack-damage: 3
                # More item stats here...
        second-modifier:
            suffix: 'Modifier Suffix'
            stats:
                pvp-damage: 20
                # More item stats here...
```
The `base` config section contains all the base item data (item material, display name, ie all the info which should be applied to the item independently of its item level). The `modifiers` config section contains all the modifiers which can be applied to the item.