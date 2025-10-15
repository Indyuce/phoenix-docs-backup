---
order: 100
---

# 🔧 Other Features

## Temporary stat modifiers

These commands can be used to temporarily buff/debuff a player's stats. You need to specify a player, a player stat, a stat value, and optionally a modifier duration and a key. The duration is in ticks. These buffs/debuffs can either be flat or relative, _flat_ meaning +10 Atk Damage, _relative_ meaning +10% Atk Damage (write `10%` or even `-10%` for debuffs).

The _key_ is something that you can use to remove your stat modifier later on (if you ever need to remove it).

```
/mythiclib tempstat add <player> <STAT> <value> (ticks) (key)
/mythiclib tempstat add <player> <STAT> <value>% (ticks) (key)
/mythiclib tempstat remove <player> <STAT> (key)
```

## Balancing stats

### Min and max stat values

Minimum and maximum values for the stat values. This means using '0 = 100' for CRITICAL_STRIKE_CHANCE means that you cannot have less than 0% and cannot have more than 100% critical strike chance. This is an important tool for server balance. You can balance stats like block rating, defense, max health, damage reduction etc.

- General format is `{min_value} = {max_value}`
- Using only `= {max_value}` will disable the lower bound.
- Using only `{min_value} =` will disable the upper bound.
- By default there are no upper or lower bounds for most stats. Some of the following are just examples.
- **The minimum value IS NOT A BASE STAT VALUE**. It just means that you cannot have less than X in that stat (it just clamps your stat value up if needed).

```
min-max-values:

  # Crits
  CRITICAL_STRIKE_CHANCE: '0 = 80'
  CRITICAL_STRIKE_POWER: '0 = 500'
  SKILL_CRITICAL_STRIKE_CHANCE: '0 = 80'
  SKILL_CRITICAL_STRIKE_POWER: '0 = 500'

  # Mitigation
  BLOCK_RATING: '0 = 80'
  DODGE_RATING: '0 = 80'
  PARRY_RATING: '0 = 80'
  BLOCK_POWER: '25 = 75'

  BLOCK_COOLDOWN_REDUCTION: '0 = 80'
  DODGE_COOLDOWN_REDUCTION: '0 = 80'
  PARRY_COOLDOWN_REDUCTION: '0 = 80'

  # Other
  MOVEMENT_SPEED: '0 = .3'
  DEFENSE: '0 = 10000'
  SPEED_MALUS_REDUCTION: '0=80'

  # Add as many as you want.
```

### Base stat values

This is where you can edit the base value of any stat. This has the exact same effect as a PERMANENT stat buff. If a MMOCore class gives you 20 base HP, and if the base value in this config section is set to 10, it will result in 20 + 10 = 30 HP. It also works like that with MMOItems items as well.

This is also an important tool for balancing your player stats. Note: If this value is lower than your minimum stat value (see above), it is most likely useless because your stat value will not be buffed.

Default Minecraft stats like Health, Armor, Attack damage.... add up their vanilla base value. If you specify - say 1 Attack Damage -, this 1 will add up to the default player's attack damage which is 1, for a total of 2 Attack Damage when not holding any item.

**Also, these values are completely overwritten by MMOCore base class values. This option only works for stats are not set in MMOCore base stats.**

```
base-stat-value:

  # Crits. By default, crits deal 2x damage
  CRITICAL_STRIKE_POWER: 200
  SKILL_CRITICAL_STRIKE_POWER: 200

  # Mitigation
  BLOCK_POWER: 25

  # Add as many as you want.
```

## Vanilla Damage Modifiers

Change the amount of damage dealt on specific damage sources. This tool comes handy when needing to balance your vanilla damage sources. You can use any math formula for any damage source possible. Available damage sources can be found in [spigot docs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html).

Using `{event_damage}` will return the initial event damage.

```
vanilla-damage-modifiers:
  enabled: false
  source:
    VOID: '%mythiclib_stat_max_health% * .05' # Deals 5% of player's max health
    FIRE: '{event_damage} * 2' # Multiplies by 2 fire damage
    WITHER: '%mythiclib_stat_max_health% * .05'
    LAVA: '%mythiclib_stat_max_health% * .2'
    DROWNING: '%mythiclib_stat_max_health% * .1'
```