---
order: 4
---

# 😈 Anticheat Support

MMOCore will automatically hook into anti-cheat plugins and can be configured to disable certain checks when casting skills.<br>

::: info
Only skills made using MythicMobs are supported
:::

The way it works, is by specifying different Anti-Cheat types and disable them for a certain amount of ticks.

## Adding Anti-Cheat to MythicMob skills
(In order to set up MythicMob skills, [go here](Player Skills#binding-mythicmobs-skills-to-mmocore-skills))
To add Anti-Cheat support to your MythicMob skills, simply add `disabled-anti-cheats:` to your skill YML file. (The one in MMOCore)
You can then add 'flags' with a tick value depending on which Anti-Cheat systems you need to disable.

An example of disabling Flying and Clipping for 20 ticks:
```yml
disabled-anti-cheats:
  flying: 20
  clipping: 20
```
An example of disabling Fast Heal for 5 ticks and Critical Hits for 30 ticks.
```yml
disabled-anti-cheats:
  fast_heal: 5
  critical_hits: 30
```

## Available Anti-Cheat Systems
The flag is what needs to be put first, the function is what the cheat is supposed to do. For more information about what each hack does, refer to the Anti-Cheat plugins documentation.

| Flag                | Function                                           |
|---------------------|----------------------------------------------------|
| `general_exploits`  | Uncategorized general hacks                        |
| `no_swing`          | Hitting players/blocks without swinging their hand |
| `movement`          | Extreme jumps, speed hacks, etc.                   |
| `clipping`          | Going through collisions                           |
| `impossible_action` | Self-explanatory                                   |
| `inventory_clear`   | Dropping all your items instantly                  |
| `inventory_clicks`  | Illegal inventory clicking                         |
| `auto_sprint`       | Always sprinting                                   |
| `jesus`             | Walking on water                                   |
| `no_slowdown`       | Preventing the 'Slow' potion effect                |
| `critical_hits`     | Always landing crits                               |
| `nuker`             | Breaking thousands of blocks at once               |
| `ghost_hand`        | Interacting with things through collisions         |
| `liquids`           | Mad placement/draining of liquids                  |
| `block_reach`       | Self-explanatory                                   |
| `elytra`            | Illegal elytra movements                           |
| `boat`              | Illegal boat movements                             |
| `fast_bow`          | Shooting max arrows without charging               |
| `fast_click`        | Reduced cooldown between attacks                   |
| `fast_heal`         | Healing more rapidly than allowed                  |
| `flying`            | WEEEEEEEEEEEEEEEEEEEE                              |
| `hit_reach`         | Self-explanatory                                   |
| `fast_break`        | Breaking blocks instantly                          |
| `fast_place`        | Placing many blocks instantly                      |
| `speed`             | Zoooom!                                            |
| `no_fall`           | Ignore fall damage                                 |
| `illegal_pos`       | Illegal positions                                  |
| `fast_eat`          | Instantly consume foods                            |
| `velocity`          | Applying invalid velocity to the player            |
| `killaura`          | Locked on target                                   |

## Compatible Anti-Cheat Plugins
- [Spartan](https://www.spigotmc.org/resources/spartan-advanced-anti-cheat-hack-blocker.25638/)