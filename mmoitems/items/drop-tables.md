---
order: 10
---

# 👛 Drop Tables

Data is stored in the ``drops.yml`` config file, located in the main plugin folder. Here is a config sample:

```yml
monsters:
  ZOMBIE:
    rock-table:
      coef: 7
      items:
        CONSUMABLE:
          ROCK: 50,1-3,10
    coin-table:
      coef: 1
      items:
        MISCELLANEOUS:
          GOLD_COIN: 1,1-10,0
```

Drop tables are split into **subtables**. When a drop table is read, a random subtable among all the subtables is chosen and the items from that subtable are then dropped. Having multiple subtables allows you to actually prevent two items from spawning at the same time.

Let's say for instance you want a zombie to drop a custom iron sword or a custom leather chestplate. Since having a chance to drop both items at the same time would be to overpowered, you can split the zombie drop table into two subtables. In the first subtable, you would have your iron sword, and in the second subtable you would have the iron chestplate. This way, these two items can't spawn at the same time.

Subtables can have different subtable coefficients. The higher the coefficient is, the higher the chance is for the subtable to be selected. Calculating the chance for a subtable to be selected is pretty easy. If, inside a drop table, the first subtable has a coefficient of 1 and the second has a coefficient of 2, the first subtable has a 1 in 3 chance of being selected. The chance for a subtable to be chosen can thus be calculated using the following formula.

```
chance = <subtable-coefficient> / <sum-of-all-subtable-coefficients>
```

The monsters section corresponds to the items that drop whenever an entity dies. Here is the config template:

```yml
MOB_NAME:
first-subtable:
    coef: <subtable-coefficient>
    items:
      ITEM_TYPE: (not case sensitive):
        ITEM_ID: (drop-chance),(min)-(max),(unidentified-chance)
      ITEM_TYPE:
        ITEM_ID: (drop-chance),(min)-(max),(unidentified-chance)
        #...
      #...
  second-subtable:
    coef: <subtable-coefficient>
    items:
      ITEM_TYPE: (not case sensitive):
          ITEM_ID: (drop-chance),(min)-(max),(unidentified-chance)
          #...
      #...
  #...
```

The _blocks_ config section corresponds to the items that drop whenever a block is broken/mined by a player. Follow the same format as in the monsters section, but replace the mob name by the block type name. Block types can be found in the [Spigot javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html).

**You can configurate three values for each subtable item:**

* **drop-chance** - The chance for your item to drop.
* **min & max** - The amount of drops is chosen randomly between these two values.
* **unidentified-chance** - the chance for your item to be unidentified when it drops.

**Additional subtable options:**

* **disable-silk-touch** - when set to true, this will prevent the subtable from dropping any item if the block was mined with a silk touch pickaxe. This prevents item duplication glitches with blocks like ores.

```yml
blocks:
  DIAMOND_ORE:
    rare-diamond:
      coef: 1
      disable-silk-touch: true
      items:
        MATERIAL:
          RARE_DIAMOND: 100,2-3,0
```

## Adding mmoitems to MythicMobs drop tables

Adding MMOItems to MM drop tables is pretty easy. Since 4.5, items created using MI can be summoned in MM drop tables using this format:

```yml
TestDropTable:
  Conditions:
  - playerwithin 100
  Drops:
  - mmoitems{type=SWORD;id=CUTLASS} 1 .1
```

This tells the drop table to add the sword from MMOItems called `CUTLASS` with a drop chance of 10% (so 0.1 in a MM drop table). You can change the amount of items you want to be dropped as if this drop was a vanilla drop. If you want the item to be unidentified when it is dropped, you will have to add one option within the brackets: this means that the item has a 30% chance of being unidentified when it is dropped
```yml
TestDropTable:
  Drops:
  - mmoitems{type=SWORD;id=CUTLASS;unidentified=0.3} 1 .1
```

NOTE: Both `type` and `id` values MUST be capitals.

The downside is that you cannot directly have one item drop at a time like you could have had with the MMOItems subtables.