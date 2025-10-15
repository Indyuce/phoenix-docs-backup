### Check for the target script location biome
Checks if the script target location (or source location when `source` is set to true) biome is a specific biome. List of biomes [here](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/Biome.html). You can use multiple biome names, separate them using `,`. Warning, biome names are highly case sensitive.

```
example_condition:
    type: biome
    name: 'BIRCH_FOREST,DEEP_COLD_OCEAN,END_HIGHLANDS'
    source: false
```

### Checking if some location is within block boundaries
Checks if the target location of the script (or source location, if `source` is set to true) is within a boundary that is defined by two other positions which are `loc1` and `loc2`. These positions must be provided using location targeters.

```
example_condition:
    type: cuboid
    loc1: # Location targeter needed here
        type: custom
        x: 10
        y: 67
        z: -250
    loc2: # Location targeter needed here
        type: custom
        x: 15
        y: 72
        z: -246
    source: false
```

### Check if script target location is close to another location
Checks if the script target location (or source location if `source` is set to true) is less than X blocks away from a center location.

```
example_condition:
    type: distance
    location: # Location targeter needed here
        type: target_location
    max: '10' # 10 blocks away max
    source: false
```

### Check for the script world
Checks if the script is ran in a specific world. You can use multiple world names, separate them using `,`. Warning, world names are highly case sensitive.

```
example_condition:
    type: world
    name: 'world_the_end'
```