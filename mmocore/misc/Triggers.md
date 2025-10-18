**This is a very technical feature, you will not learn anything by reading this page on its own (out of context). It should only be read if other wiki pages redirect you to this page.**

Triggers are used by MMOCore to execute actions when certain conditions are met. They are used for both quests and professions, and each has a set of actions or objectives that can "trigger" them.

### Trigger Tables (Since 1.9.5)

Since 1.9.5, you can define trigger tables in `triggers.yml`. You can reference each trigger list with its id which will fire all the corresponding triggers.

```
#Example
test-trigger:
 - 'command{format="broadcast Triggered!"}'
 #Will fire the 2 commands in test-trigger-2
 - 'from{source="test-trigger-2"}'


test-trigger-2:
 - 'command{format="mmocore admin skill-points give %player_name% 1"}'
 - 'command{format="mmocore admin atr-realloc-points give %player_name% 3"}'
```

## Available Trigger Types

| Trigger | Description | Format/Example |
|---------|-------------|----------------|
| stat | Gives a permanent stat to the player. FLAT type just adds the amount to the stat. Relative makes it have a % increase for the stat. | `stat{stat=<STAT_NAME>;amount=<amount>;type=FLAT/RELATIVE}` |
| skill_buff | Gives a permanent buff for all the skills matching the formula by changing the value of a certain modifier (cooldown, damage, mana...). More info on skill buffs [here](https://gitlab.com/phoenix-dvpmt/mmocore/-/wikis/Player%20Skills#skill-buffs). | `skill_buff{formula="<FORMULA>";modifier=<MODIFIER>;amount=<amount>;type=FLAT/RELATIVE}` |
| unlock_skill | Unlocks a skill for the player. More about skill unlocking [here](https://gitlab.com/phoenix-dvpmt/mmocore/-/wikis/Player%20Skills#skill-unlocking). | `unlock_skill{skill=FIREBALL}` |
| unlock_slot | Unlocks a specific [skill slot](https://gitlab.com/phoenix-dvpmt/mmocore/-/wikis/Player%20Classes#skill-slots-since-1120) for the player. | `unlock_slot{slot="<SLOT>"}` |
| bind_skill | Binds a skill to a specific slot. | `bind_skill{skill=FIREBALL;slot=10}` |
| levelup_skill | Increases the player's skill level. | `levelup_skill{skill=<NAME>;amount=1}` |
| message | Sends a message to the player. | `message{format="&aYour message here... "}` |
| command | Makes the console perform a command. | `command{format="tellraw @a {"text":"Hello!"}"}` |
| experience | Gives experience in a profession. | `exp{profession=<PROFESSION>;amount=<AMOUNT>}` |
| experience | Gives main class experience. | `exp{amount=<AMOUNT>}` |
| sound | Broadcasts a sound to the player. | `sound{sound=<SOUND_NAME>;volume=<VOLUME>;pitch=<PITCH>}` |
| item | Gives an item to the player. | `item{type=DIAMOND;amount=3}` |
| mmoitem | Gives an mmoitem to the player. | `mmoitem{type=SWORD;id=FALCON_BLADE;amount=2}` |
| mana | Give/take/set player mana. | `mana{operation=<GIVE/SET/TAKE>;amount=2-3}` |
| stamina | Give/take/set player stamina. | `stamina{operation=<GIVE/SET/TAKE>;amount=2-3}` |
| stellium | Give/take set player stellium. | `stellium{operation=<GIVE/SET/TAKE>;amount=2-3}` |
| mmskill | Cast a MythicMobs skill. | `mmskill{id=MythicMobsSkillInternalName}` |
| money | Give/take/set player balance. | `money{operation=<GIVE/SET/TAKE>;amount=2-3}` |

Most of these types and triggers are shown in the default config with how to properly use them. The message and command triggers support placeholders from [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/).