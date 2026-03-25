---
order: 4
---


# 💪 Player Stats

Player statistics are essential in MMOCore. They can be granted by classes, attributes, party buffs, temporary skills, items... For better compatibility, MMOItems shares its stat system with MMOCore, so any stat that can be found in MMOItems can be used inside of MMOCore.

## Stats handled with vanilla attribute modifiers

| Stat name | Description |
|-----------|-------------|
| `attack_damage` | Damage dealt by melee attacks |
| `attack_speed` | The player's speed of attacks |
| `max_health` | Max health of the player |
| `movement_speed` | Player's walking speed |
| `knockback_resistance` | Chance of negating knockback (vanilla player attribute) from 0 to 1 |
| `armor` | Reduces damage taken, vanilla player attribute |
| `armor_toughness` | Vanilla armor toughness, reduces damage taken (see MC wiki) |

The default player movement speed is set to 0.1 which is 4.317m/s according to the Minecraft wiki. Since one block measures 1m^3, the formula for the player move speed is `<attribute_value> * 43.17 m/s`.

### Minecraft 1.20.2+

| Stat name | Description |
|-----------|-------------|
| `max_absorption` | Maximum amount of absorption hearts |

### Minecraft 1.20.5+

| Stat name | Description |
|-----------|-------------|
| `block_break_speed` | Player's block breaking speed |
| `block_interaction_range` | How far the player can break or interact with blocks |
| `entity_interaction_range` | How far the player can hit or interact with entities |
| `fall_damage_multiplier` | Increases/decreases fall damage |
| `gravity` | How strong gravity is |
| `jump_strength` | How high the player can jump (basically Jump Boost) |
| `safe_fall_distance` | How high the player can fall from without taking fall damage |
| `scale` | How big the player is (increases player's size and offsets camera location) |
| `step_height` | How many blocks the player can climb when walking without having to jump |

### Minecraft 1.21+

| Stat name | Description |
|-----------|-------------|
| `burning_time` | Amount of time how long an entity remains on fire after being ignited as a multiplier. |
| `explosion_knockback_resistance` | Resistance to knockback due to explosions. |
| `mining_efficiency` | Factor for increasing/reducing mining speed |
| `movement_efficiency` | Movement speed factor when walking on blocks that slow down movement. |
| `oxygen_bonus` | Determines the chance not to use up air when underwater. |
| `sneaking_speed` | Movement speed when sneaking. |
| `submerged_mining_speed` | Mining speed factor when submerged. |
| `sweeping_damage_ratio` | Percentage of damage transferred by sweep attacks. |
| `water_movement_efficiency` | Movement speed factor when submerged. |

## Resources

| Stat name | Description |
|-----------|-------------|
| `max_mana` | Maximum mana the player may have. |
| `max_stamina` | Maximum stamina the player may have. |
| `max_stellium` | Stellium is a resource used to travel using waypoints. |
| `health_regeneration` | Health [regeneration](../features/combat.md) in pts/sec. |
| `mana_regeneration` | Mana regen in pts/sec |
| `stamina_regeneration` | Stamina regen in pts/sec |
| `stellium_regeneration` | Stellium regen in pts/sec |
| `max_health_regeneration` | Health regen in % of max health/sec |
| `max_mana_regeneration` | Mana regen in % of max mana/sec |
| `max_stamina_regeneration` | Stamina regen in % of max stamina/sec |
| `max_stellium_regeneration` | Stellium regen in % of max stellium/sec |

## Utility

| Stat name | Description |
|-----------|-------------|
| `additional_experience` | Extra experience the player earns. |
| `cooldown_reduction` | Reduces skills cooldowns by a specific % |
| `speed_malus_reduction` | Reduces (in %) slow debuffs. |
| `luck` | Greater chance to have rare items in loot chest and with fishing drop tables. An item with a drop chance of 1% will in truth, have drop chance of 10% with 100 LUCK. |

Speed malus reduction doesn't directly increase the player's movement speed. It decrease by a certain amount speed debuffs like debuffs due to MMOItems. By registering a negative movement speed buff on MMOItems, you can create the feeling that items are heavy and reduce the player's move speed when worn/held. Speed malus reduction reduces such slow debuffs.

## Critical Strikes

| Stat name | Description |
|-----------|-------------|
| `critical_strike_chance` | Chance to deal crits with weapons. |
| `critical_strike_power` | Extra damage dealt by weapon crits. |
| `skill_critical_strike_chance` | Chance to deal crits with skills. |
| `skill_critical_strike_power` | Extra damage dealt by skill crits. |

## Damage Stats

The following stats are damage multiplier _e.g_ when set to 50, specified attack damage is increased by 50%.

| Stat name | Description |
|-----------|-------------|
| `magic_damage` | Additional magical skill damage. |
| `physical_damage` | Additional physical skill/weapon damage. |
| `projectile_damage` | Additional projectile based weapon & skill damage. |
| `weapon_damage` | Additional weapon based attack damage. |
| `skill_damage` | Additional skill (magical/physical) damage. |
| `undead_damage` | Additional damage against undead creatures. |
| `pvp_damage` | Additional damage against players. |
| `pve_damage` | Additional damage against anything but players. |

