# 🎨 Item Textures

## 1.20+

::: info
Under construction
:::

## 1.14+

In Minecraft 1.14, texture by durability still works but it is outdated. MC 1.14 introduces a new item NBTTag called _CustomModelData_ which lets an item have a custom texture without using its durability. This tag is much better than the 1.9 system since it allows you to have custom textured items while keeping their durability bar.

Once again MI does not provide anything to setup the required resource pack, moreover you can find tutorials online on how to setup it. Once your resource pack is setup, head to MC and open the edition GUI for the item which you want to give a texture to. If you're running a 1.14 server, a new item option called _Custom Model Data_ should display in the menu. Simply input the desired integer which corresponds to the texture you setup in your resource pack. Your item should then load the texture.

## From 1.9 to 1.13 (outdated)

Since 1.9 items can have **different textures or models** depending on their durability. MMOItems supports these custom textures however it does not help you setting up the resource pack you need for these custom textures. Using the 1.9 _texture by durability_ feature, two items with the same item material can have different textures based on the item durability values.

It is almost necessary to read [**that guide**](https://www.spigotmc.org/wiki/custom-item-models-in-1-9-and-up/) on custom textures first (you don't have to read the **CODE** part).

Once you read the tutorial, create an item in-game in MMOItems to get started. Make your item _unbreakable_ (it is very important) using the corresponding item option and give your item the durability that corresponds to the one you set in your resource pack. Your item should now load the custom texture you created. If your item is not unbreakable, the texture will either not load or will be lost once you use one durability point from your item.
