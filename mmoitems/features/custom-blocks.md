---

---


# 📦 Custom Blocks
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

## How to upgrade to MMOItems 5.5.5 Custom Blocks

This section will explain how to upgrade custom blocks to MMOItems 5.5.5 correctly.

**[DOWNLOAD NEW RESOURCE PACK HERE](https://drive.google.com/uc?id=1FjV7y-2cn8qzSiktZ2CUXmkdjepXdj5N)**

### Item Type Addition

You will first have to add the new type to item-types.yml. You can either paste this anywhere inside the file or just regenerate it.
**If you do not do this the plugin will not enable and throw a NullPointerException.**
```
BLOCK:
    display: STONE:0
    name: 'Block'
    unident-item:
        name: '&f#prefix#Unidentified Block'
        lore:
            - '&7This item is unidentified. I must'
            - '&7find a way to identify it!'
            - '{tier}'
            - '{tier}&8Item Info:'
            - '{range}&8- &7Lvl Range: &e#range#'
            - '{tier}&8- &7Item Tier: #prefix##tier#'
```

### Custom Block Conversion
_If you are currently using custom blocks the note below applies, if not you can just delete custom-blocks.yml._

Your custom-blocks.yml file should auto generate into item/block.yml. Once it does that it is safe to delete.

### Post Install Notes
**Custom blocks will now behave like regular mmoitems.** This means they will be editable through /mi browse. The blocks should also now be safe to give to players for them to use. This is because they are placed like regular blocks now. If you do allow players to use custom blocks make sure `replace-mushroom-drops` is set to true in the config.yml or else things will be exploitable.

Whenever you make a change with the blocks via the gui the plugin must be reloaded. Either a restart or use of /mi reload.

If you have any issues with the new update make sure to ask on the MythicMobs Discord in the mmo channels.