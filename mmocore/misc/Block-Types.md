Block types are helpful to determine what happens (item drops, block
regen..) when you [break a block](Mining and Block Regen).



By distinguishing these block types MMOCore can apply different behaviours to them. Using player skulls with custom texture, you can setup small ore blocks which are a great addition for building. Using MI custom blocks you can have blocks with new textures, breaking speed and fully configurable drop tables.

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