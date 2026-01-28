---
order: 4
---

# 📚 Variables 

When provided mechanics do not provide enough configurability you can always use variables to recode some more complex script. Variables can be used to store temporary data or even do complex numeric or vector computations for advanced particle effects for instance.

## Internal & Custom Variables

There are two types of variables. First, **internal variables** or **reserved variables** have names which are reserved by MythicLib. They are used all of the time by MythicLib, and you cannot create custom variables with reserved variables names. You can access these variables using `<caster>` or `<target_location>` for instance.

| Variable | Type | Usage |
|----------|------|-------|
| `source` | position | Location where the script was cast |
| `target_location` | position | The target location **if it exists** |
| `caster` | player | Player who cast the script |
| `attack` | attackMetadata | The attack which triggered the skill **if it exists** |
| `stat` | statMap | The stat map of the caster BY THE TIME he cast the script |
| `target` | entity | The skill target **if it exists** |
| `random` | random | An extra module to generate random numbers. See below |

On the other hand, **custom variables** are initialized and can be manipulated by the user. You can access them using `<your_variable_name>`, use them in numeric formulas or just like PAPI placeholders in any mechanic or condition. MythicLib comes with many mechanics that let you initialize and edit your custom variables. The full list is available [here](mechanics/intro.md).

You cannot use a 

## Scopes

Custom variables have **scopes**. This feature is very important since it determines if the variable is specific to the player, if it should be accessible by any player and if it should be saved when a script eventually runs its last mechanic.

Internal variables don't need scopes.

There are three variables scopes available:

- `SERVER` (a server variable is the same for all players and all scripts)
- `PLAYER` (a player variable is the same for all scripts ran by a specific player)
- `SKILL` (the default scope. A skill/script variable will be lost when the script runs its last mechanic).

You only need to provide the scope of your variable when editing or initializing it. When fetching the value of a custom variable using `<var.custom_var_name>`, there might be multiple variables with the same name but different scopes (one per scope, at most). In this case, priority is `SKILL` \> `PLAYER` \> `SERVER` (lowest scopes first).

## Types

Variables are typed: `<source>` is a location (where the script is ran from) whereas `<target>` is an entity (the skill target, if it exists). Variables also have **subvariables**: for instance, you can access the location of an entity using `<entity_variable.location>` which has the effect of transforming an entity variable into a location variable.

A subvariable is also a variable which means you can use multiple dots to access subvariables of subvariables etc. to get the data wanted: `<caster.location.world.name>`

Here is the list of all the currently supported variable types, as well as their subvariables

## Variable types

### AttackMetadata

| Subvariable | Type | Description |
|-------------|------|-------------|
| `damage` | double | Amount of damage being dealt |
| `damage_<type>` | double | Amount of damage being dealt, with given damage type |

### AttributeMap

This is useful if you want to access some player's vanila attribute values. Example use: `<caster.attribute.max_health>`.

Vanilla attributes shall not be mistaken for player stats which are added by the MMO plugins. Some of these stats are based on vanilla attributes, but not all of them. For instance, weapon crit chance is a custom stat which isn't based on any vanilla attribute so you can't access it using this variable type. You'll need to use the `statMap` variable type: `<caster.stat.critical_strike_chance>`. However since attack damage is based on a vanilla attribute, `<caster.stat.attack_damage>` will NOT return the correct value, because it only takes into account stat modifiers registered in MythicLib and not external attribute modifiers!

| Subvariable | Type | Description |
|-------------|------|-------------|
| `max_health` | double | // |
| `follow_range` | double | // |
| `knockback_resistance` | double | // |
| `movement_speed` | double | // |
| `flying_speed` | double | // |
| `attack_damage` | double | // |
| `attack_knockback` | double | // |
| `attack_speed` | double | // |
| `armor` | double | // |
| `armor_toughness` | double | // |
| `luck` | double | // |
| `armor_toughness` | double | // |

### CooldownMap

Cooldown maps are used to store a player's cooldown values. Cooldowns are used by MythicLib for damage mitigation (block, parrying, dodging) and for skill cooldowns, and by MMOItems for item cooldowns. You can access the cooldown map of the player casting the script using `<caster.cooldown>`.

Using subvariable `some_key` will return a double corresponding to the remaining cooldown for the given cooldown key. For instance, `<caster.cooldown.mmoitem_small_mana_pot>` returns the remaining cooldown for the MMOItem with ID `SMALL_MANA_POT`, `<caster.cooldown.hello>` returns the remaining cooldown for the skill/item/etc. with cooldown key `hello`.

