This page will explain how to upgrade custom blocks to MMOItems 5.5.5 correctly.

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