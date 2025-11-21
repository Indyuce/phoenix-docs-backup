Most of the Item Updater has been replaced by the [Revision ID System](Revision-ID-System).  
Some of these commands may still work, however,  
**This page is outdated and information here may not be 100% accurate**  
- - -
Once items are generated using drop tables or the give command, they become independant of the /item config. Therefore the only way to directly update items in the player's inventories is to use the **Item Updater**. You can either directly update the item you are holding using **/updateitem**, or enable the item updater for a specific item using `/updateitem <type> <id>`.

### Updating physical items
Once the item updater is enabled for a specific item, every physical instance of that item is considered _outdated_ and will be updated. An outdated item can only be updated **once** (performance save) when enabling the item updater, unless you apply further changes to the item. Every change you apply in the item edition GUI will make physical item instances _outdated_ again till they are updated.

MMOItems updates every item in the players inventories whenever they log in. Furthermore any item clicked in a non-creative inventory undergoes an update check.

### Enabling the updater for every item
If you do not want to worry about players having outdated items here and there on your server, you might want to enable the item updater for every item in the plugin. **This is possible however strongly not recommended.**\
The item updater was designed to hot-nerf items in players' inventories once they have been generated. It is not designed to mass-update every item on your server. The more items you have, the higher the performance the plugin will need in order to keep them updated.

The item updater is **100% useless** for items which have not been changed after they are generated. In order to save performance, MI first checks if a physical item has some non-applied item change, and then updates the item if it is considered outdated. Enabling the item updater for all of your items generates useless update checks.

You can manually enable the item updater for every item in your server using the following command: `/mi update apply 2 2`. This loops through every item in your config files and registers them in the item updater list.