# 💰 Drop Tables

The `/drop-tables` folder is where you setup all of your custom drop tables for [blocks](mining.md) and [loot chests](loot-chests.md). Since their use is not limited to block drops, we decided to give them a separate folder so that you can setup them there and only use their reference in other configs to make them lighter/easier to read and setup.

Drop tables can be used to drop vanilla items, mmoitems or the content of another MMOCore drop table. You can encapsulate drop tables inside of other drop tables to create complex drop tables.

## Default Config

```yaml
# You may create as many drop tables as you want. You can also
# make drop tables refer to other drop tables.
#
# DON'T try to create recursive drop tables (drop tables which
# call themselves to multiply items dropped). It will work, but
# if you put a probability of 1 it will crash your server
# instantly. The more the probability, the higher your chance
# to slow down your server performances. Fun fact though :p

diamond-drop-table:
    items:
    - 'vanilla{type=DIAMOND} 1 1-3'
    - 'mmoitem{type=material;id=RARE_DIAMOND} .1 1-3'
    - 'droptable{id=other-drop-table} .1'

other-drop-table:
    items:
    - 'vanilla{type=STONE} 1 1-3'
```

This default file is pretty self explanatory. The first drop table example showcases all the drop items you can use inside of any drop table. In order to create a drop table, just add a new section to any file in the `/drop-tables` folder. Then find an ID for your drop table (this identifier must be unique and will be used as a reference later).

The `diamond-drop-table` example is the drop table used in the [Mining profession](../features/mining.md) when mining diamond ore. The items it may drop are vanilla diamonds, a rare diamond from MMOItems, and all the content from the table called `other-drop-table` (a stone block).

The numbers after the item mean the chance, and then the amount (can be an integer range). The format for every drop item is the following:

```
droptype{<parameter1>=<value1>;<parameter2>=<value2>} <drop-chance> <min-max> <weight>
```

You don't have to specify any of the three last parameters (drop chance/amount/weight) although you will need to specify, for instance, drop chance if you want to utilize the weight system (explained at the bottom of the page).

## Available Drop Types

| Drop Item | Format |
|-----------|--------|
| Another Drop Table | `droptable{id=drop-table-id} <chance> <amount>` |
| Vanilla Item | `vanilla{type=ITEM_MATERIAL} <chance> <amount>` |
| Gold Coin | `gold{} <chance> <amount>` |
| Note | `note{min=MIN_WORTH;max=MAX_WORTH} <chance> <amount>` |
| mmoitem | `mmoitem{type=MMOITEM_TYPE;id=MMOITEM_ID} <chance> <min-max>` |
| gentemplate | `gentemplate{id=TEMPLATE_ID;tier=TIER_NAME;level=<int>;match-level=<true/false>} <chance> <min-max>` |
| miloot | `miloot{type=ITEM_TYPE_ID;class="Class Name";match-class=<true/false>;tier=TIER_ID;level=<int>;match-level=<true/false>} <chance> <min-max>` |

`mmoitem`, `gentemplate` and `miloot` are only available when using MMOItems. For the `gentemplate` and `miloot` drop table items, please refer to [this MMOItems wiki page](../../mmoitems/items/obtain-item.md).

## Table Capacity & Items Weights

Item weights and table capacity fix the problem of having a drop table with two items that are both too rare to drop at the same time. Using item weight you can define how 'heavy' each drop is compared to others, in order to limit extreme drops where one player has enough luck and drops every single rare item from a boss.

```yaml
weighted-drop-table:
    items:
    - 'vanilla{type=DIAMOND} .33 1-3 1'
    - 'vanilla{type=EMERALD} .5 1-3 1'
    - 'vanilla{type=GOLD_INGOT} 1 1-3 1'
```

Example scenario: you want ONLY one of these three items to drop and every item has 1/3 chance to be selected.

Every drop item has an item weight of 1, meaning that if this drop table is utilized by a loot chest (or any other system that supports MMOCore drop tables) with a capacity of 1, only one item will be selected.\
**When a drop table is called to generate random loot, the sum of all selected drop items WEIGHTS cannot exceed the given CAPACITY.** The same drop table can be used with different capacities (for practical reasons). If you use the drop table setup above with a capacity of 3, you can drop the three items at the same time. If you use it with a capacity of 2, 2 items will spawn at most.

Keep in mind you can use any value for the item weights. You can also have items with 0 weight along with weighted items in the same drop table (in fact, this is the setup you will be probably using to setup rare boss drops).

When a drop table is called, drop items are read in the order given by the config setup. You must keep that in mind when setting up your item drop chances, as this is why items towards the ends have a higher chance of being picked. The last item always has probability 1 because it's guaranteed to be picked, if all the previous item rolls failed.

### Where to configure the loot table capacity

If you are using drop tables inside of loot chests, please refer to [this page](loot-chests.md#loot-chest-tiers) to configure the chest loot table capacity.

Otherwise, you can specify the default capacity for any loot table using the `capacity` option:

```yaml
some-drop-table:
    capacity: 2
    items:
    - 'vanilla{type=DIAMOND} .33 1-3 1'
    - 'vanilla{type=EMERALD} .5 1-3 1'
    - 'vanilla{type=GOLD_INGOT} 1 1-3 1'
```

If absolutely no capacity is specified, MMOCore will use a default capacity of 100.

## Drop Table Conditions

Conditions are added to the drop table using the following syntax. Learn more about the conditions system [here](../misc/conditions.md).

```yaml
diamond-drop-table:
    items:
    - 'vanilla{type=DIAMOND} 1 1-3'
    - 'mmoitem{type=material;id=RARE_DIAMOND} .1 1-3'
    - 'droptable{id=other-drop-table} .1'
    conditions:
    - 'level{profession=mining;amount=10}'
    - ...
```

## Extra Options

Toggling on the `shuffle` option will shuffle the order in which items are looted inside the drop table. This can be used to easily increase the randomness of drop tables.

```yaml
some-drop-table:
    shuffle: true
    items:
    - 'vanilla{type=DIAMOND} 1 1-3'
    - 'mmoitem{type=material;id=RARE_DIAMOND} .1 1-3'
```