The following table lists all the keys used by MMOCore and MMOItems. You can use virtually any cooldown key inside your scripts or plugins, you can also mess/interfere with the cooldown keys used internally by MMOItems and MMOCore if you want to.

::: info
You can also use `%mythiclib_cooldown_<cooldown_key>%` to retrieve the player's current cooldown using placeholders from PlaceholderAPI. Example: `%mythiclib_cooldown_skill_fireball%`
:::

| Subvariable | Type | Description |
|-------------|------|-------------|
| `mmoitem_<lower_case_item_id>` | double | Remaining item cooldown or 0 |
| `<cooldown_reference>` | double | If the MMOItem has a cooldown reference, use it instead of the above. |
| `skill_<lower_case_skill_id>` | double | Remaining skill cooldown or 0 |
| `dodge` | double | Remaining dodging cooldown or 0 |
| `parry` | double | Remaining parrying cooldown or 0 |
| `block` | double | Remaining dodge cooldown or 0 |
| `weapon_crit` | double | Remaining weapon crit strike cooldown or 0 |
| `skill_crit` | double | Remaining skill crit strike cooldown or 0 |

### Double

Numeric value.

| Subvariable | Type | Description |
|-------------|------|-------------|
| `int` | integer | The whole part of that number |
| `round.xxx` | string | Round the double up to N decimal places |

### Entity

Any entity that **is NOT a player**. Players share many subvariables with the Entity variable type but have a few extra properties.

| Subvariable | Type | Description |
|-------------|------|-------------|
| `id` | integer | The entity id |
| `uuid` | string | The entity UUID |
| `type` | string | The entity type (ZOMBIE, GHAST etc. [full list](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html)) |
| `location` | position | The entity current loc |
| `bb_center` | position | The center position of that entity given its bounding box |
| `eye_location` | position | The position of the eyes of the entity |
| `health` | double | The current entity health bar |
| `looking` | position | A vector pointing towards where the entity is looking |
| `velocity` | position | The instantaneous entity velocity |
| `height` | double | The entity height |
| `attribute` | attributeMap | The entity attribute map |
| `fire_ticks` | int | The amount of ticks during which the entity will be on fire (0 if not on fire) |

### Integer

A round number. No subvariables!

### Player

A player entity. Players share many subvariables with the Entity variable type but have a few extra properties.

| Subvariable | Type | Description |
|-------------|------|-------------|
| \--- | \--- | Any from the Entity variable type |
| `stat` | statMap | The player's stat map |
| `cooldown` | cooldownMap | The player's cooldown map |
| `name` | string | The player name |

### Position

Positions/locations/vectors are all _pretty much_ synonyms. A position is defined by a world + three coordinates (X, Y and Z). Positions are both used to describe player location (in that case you are using the `world` subvariable) and to make vector computation (the `world` subvariable is therefore useless).

| Subvariable | Type | Description |
|-------------|------|-------------|
| `world` | world | Position world |
| `x` | double | X coordinate |
| `y` | double | Y coordinate |
| `z` | double | Z coordinate |
| `length` | double | Vector length computation |
| `biome` | string | Biome name |
| `altitude` | double | Computes altitude of position |

### StatMap

Stat maps are used to store all the stat modifiers from a specific player. You can access the script runner's stat map using `<caster.stat>`. Then retrieve the stat value using `<caster.stat.skill_critical_strike_chance>` for instance.

Vanilla attributes shall not be mistaken for player stats which are added by the MMO plugins. Some of these stats are based on vanilla attributes, but not all of them. For instance, weapon crit chance is a custom stat which isn't based on any vanilla attribute so you can't access it using this variable type. You'll need to use the `statMap` variable type: `<caster.stat.critical_strike_chance>`. However since attack damage is based on a vanilla attribute, `<caster.stat.attack_damage>` will NOT return the correct value, because it only takes into account stat modifiers registered in MythicLib and not external attribute modifiers!

### String

| Subvariable | Type | Description |
|-------------|------|-------------|
| `uppercase` | string | Same string in upper case |
| `lowercase` | double | Same string in lower case |

### Random

| Subvariable | Type | Description |
|-------------|------|-------------|
| `uniform` | double | Decimal number sampled uniformly between 0 and 1 |
| `int` | int | A random integer|
| `bool` | boolean | A random boolean (true or false), uniformly |
| `gaussian` | double | Decimal number sampled from a standard gaussian distribution |

### World

| Subvariable | Type | Description |
|-------------|------|-------------|
| `time` | int | Current time in the world |
| `name` | string | World name |

