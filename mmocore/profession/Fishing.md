---
order: 3
---

# 🎣 Fishing

MMOCore may be used to override/rewrite default fishing drop tables.

## Fishing Experience

Using the `fishitem` [experience source](../level/sources.md), you can make players earn a certain amount of EXP when fishing specific items, like fishes, enchanted books, saddles, etc. The rarer the item, the more experience players should earn.

Currently, the `fishitem` experience source only supports item materials, which means a player will not get extra EXP from looting a mending enchanted book over a Power I enchanted book. The only way to bind specific experience amounts to amounts is to hook onto MMOItems items using the fishing drop tables which can be edited in the fishing.yml profession config file.

**If you don't want to utilize professions in general**, just ignore the fishing experience sources and use the fishing drop tables without specifying any experience. **If you don't want to utilize the MMOCore fishing drop tables**, just use the fishing experience sources, and delete any default fishing drop tables.

## Configuration

The main config file is `professions/fishing.yml`.

```yml
name: Fishing
experience:
    base: 20
    per-level: 3

exp-sources: {}

# Fishing drop tables which override MC default.
# When fishing, the plugin reads through all the drop tables
# and picks THE first one which all conditions are met!!
# You must put at first place the drop tables which
# have the most conditions/which are the most important.
# Number of tugs = number of times you need to click to fish.
on-fish:
    overriding-drop-table:
        conditions:
        - 'region{name="swamp,second-region"}'
        - 'biome{name=beach}'
        
        # When drop table is read, one of these
        # items will be selected randomly.
        items:
        
        # Tugs needed: 4 to 5
        # Fishing EXP earned: 1 to 6
        - 'mmoitem{type=CONSUMABLE;id=SUSHI_ROLL;tugs=30-40;experience=1-6} 1 1-1 9'
        
        # Tugs needed: 10 to 20
        # Fishing EXP earned: 20 to 30
        - 'mmoitem{type=GEM_STONE;id=SPITEFUL_OPAQUE_DIAMOND;tugs=10-15;experience=20-30} 1 1-1 1'

    # Default drop table which always apply.
    # When removing every drop table, the vanilla
    # fishing mecanism is back.
    default:
        items:
        - 'vanilla{type=SALMON;tugs=4-5;experience=1-6} 1 2-5 1'
```

_As you can see, the default fishing config setup does not utilize fishing experience sources although you can add other exp sources to that profession if required._ Fishing drop tables are defined by two options: conditions and items.

When a player fishes, MMOCore goes through all the fishing drop tables and picks the first one which conditions are all met by the player. The two conditions available as of right now are the `region` condition which hooks onto WorldGuard. This condition lets you configure specific drop tables for each WorldGuard region. This lets you create specific regions where you can fish rarer items. You can use the [waypoints](Waypoints) system in parallel to create a unique fishing zone with rare drops! The other condition is the `biome` condition, which reads the biome your standing in. Biomes must be formatted in the `name=<biome>` format to function -- see example above.

If you create a drop table with no condition, make sure it's the last one otherwise it will always be chosen by MMOCore. Moreover creating a no-condition fishing drop table means that MMOCore fishing drop tables **always** override the default vanilla drop tables.

### Fishing drop tables
Learn about [regular drop tables](Drop Tables) first.

Fishing drop tables are slightly different from regular drop tables (used by random chests or block drops). The main difference is that a fishing drop table always require ONE and only ONE item to be randomly picked and dropped.

This changes the way MMOCore picks that one random item. In fact the `chance` option is never used by fishing drop tables. Even if you set the drop item chance to 0%, your item might be picked.

Fishing drop tables **use item weight to determine drop chance**. Every table item is assigned a weight, which is a number. The higher this number, the higher the drop chance. The probability of an item being picked and dropped is `<item weight> / <sum of item weights from all the items in that drop table>`.

The generic format for a drop item is the following (same as a regular drop table item). As explained above, the `<drop-chance>` option is completely useless and can be set to anything.
```
droptype{<parameter1>=<value1>;<parameter2>=<value2>} <drop-chance> <min-max> <weight>
```

There are some advantages to this weight system. First of all, if you ever want to add a new item to your fishing drop tables, you don't actually have to edit all the previously configured drop chances. Just add some new table item with a specific weight, and because of the way the drop chances are calculated, this will have the effect of 'updating all the other item drop chances'. The second advantage is that it's really adapted to fishing tables requiring to have only ONE item dropped at a time.

### Tugs
MMOCore improves the default fishing mechanism by adding **tugs**. When a player catches a fish, the fish tries to resist, therefore the player must spam-click his fishing rod until it gives up! The tugs dictate the amount of clicks needed to catch the fish.
If a player stops clicking while the fish is resisting, the fish will eventually go away.

To set the amount of tugs required to catch a certain item, add `;tugs=min-max` to the item line config. You may also use `;tugs=10` if you want that tugs number to always be the same.

### Experience
To have an item give the player a specific amount of exp when fished, add `experience=min-max` to the item line config. A random amount of exp anywhere between the two given boundaries will be rolled every time the item is caught by a player. You may also use `experience=30` if you want the exp amount to be a constant.

### Vanilla exp
You can also give vanilla exp when catching a fish by adding `vanilla-exp=min-max` to the item line config.  This field is optionnal and works exactly like `experience`.