# 📦 Block Types

Block types are helpful to determine what happens (item drops, block
regen..) when you [break a block](../features/mining.md).

By distinguishing these block types MMOCore can apply different behaviours to them. Using player skulls with custom texture, you can setup small ore blocks which are a great addition for building. Using MI custom blocks you can have blocks with new textures, breaking speed and fully configurable drop tables.

## Available Block Types

The following table provides all block types that are supported by the MMOCore custom mining system.

| Block Type | Description | Example |
|------------|-------------|---------|
| MMOItems Custom Block | When mining a MMOItems custom block.       | `mmoitems{id=6}`                   |
| Player Head     | When mining a player head with a custom texture. | `skull{value="aZd9fE8...48dfQX="}` |
| Noteblock       | When mining a noteblock.                         | `note{note=1;instrument=PIANO}`        |
| Mushroom Block  | When mining a mushroom block.                    | `mushroom{type=MUSHROOM_STEM,faces="NORTH,EAST"}`        |
| Vanilla Block   | When mining any other block. Fallback.           | `vanilla{type=DIAMOND_ORE}`        |

Notes:
- For player heads/skulls with textures, you need to provide the Base64 texture value of the skull, not the texture URL.
- For noteblocks, the note is from 1 to 24. The list of intruments can be found in the [Spigot javadocs](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Instrument.html).
- For mushroom blocks, possible types are `MUSHROOM_STEM`, `RED_MUSHROOM_BLOCK` and `BROWN_MUSHROOM_BLOCK`. Available faces are `UP`, `DOWN`, `NORTH`, `SOUTH`, `EAST`, `WEST`.


Example config
--------------
This is a small part of the default config for the Mining profession.
```
on-mine:
    emerald:
        material: vanilla{type=EMERALD_ORE}
        drop-table:
            items:
            - 'vanilla{type=EMERALD} 1 1-9'
        vanilla-drops: false
        regen:
            time: 2000
            temp-block: skull{value="long_texture_value_here"}
```

This config makes the vanilla emerald ore block drop 1 to 9 emeralds (and cancels vanilla drops), and replace it temporarily (100 seconds = 2.000 ticks) by a custom textured skull. This means you can also use these block types to chose what temporary block should be placed after breaking a specific block.

Extra Options
-------------

You may use the `age` vanilla block type option to spawn back
fully/partially grown crops using block regen. The following example
would spawn back fully grown wheat crops after a wheat block is broken.
`vanilla{type=WHEAT,age=7}`