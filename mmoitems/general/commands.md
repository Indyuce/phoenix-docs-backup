---
order: 1
---

# 💾 Commands

## Item Commands

| Command  | Usage |
|--------------------------|-------------------|
| ``/mmoitems create <type> <id>`` | Creates a new item with the specified item type and item ID. ID is NOT the display name. |
| ``/mi copy <type> <current-id> <new-id>`` | Copies the item you are holding into a new item with a different ID. Useful if mass producing. |
| ``/mi delete <type> <id>`` | Deletes the specified item. |
| ``/mi edit <type> <id>`` | Opens up the item editor. |
| ``/updateitem`` | Updates the item you are holding. |
| ``/updateitem <type> <id>`` | Turns on the automatic [Item-Updater](Item Updater) for a specific item. It is not totally recommended to leave this on constantly as always updating items may eventually cause lag if you have enough. |
| ``/mi drop <type> <item-id> <world> <x> <y> <x>`` | Generates and drops (essentially spawn in an item without putting it in a player inventory).  |
| ``/mi item identify``| Manually identifies the item you are holding.|
| ``/mi item repair``| Manually repairs the item you are holding.|
| ``/mi item unidentify``  | Manually UNidentifies the item you are holding. |
| ``/mi item deconstruct`` | Manually deconstructs the item you are holding. |
| ``/mi give <type> <item> (player) (min-max) (unident-chance) (drop-chance) (soulbound-chance) (silent)`` | Gives an item to a player  |

## Item Management

| Command  | Usage |
|--------------------------|-------------------|
| ``/mi browse`` | Pulls up an interactable library of ALL of our created items, sorted by item types. (Recommended for most item creation!)|
| ``/mi itemlist <type>`` | Lists all items from a specific item type.  |
| ``/mi allitems`` | Lists all created items, not as useful as /mi browse.|
| ``/mi giveall <type> <item> <min-max> <unident-chance>``| Gives an item to all online players.|

## Crafting Stations

| Command  | Usage |
|--------------------------|-------------------|
| ``/mi stations list`` | Lists all current crafting stations.|
| ``/mi stations open <station> (player)``| This opens the specified station, for the specified player. This is the command you would use to bind stations to blocks.  |

## Miscellaneous

| Command  | Usage |
|--------------------------|-------------------|
| ``/mi ability <ability> (player) (mod1) (val1) (mod2) (val2)`` | Cast an MMOItems ability (works with MM skills as well). There is arguments to select the ability, the player who casts it, and modify the values like damage and cooldown etc.|
| ``/mi heal``  | Similar to essentials/CMI heal, this heals you and removes all negative effects.|
| ``/mi debug info (player)`` | Opens up a useful chat menu with information about the player. This includes stats like class and mana (if applicable). |
| ``/mi list (type/spirit/ability)`` | Shows all available types for weapons,staff spirits, entities etc. |

## General

| Command  | Usage |
|--------------------------|-------------------|
| ``/mmoitems reload``| Reloads the entire plugin, after editing config files. No need to restart your server!  |
| ``/mi reload (adv-recipes/stations)``| Reloads the plugin or reloads the advanced recipes/crafting stations if applicable.  |


## Item Generation


| Command  | Usage |
|--------------------------|-------------------|
| ``/mi generate <player> (extra-args)``  | Check [Obtaining an item](Obtaining an item) for more info |