# Oraxen

Oraxen is a great plugin that handles everything for you when seting up custom textures for items, chat characters or even GUIs. If you've never heard of custom GUI textures, it's a little trick you can use to have cool looking GUIs which **ALL** have different textures.

## Custom textured GUIs in MMOCore
You'll need [Oraxen](https://www.spigotmc.org/resources/%E2%80%8D%E2%9C%85-25-%E2%98%84%EF%B8%8F-oraxen-add-items-blocks-armors-hats-food-furnitures-plants-and-gui.72448/) to setup these GUIs. Simply open up the corresponding GUI config file (located at `/gui/whatever-gui.yml`) and modify the GUI name to whatever you want:
```
# GUI display name
name: '&f%oraxen_shift_16%%oraxen_shift_2%%oraxen_mmocore_attr%'

...

items:
    ......
```

The `%oraxen_<glyph_id>%` placeholder has the effect of overlaping the default GUI texture with the newly configured glyph texture. Using `shift` placeholders you can also correct the small horizontal offsets you might get when using the glyph placeholder alone (try it and see). In under an hour you can setup custom item and GUI textures and have a similar GUI (given that you already have the custom textures):
![O0ISYkr](uploads/74239826d8efc6925442ce09555ffe69/O0ISYkr.gif)