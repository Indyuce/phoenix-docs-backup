---
order: 3
---

# 🏷️ Placeholders

All placeholders automatically register upon plugin load, and require **PlaceholderAPI** to work. You do not need to run any commands to initialize the placeholders. Keep in mind you can access PAPI placeholders from MVdWPlaceholderAPI using `{placeholderapi_mmocore_...}`.

If you're looking for a placeholder and you can't see it here, remember MythicLib also comes with its own set of [PAPI placeholders](../../mythiclib/general/placeholders.md).

### Main Placeholders

| **Placeholder** | **Description** |
|-----------------|-----------------|
| `%mmocore_attribute_<attribute>%` | Current value of a [player attribute](Player%20Attributes). |
| `%mmocore_<health/mana/stamina/stellium>%` | Nicely formatted current resource value |
| `%mmocore_<health/mana/stamina/stellium>_bar%` | Nicely formatted current resource value AS A BAR! |
| `%mmocore_max_health%` | Nicely formatted shorthand for `%mythiclib_stat_max_mana%` |
| `%mmocore_stat_<stat_name>%` | Returns the formatted player [stat](Player%20Statistics) value |

### Points

| **Placeholder** | **Description** |
|-----------------|-----------------|
| `%mmocore_skill_points%` | More info on [skill points](Player%20Skills). |
| `%mmocore_class_points%` | More info on [class points](Player%20Classes). |
| `%mmocore_attribute_points%` | More info on [attribute points](Player%20Attributes). |
| `%mmocore_attribute_reallocation_points%` | More info on [attribute points](Player%20Attributes). |
| `%mmocore_attribute_points_spent_<attribute_id>%` | The points spent on a specific attribute. |
| `%mmocore_skill_tree_points_<tree>%` | Unspent skill tree points, for a specific tree. Use `global` for global skill tree points. |

### Class & Professions

| **Placeholder** | **Description** |
|-----------------|-----------------|
| `%mmocore_level%` | Main RPG player level. |
| `%mmocore_level_percent%` | Progression to next level in %. |
| `%mmocore_experience%` | Returns player experience. |
| `%mmocore_next_level%` | Returns player experience needed for next level. Works well beside %mmocore_experience%. |
| `%mmocore_profession_<profession>%` | [Profession](Custom%20Professions) player level. |
| `%mmocore_profession_experience_<profession>%` | Returns player experience for the specific profession. |
| `%mmocore_profession_next_level_<profession>%` | Returns player experience needed for next level for the specific profession. Works well beside %mmocore_experience\_% |
| `%mmocore_profession_percent_<profession>%` | Current progression to next profession level in %. |
| `%mmocore_class%` | Player class name, or name of default class. |
| `%mmocore_class_id%` | Internal name/ID of current player class |
| `%mmocore_mana_icon%` | The mana icon for the players current class |
| `%mmocore_mana_name%` | The mana name for the players current class |
| `%mmocore_exp_multiplier_<profession>%` | Returns the EXP multiplier for the specific profession ("main" may replace the profession name) |
| `%mmocore_exp_boost_<profession>%` | Returns how much of the EXP multiplier is provided by boosters for the specific profession ("main" may replace the profession name) |

### Quests & Objectives

| **Placeholder** | **Description** |
|-----------------|-----------------|
| `%mmocore_quest%` | Ongoing [quest](Quests), or "None". |
| `%mmocore_quest_progress%` | Progress of current quest, or "0" if no quest. |
| `%mmocore_quest_objective%` | Current quest objective, or "None" if no quest. |

### Social

| **Placeholder** | **Description** |
|-----------------|-----------------|
| `%mmocore_guild_name%` | Returns the guild name or '' if none |
| `%mmocore_guild_tag%` | Returns the guild tag or '' if none |
| `%mmocore_guild_leader%` | Returns the guild leader or '' if none |
| `%mmocore_guild_members%` | Returns the guild members or '' if none |
| `%mmocore_guild_online_members%` | Returns the guild online members or '' if none |
| `%mmocore_party_count%` | Counts the number of party members. |
| `%mmocore_party_member_<n>%` | Name of the n-th party member, `None` if invalid |
| `%mmocore_online_friends%` | Number of online friends right now |
| `%mmocore_online_friend_<n>%` | Name of n-th online friend, `None` if invalid |

### Skills

| **Placeholder** | **Description** |
|-----------------|-----------------|
| `%mmocore_skill_level_<skill_name>%` | Returns the level a player has for a specific skill. |
| `%mmocore_skill_parameter_<param_id>:<skill_id>%` | Returns the value of a skill parameter, you can for instance use `mana` or `cooldown` as parameter. |
| `%mmocore_bound_skill_parameter_<param_id>:<slot_number>%` | Returns value of skill parameter, of skill bound to slot with given number. |
| `%mmocore_bound_<slot_idx>%` | Name of skill bound to given skill slot. |
| `%mmocore_id_bound_<slot_idx>%` | UPPERCASE_ID of skill bound to given skill slot. |
| `%mmocore_cooldown_bound_<slot_idx>%` | Returns the remaining cooldown time of the skill in the specific skill slot. |
| `%mmocore_is_casting%` | Returns true if the player is skill casting, false otherwise |
| `%mmocore_passive_bound_<slot_idx>%` | (true/false) Is a passive skill bound to given slot? |
| `%mmocore_cast_slot_offset_<slot_idx>%` | Only when using _skill bar_ skill casting. Returns the keybind the player needs to press in order to cast the skill on the n-th slot |

### Combat

| **Placeholder** | **Description** |
|-----------------|-----------------|
| `%mmocore_in_combat%` | Returns true if the player is in combat, false otherwise |
| `%mmocore_pvp_mode%` | True if the player has enabled PVP mode, false otherwise |
| `%mmocore_since_last_hit%` | Returns time in seconds since last combat hit (or -1 if not in combat). Since MMOCore 1.11.2 snapshots |
| `%mmocore_since_enter_combat%` | Returns time in sec since FIRST combat hit (or -1 if not in combat). Since MMOCore 1.11.2 snapshots |
| `%mmocore_invulnerability_left%` | Time left before being vulnerable (when changing region/using the PvpMode command) |
| `%mythiclib_cooldown_pvpmode%` | Cooldown of `/pvpmode` |

