---
order: 4
---

# 💪 Player Stats

MMOItems and MMOCore share the same stat system. Any stat that you gain through an MMOItems item, MMOCore class, or item placed inside a MMOInventory inventory, will propagate to all MMO plugins.

## Temporary Stats

Temporary stats, or _stat modifiers_, are stats boosts/debuffs that are given to players for a limited/unlimited amount of time. In either way, these stats are removed when the server restarts.

### Using a script

Note that you can give temporary stats to players using the `add_stat` script mechanic. You will find more information on [this wiki page](../scripts/mechanics/buffs.md#add-temporary-stats). These stats will be removed when the server restarts.

### Using commands

The easiest way to provide temporary stats to players is through commands.
```plaintext
/ml stat add <player> <stat> <amount> (duration) (key) (unique)
/ml stat remove <player> <stat> <key>
/ml stat clear <player> <key>
```

Using the `add` subcommand, you can provide a stat modifier to a player.
- If you provide a duration through the `duration` parameter (in ticks), the stat will be temporary and removed after that time.
- If you provide a `key`,  you can later remove this stat modifier using the `remove` subcommand. If you do not provide any, it will use the default key `default`.
- If you set `unique` to true, only one modifier with the same key will be active at a time; adding a new one will replace the previous one. This is useful for buffs that you want to refresh periodically.

::: tip Example
The following command provides a flat +10 Attack Damage stat to the player `Notch` for 5 seconds (100 ticks), using the key `my_custom_buff`. If you execute the same command again, it will not override the previous one since `unique` is set to false, and it will stack with itself.
```plaintext
/ml stat add Notch ATTACK_DAMAGE 10 100 my_custom_buff false
```
:::

Using the `remove` subcommand, you can remove a specific stat modifier from a player using its `key`.

::: tip Example
The following command unregisters the stat modifier given in the previous example.
```plaintext
/ml stat remove Notch ATTACK_DAMAGE my_custom_buff
```
:::

Using the `clear` subcommand, you can remove all stat modifiers with the associated `key` from a player.

::: tip Example
The following command removes all stat modifiers with the key `my_custom_buff` from the player `Notch`.
```plaintext
/ml stat clear Notch my_custom_buff
```
:::

## Min/Max Stat Values

Minimum and maximum values for the stat values. This means using '0 = 100' for CRITICAL_STRIKE_CHANCE means that you cannot have less than 0% and cannot have more than 100% critical strike chance. This is an important tool for server balance. You can balance stats like block rating, defense, max health, damage reduction etc.

- General format is `{min_value} = {max_value}`
- Using only `= {max_value}` will disable the lower bound.
- Using only `{min_value} =` will disable the upper bound.
- By default there are no upper or lower bounds for most stats. Some of the following are just examples.
- **The minimum value IS NOT A BASE STAT VALUE**. It just means that you cannot have less than X in that stat (it just clamps your stat value up if needed).

You will find the following code snippet inside the `MythicLib/stats.yml` config file.

```yml
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

## Base Stat Values

This is where you can edit the base value of any stat. This has the exact same effect as a PERMANENT stat buff. If a MMOCore class gives you 20 base HP, and if the base value in this config section is set to 10, it will result in 20 + 10 = 30 HP. It also works like that with MMOItems items as well.

This is also an important tool for balancing your player stats. Note: If this value is lower than your minimum stat value (see above), it is most likely useless because your stat value will not be buffed.

Default Minecraft stats like Health, Armor, Attack damage.... add up their vanilla base value. If you specify - say 1 Attack Damage -, this 1 will add up to the default player's attack damage which is 1, for a total of 2 Attack Damage when not holding any item.

**Also, these values are completely overwritten by MMOCore base class values. This option only works for stats are not set in MMOCore base stats.**

```yml
base-stat-value:

  # Crits. By default, crits deal 2x damage
  CRITICAL_STRIKE_POWER: 200
  SKILL_CRITICAL_STRIKE_POWER: 200

  # Mitigation
  BLOCK_POWER: 25

  # Add as many as you want.
```
