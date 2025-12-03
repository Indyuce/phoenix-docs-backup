# 🔨 Custom Durability

::: tip
Since 1.20.6 Minecraft has introduced a tag to edit the maximum vanilla durability of items. We recommend users to use this over custom durability!
:::

Custom durability is a really powerful system that allows you to create items with a set amount of uses, unlike the \<1.20.5 vanilla durability system which forces you to always have the same max amount of uses for a type of item.

All items feature the _Max Custom Durability_ stat, which defines how many times an item can be used before either **breaking** or **becoming unusable**. The _Lost when Broken_ item option defines whether or not the item should be lost when reaching 0 durability.

Durability is displayed on the item vanilla durability bar, however you may also display the player's held item durability using PAPI placeholders. Items can be repaired only using repairing consumables.

## 1.20.5+ Durability

Minecraft 1.20.5 introduced a new item tag which allows you to modify an item's maximum vanilla durability. This tag is fully supported by recent MMOItems builds. We encourage users to switch to this system as the primary reason why MMOItems introduced custom durability was the impossibility to change an item's maximum durability. Now that this has been changed, you no longer need MMOItems custom durability.

This does not fix the issue of having items which cannot have a durability bar at all, like apples, blocks and most items. An easy workaround is to use a breakable tool like a pickaxe or a shovel and change its texture using a resource pack if you really need a durability bar.

**We encourage users moving to vanilla durability as it is generally better for compatibility with external plugin features, and because MMOItems fully supports it.**

## Durability Placeholders

This cannot be used in the item lore! These are placeholders that can be used in scoreboards, GUIs or anything else that supports PlaceholderAPI.

* **%mmoitems_durability%** returns the amount of uses left of the item the player is holding.
* **%mmoitems_durability_max%** returns the item max durability.\
  ![](https://i.imgur.com/TaumARR.png)
* **%mmoitems_durability_ratio%** returns the item's durability ratio (from 0% to 100%).\
  ![](https://i.imgur.com/90KnpS2.png)
* **%mmoitems_durability_bar_square%** returns the item durability as a progress bar.\
  ![](https://i.imgur.com/HmS1wFR.png)
* **%mmoitems_durability_bar_diamond%** returns the durability bar, but the char used is a diamond.\
  ![](https://i.imgur.com/QPrLKtj.png)
* **%mmoitems_durability_bar_thin%** returns a much thiner durability bar.\
  ![](https://i.imgur.com/MJvhd6S.png)

## Durability in item lore

You can also display the item durability in the item lore. First, add the following line to your `lore-format.yml` config file if it's not already there:

```yml
lore-format:
  # ...
  - '#durability#'
```

The following line in `stats.yml` can be edited to change how custom durability is displayed in the item lore. Add it to the file if it's not already there:
```yml
durability: '&7Durability: {current} / {max}'
```

![](https://i.imgur.com/InWJLD4.png)