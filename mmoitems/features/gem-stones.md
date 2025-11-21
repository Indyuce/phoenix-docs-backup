You can create gem stones using the `GEM_STONE` item type. Gem stones are special items that you can drag & drop onto other items to give them extra stats. The item you're applying the gem on has to have at least one empty gem socket. Item restrictions (perms/class/level) apply on gem stone application just like a regular item.

Moreover, you can give **item type restrictions** to a gem so it can only be applied on a set number of items. This way, if you have, let's say, a gem that is supposed to give extra damage to weapons by sharpening the blade edge, you can make it so it can't be applied onto armors which would not make much sense because why the heck would you try to sharpen an armor.

Gem stones may also apply abilities onto your weapons. _Coming soon: potion & particle effects._

Applying a gem onto another item sometimes fail. If the gem isn't successfully applied, the gem stone will be lost and the item will receive no extra stat. The gem socket will not be used nevertheless.
![](https://i.imgur.com/8SZfLn4.gif)


## Socket Colors

Every gem stone and gem socket has a color. You can only apply a colored gem stone onto a gem socket of the same color. The gem color can be edited using the edition GUI and is NOT displayed on the lore tag _yet_.

You can display the gem color on an item using the `Displayed Type` option. For example, if your gem is a blue gem stone, set the displayed type option to `Blue Gem Stone`. By default, the item type is a red lore tag which is displayed right under the item name. You may also display the gem color using a different material, like a blue diamond for blue gem stones. Last but not least you may also use the item lore (`Can be applied onto blue sockets.`).

The socket names are case sensitive.. if your item has a `Blue` gem socket, make sure your gem stone color is `Blue`.\
![On the gem](https://i.imgur.com/yzPIa5M.png)![On the weapon](https://i.imgur.com/Ll4VfNi.png)

## Uncoloured Sockets
Gems with no gem color can be applied onto any gem socket. Similarly, uncolored gem sockets can receive any gem stone. Gem stones which gem colors are not specified (in the item edition menu) are considered uncolored. To setup an uncolored gem socket, make sure the input socket color is the exact same as the string setup in the main plugin config:
```
gem-sockets:
    # Define the text you need to enter in the
    # item gem sockets if you want to create an
    # uncolored gem socket i.e a socket for any type of gem.
    uncolored: 'Uncolored'
```
![On the item](https://i.imgur.com/csqISPc.png)

If you don't want to utilize the gem color system, simply create items with uncoloured sockets and don't specify a gem color when creating gem stones. Additionally, you may also change the `gem-socket` display in _stats.yml_ so it does not display the gem color whatsoever.

## Removing Gemstones

As of v6.5.7 (Build 709), a way to remove applied gemstones has been introduced. To remove a gemstone from an item, a consumable would have to be created featuring the "Random Unsocket" option. Setting this option to 1 will remove 1 random gemstone from the item. To remove all of the gems off the item, simply set the value to something higher.

![Consumable option](https://i.imgur.com/yWeQMP7.png)

To prevent the consumable from accidentally being eaten instead of applied to the item, enable the `inedible` option:
```
GEMSTONE_REMOVER:
  base:
    material: GRINDSTONE
    random-unsocket: 1.0
    inedible: true
```