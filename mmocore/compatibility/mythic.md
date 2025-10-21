---
order: 2
---

# 🧌 MythicMobs

Most of our mob features and custom drops tie into MythicMobs, the best mob creation plugin. Also **one of the most important features**, in order to create your own skills through MMOCore, you will utilize MythicMobs to make any skill you want. More info [here](Player%20Skills#binding-mythicmobs-skills-to-mmocore-skills).

MythicMobs also adds more options to the quest system: you can setup quests where players must kill X mobs from MythicMobs, more info [here](Quests).

Players may also earn main-class experience when killing mobs from MythicMobs, more info on that [wiki page](Custom%20Professions).

## MythicMobs drop items

MMOCore adds new drop item types to MythicMobs drop tables, here is the list:

| Drop Item | Usage | Description |
|-----------|-------|-------------|
| Gold Pouch | `gold_pouch{min=10;max=100}` | Gold pouch containing a random amount of $$ between MIN and MAX |
| Gold Coin | `gold_coin{}` | Drops a gold coin worth $1 |
| Note | `note{minw=20;maxw=30}` | Drops a note with random value. |

## Gold Pouches

Gold pouches are leather pieces you can right click in order to open a 2-rows GUI which contains randomly generated gold coins and notes. Players cannot place any item in there, they may only take items from it if they have some space left in their inventory. Pouches **are taken off the player inventory** when fully emptied.
![pp](uploads/e5fa3197fe924597eb61ad457c1f57ca/pp.gif)