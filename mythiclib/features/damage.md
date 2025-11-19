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