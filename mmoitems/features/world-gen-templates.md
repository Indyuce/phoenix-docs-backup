# 🌱 Spawning Custom Blocks

_World gen templates_ are used to make your custom blocks spawn in a newly generated world. Custom blocks spawn in veins of a random amount of blocks. They may only spawn in a set list of biomes of worlds. Gen templates do also have more specific options that this wiki page will be overviewing.

**If you want custom blocks to spawn in your worlds, make sure you enable the `custom-blocks.enable-world-gen` option in the main MMOItems config file!**

## Basic gen template example

```yml
basic-template:
  replace: [STONE]
  chunk-chance: 0.7
  depth: -64=255
  vein-size: 5
  vein-count: 2
```

When a world is being generated, every chunk has a set chance to be selected in order to spawn a block (`chunk-chance`). You may also configure the depth at which your block will be placed. The `replace` option defines what vanilla blocks your custom block will replace. That means custom blocks cannot spawn midair so that custom ores can spawn inside stone walls just like vanilla ores.

`vein-count` is the amount of veins that will be generated inside a selected chunk, `vein-size` is the amount of custom blocks that will be generated in every block vein.

## Specific options

Use the `slime-chunk` option so that your block may only spawn in slime chunks.
```yml
template-id:
  slime-chunk: true
```

Use the `bordering` or `not-bordering` options so that your blocks only spawn if specific blocks surrounding the custom block meet their conditions.

```yml
end-debris:
  replace: [END_STONE]
  chunk-chance: 0.4
  depth: 0=255
  vein-size: 2
  vein-count: 20
  bordering:
  - AIR
  worlds:
  - world_the_end
```

In this example, the `end-debris` would only generate if one of the faces is touching air.

## Biome/World black/whitelist

By adding an entry to the `worlds` list, you can restrict any custom block to a specific set of worlds. If you use `!` before the world name, the world whitelist will turn into a blacklist, and the custom block will spawn anywhere but in the specified worlds.

```yml
template-id:
  worlds:
  - world_nether # Just like nether quartz
```

The format is the same for biomes, just use `biomes` instead of `worlds` and input the biomes names ([Spigot javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/Biome.html)).

```yml
template-id:
    biomes:
    - moutains # Just like emerald
```
