---
order: 9
---



# 🎁 Loot Chests

Lootable chests are a great way to reward RPG players for exploring your world. They spawn around players in specific regions with randomly generated loot. Loot chests can have tiers; the higher the tier, the better the loot.

The following code snippets can be found under the `/loot-chests` folder.

## General options

These options can be found inside the MMOCore `config.yml`.
```yml
loot-chests:

    # Time in seconds it takes for a loot chest to
    # expire after it was spawned. 600 is 10 minutes.
    chest-expire-time: 600
    
    # Interval in seconds before the same player
    # spawns two loot chests in ANY region.
    player-cooldown: 600
```

## Loot Chest Regions

MMOCore lets you setup regions where chests can spawn. The first thing you will need to define is the region boundaries just like with WorldGuard regions:
```yml
loot-chest-region-id:
    
    # Region boundaries
    bounds:
        world: world_name_here
        x1: 32
        x2: -15
        z1: -419
        z2: -375
```
The `loot-chest-region-id` only serves as an internal identifier. It can be anything, just make sure two regions do not share the same ID when editing the configs.

You will then need to define how frequent chests spawn in that region (period is given in seconds, it's set to 120 by default which corresponds to 2 minutes).
```yml
loot-chest-region-id:
    spawn-period: 120
```
Every X minutes, the region will look for a random player in that region and spawn a chest nearby. Keep in mind that MMOCore will first filter the players which are still on cooldown: that means no chest will spawn in a specific region, if and only if there are either no player in that region/all the players are on cooldown.

## Loot Chest Tiers

Chest tiers directly determine the loot chest drops. Every tier has a set chance to be chosen when a loot chest is spawned in a region.
```yml
loot-chest-region-id:
    tiers:
    
        # Some tier
        normal:
        
            # Particle effect played around a spawned loot chest
            effect:
                type: OFFSET # Type of particle effect used
                particle: FLAME # Particle used to play the effect
                period: 60 # Plays the effect every 60 ticks
            
            chance: 0.9
            drops:
                items:
                - 'vanilla{type=DIAMOND} 1 1-10 8'
                - 'vanilla{type=GOLD_INGOT} 0.5 1-10 4'
                - 'vanilla{type=EMERALD} 0.5 1-10 4'

        # Some other tier
        rare:
            effect:
                type: HELIX
                particle: FIREWORKS_SPARK
                period: 80
            chance: 0.1
            capacity: 10
            drops: drop-table-id
```

Every tier has its own particle effect that will be displayed around the loot chest block every X ticks (it corresponds to the `period` option), until it is opened/it expires. A particle effect is defined by its type (the shape or figure the particle will draw) and the particle used (flame, firework, water, etc. particles).
Available particle types are HELIX, OFFSET and GALAXY. Available particle names can be found over the [Spigot Javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html).

`chance` is the probability for the tier to be chosen when a loot chest is spawned. All of the tier chances should add up to 1 (10% chance is 0.1).

`drops` is the drop table used to fill the loot chest inventory, along with `capacity` which is the chest capacity. For more information about how loot table _capacity_ works, please refer to this [wiki section](Drop Tables#capacity-and-drop-item-weight). You can either directly specify a number using `capacity: 10` or use a scaling formula instead like this:

```yml
capacity:
    base: 10 # Base value of 10 capacity
    scale: 3 # 3 extra capacity for every player level
    spread: 0.1 # +/-10% spread in average
    max-spread: 0.3 # Relative offset due to the 'spread' option cannot be greater than 30%
```

The `spread` and `max-spread` options are optional if you're using a scaling formula for the loot capacity.

For the `drops` option, do note that you can either specify a drop table ID if your drop table is already setup in your drop tables config folder, or an entire config section if you want to define a new drop table specifically for the chest tier.

## Default Config

`chests.yml` handles all of your RPG random loot chests! This wiki page is unfinished as there are more loot options and plugin compatibilities that get added to the possible drop tables.

```yml
'world 59 71 131':

    # Create directly your drop table here.
    drop-table:
        items:
        - 'vanilla{type=DIAMOND} 1 1-3'
        - 'gold{} .9 1-3'
        - 'gold{} .9 1-3'
        - 'gold{} .9 1-3'
        - 'gold{} .9 1-3'
        - 'gold{} .9 1-3'
        - 'gold{} .9 1-3'
        - 'note{min=1;max=10} .9 1-3'
    
    # Ticks the chest takes to appear again.
    regen-time: 40
    
    # The particle played every 4sec around the chest.
    # Types available: helix|offset|galaxy
    # Particle names here: https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html
    effect:
        type: helix
        particle: FLAME
```

The name of your chest, in this case "world 59 71 131", defines where the chest is placed. It uses WORLD,X,Y,Z format. You do not actually name your chests, and instead just put different coordinates down where you want a chest.

* drop-table

This option defines what could possibly be in your chest. It currently supports MMOItems, Vanilla items, MMOCore currency (gold and notes). The format is shown in the default chest.

The 2 sets of numbers after the entry are drop chance and drop amount. In this example .9 (90%) is the chance for the chest to include it, and 1-3 is the randomized amount.

* regen-time

This is the time it takes for the chest to respawn with randomized loot, in ticks. When a chest is opened and cleared, it will be deleted. Or a chest can be punched to drop all the loot on the ground.

* Effect

In order to make loot chests stand out, you can put particle effects on them so players know they are special chests. You can also use these particle effects to determine chest tiers. Just give different chests and drop tables, different effects!
