---
sidebar_position: 3
---

# 🤔 FAQ
More frequent bugs and issues are documented on **[this MythicLib wiki page](https://gitlab.com/phoenix-dvpmt/mythiclib/-/wikis/Frequent%20Issues)**, please consider checking it as well.

### Is there an installation guide

An installation guide is available [here](install).

### Is MySQL supported?

Yes, you can enable MySQL in the main plugin config file. Look for the following lines: 
```yml title="config.yml"
mysql:
  enabled: false
  host: localhost
  port: 3306
  database: minecraft
  user: mmolover
  pass: ILoveAria
  ....
```

### How do I make it open when I press E?

You can do this using [MythicKeys](https://www.spigotmc.org/resources/mythickeysplugin-custom-keybinds-api.98893/) which requires a client mod. You cannot do this without a client mod as there are **NO** ways (in vanilla Spigot) of checking if a player has his crafting inventory open, as it is all client side. A client mod allows to send the right packets for the server to detect when a player opens his inventory.

This used to be possible under Spigot 1.12 using advancement packets but these were removed in non legacy builds.

What you can you is use another plugin to make the 2x2 crafting grid perform the `/mmoinventory` command when clicked which can be a nice vanilla alternative. Some other alternative is using an item you'd place in some static slot of your inventory that opens the inventory when right clicked (there's an option to do that in the main config file).

### Does MMOInventory have auto-elytra equip?

In recent dev builds, yes!

### Does MMOInventory auto use totems?

No.

### MMOItems placed in their respective slots don't apply their stats.

Make sure the corresponding item type from `MMOItems/item-types.yml` has its subtype/parent set to `ACCESSORY`, which is **mandatory** to have MMOItems register stats from items placed in the custom inventory GUI. If you try equipping a catalyst item in a catalyst slot, you'll suceed but won't get ANY stat because catalysts don't apply their stats when equipping in custom inventory slots! This is a limitation with how MMOItems is made.

Similarily items with non met level restrictions can be equipped but won't apply their stats (unless you are using the `milevel{}` slot restriction).

### Is there a backpack slot, or a mount slot?

No.

### Is there a weapon slot?

No, because this feature gets glitchy really fast with other plugins like MMOItems. It used to be a thing in old inventory plugins such as RPGInventory but we decided not to implement it.

### My GUI looks weird

This issue is no longer relevant as of 1.21.8 as the _scale_ parameter can no longer be used to cover up the vanilla inventory grid pattern. Please refer to [this wiki page](custom-inventory-texture) for more details.

![](https://i.imgur.com/PgtP1Yn.png)

As explained on the main plugin resource page, the default MMOInventory resource pack uses custom textured diamond hoes to display gray filler items to fill in the Minecraft default inventory grid pattern. In order to hide that grid pattern you have to resize your items to approximately 110% but the required percentage can vary sometimes. Edit your resource pack and find the corresponding model which is (by default) located in `/assets/minecraft/models/item/slots/fill.json`.

Using the `scale` json section you can change it to something higher to hide that tiny 1-pixel-wide frame from the inventory grid pattern. Then tweak the `1.1` value so that the grid pattern fully hides. Be careful, if you set it too high the filler items will get past the item slot square.

```json title="assets/minecraft/models/item/slots/fill.json"
{
  "parent": "item/handheld",
  "textures": {
    "layer0": "items/slots/fill"
  },
  "display": {
    "gui": {
      "rotation": [ 0, 0, 0 ],
      "translation": [ 0, 0, 0 ],
      "scale": [ 1.1, 1.1, 1.1 ]
    }
  }
}
```

### Is it compatible with Oraxen, ItemsAdder, Nexo?

MMOInventory is compatible with, and [natively supports](https://gitlab.com/phoenix-dvpmt/mmoinventory/-/wikis/Item%20Plugins#oraxen) Oraxen.

It is **fully compatible with ItemsAdder and Nexo** but does not feature native/built-in support. There is slightly more work to be done with IA to have it work with MMOInventory, namely manually registering fictive items to your custom resource pack in order to register the custom textures used by MMOInv. This process is done automatically when using Oraxen.