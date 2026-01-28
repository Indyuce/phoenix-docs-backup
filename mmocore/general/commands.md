---
order: 1
---

# 💾 Commands

Below is a list of all available commands in MMOCore. You can also explore these in-game as tab-completion is fully supported.

| Command | Usage |
|--|--|
| `/mmocore` | Displays the main help page. |
| `/mmocore reload` | Reloads the entire plugin, after editing config files. No need to restart your server! |

### Currency
| Command | Usage |
|--|--|
| `/mmocore note` | Gives players a note worth $X. Can be [deposited](../misc/economy.md) into banks. |
| `/mmocore coins` | Gives players gold coins based on the amount input. Can be deposited into banks. |

### Quests
| Command | Usage |
|--|--|
| `/mmocore quest start` | Force start a quest for a player. |
| `/mmocore quest cancel` | Force cancel a player's current quest. |

### Waypoints
| Command | Usage |
|--|--|
| `/mmocore waypoints unlock` | Manually unlocks a waypoint for a set player. |
| `/mmocore waypoints lock` | Manually locks a waypoint for a set player. |
| `/mmocore waypoints teleport` | Manually teleports a player to a set waypoint. |
| `/mmocore waypoints open` | Opens the waypoint menu AND checks if a player is standing on a waypoint |

### Admin
| Command | Usage |
|--|--|
| `/mmocore admin exportdata` | Exports all the existing player data from the yml files to the sql database. So you can can then change you data storage to SQL while keeping all your player data. |
| `/mmocore admin attr-realloc-points <give/set>` | Manually gives attribute reallocation points to a player. |
| `/mmocore admin attribute-points <give/set>` | Manually gives attribute points to a player. |
| `/mmocore admin attribute <give/take>` | Increases a player's attribute |
| `/mmocore admin force-class` | Sets a player's class by force. This means their level, skills, etc. won't update as well. Make sure your classes have the same skills/skill-trees if you plan on using this command. |
| `/mmocore admin class-points` | Gives [class points](../features/classes.md#class-points) to a player. |
| `/mmocore admin exp give <player> <profession/main> <value>` | Gives profession/class experience to a player. |
| `/mmocore admin exp set <player> <profession/main> <value>` | Sets the profession/class exp of a player. |
| `/mmocore admin exp take <player> <profession/main> <value>` | Take off class/profesion exp from a player. |
| `/mmocore admin hideab <player> <ticks>` | Hides the action bar for a player for X ticks. |
| `/mmocore admin info` | See summary of levels for a player. |
| `/mmocore admin level <profession/main>` | Same parameters as the EXP command, gives X levels. |
| `/mmocore admin nocd` | Used by admins to test skills without beign affected by skill cooldown or mana usage. |
| `/mmocore admin reset <player>` | HARD RESETS a player's info i.e class, level, EXP... |
| `/mmocore admin resource-health <give/set/take>` | Modify a player's health. |
| `/mmocore admin resource-mana <give/set/take>` | Modify a player's mana. |
| `/mmocore admin resource-stamina <give/set/take>` | Modify a player's stamina. |
| `/mmocore admin resource-stellium <give/set/take>` | Modify a player's stellium. |
| `/mmocore admin skill-points <give/set>` | Gives [skill points](../skills/intro.md#upgrading-a-skill) to a player so they can upgrade their skills. |
| `/mmocore admin skill-realloc-points <give/set>` | Gives skill reallocation points to a player. |
| `/mmocore admin skill <give/set>` | Gives points directly to a skill for a player. |
| `/mmocore admin skill <lock/unlock>` | Locks/unlocks a [skill](../skills/intro.md#unlocking-skills) for a certain player. |
| `/mmocore admin slot <lock/unlock>` | Locks/unlock a [slot](../features/classes.md#skill-slots) for a player. |
| `/mmocore admin slot bind <slot> <skill>` | Binds a skill to a certain slot. This will work even if the designated skill is not unlocked for the player but won't unlock it.  |
| `/mmocore admin slot unbind <slot>`  | Unbinds a skill from a certain slot. |

### Classes
| `/mmocore class force <player> <class>` | Forcefully sets a player's class without loading class data |
| `/mmocore class select <player> <class>` | Sets the player's class and loads their class data |
| `/mmocore class check <player>` | Prints the current class of a player |

### EXP Boosts
| Command | Usage |
|--|--|
| `/mmocore booster create <profession/main> (player)` | Creates an [EXP booster](../level/boosters.md) with specified power and length. |
| `/mmocore booster list` | Displays active EXP boosters. |
| `/mmocore booster remove` | Removes a booster with specified ID. |
