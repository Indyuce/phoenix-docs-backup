Using MMOItems 5+ you may implement blocks with a custom texture. You can even them spawn and define how rare they are using [world generation templates](World Generation Templates), configure with what tool it should be broken by players, decide what it loots using MMOItems drop tables and bind a random amount of exp to it.

**[DOWNLOAD REQUIRED RESOURCE PACK HERE](https://www.dropbox.com/s/90w9pvdbfeyxu94/MICustomBlockPack.zip?dl=1)**

## Creating and editing a custom block
You can browse current custom blocks using `/mi browse blocks`. When using the item browser, you may use the small item indicator at the bottom right of the GUI to switch to the Block Browser. Just like with the item browser, you can right click your custom blocks to edit them.

Here is a config template from `blocks.yml`
```
'1':
  base:
    name: '&aMy First Custom Block'
    lore:
    - '&7Wow... It''s possible!'
    - '&7That''s awesome!'
    required-power: 2
    min-xp: 10
    max-xp: 20
    gen-template: basic-template
    material: STONE
    block-id: 1.0
```
`required-power` defines the pickaxe power your tool must have in order to break that block. If it is set to 3, players must use a tool with a `Pickaxe Power` higher than 3. When breaking a custom block, MMOItems rolls a random amount of exp chosen between `min-xp` and `max-xp` and spawns an exp orb on the block just like regular ores.

`gen-template` is the custom block [generation template](World Generation Templates). It defines where this block may spawn and how rare it is.