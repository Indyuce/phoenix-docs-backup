---
order: 4
---

# ⚔️ Offense

## Deal damage to an entity

Deals damage to the entity provided. This applies on-hit effects, crit strikes, damage mitigation... (fully compatible with MMOItems and MMOCore). 

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| amount   | amt, a, damage, dmg, d, value, val, v      | The amount of damage to deal. | - |
| knockback   | kb, knock      | If true, applies knockback to the target. | true |
| ignore_immunity   | ii      | If true, ignores the target's invulnerability frames. | false |
| damage_type   | dtype, dt      | The damage type(s) to deal. Separate damage types with commas and no spaces. See available damage types [here](../../features/damage.md). | magic,skill |
| element  | -      | The element name to deal damage with. See available elements [here](../../features/elements.md) | none |
| target  | -      | The target entity or entities to deal damage to. | target or caster |

```yml
example_script:
  mechanics:
  - 'damage{amount="100 * (1 + <modifier.extra> / 100)";dtype="PHYSICAL,WEAPON";kb=true;ii=false;element=FIRE;target={type=nearby_entities;radius=3}}'
```

## Multiply the current attack damage

Multiplies the current attack damage by a given amount.

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| value   | val, v, amount, amt, a, scalar, s, coef, c       | The amount to multiply the damage by. Can be an expression. | - |
| damage_type   | dtype, dt      | The damage type to modify. See available damage types [here](../../features/damage.md) | none |
| additive  |  -      | If true, this damage buff will stack additively with other additive buffs. | false |
| element  | -      | The element name to modify. See available elements [here](../../features/elements.md) | none |

If no damage type is provided the entire attack damage is modified. Otherwise only the specific portion of the attack due to the given damage type is affected. If an element name is provided, only damage due to that specific element will be affected.

You cannot provide both an element and a damage type. When providing an element name, the damage type parameter is ignored.

If `additive` is set to `true`, this damage buff will stack with stats like PvE damage, Undead Damage (which stacks additively i.e `10% + 10% <=> +20%`). Otherwise, buffs stack up geometrically i.e `110% * 110% = 121% <=> +21%`.
```yml
example_script:
  mechanics:
  - 'multiply_damage{amount="1 + <modifier.extra> / 100";damage_type=PHYSICAL;element=FIRE;additive=false}
```

## Apply potion effect

Gives a potion effect to the target entity, for a given duration, with given level. Potion effect names are available on the [Spigot javadocs](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html).

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| effect   | eff, e, type, pe | Name of potion effect to take off | - |
| duration   |  dur, d, ticks, t, time     | Duration of potion effect in ticks | - |
| level  | lvl, l      | Level of potion effect (0 = level 1, 1 = level 2, etc.) | 0 |
| ambient  | amb      | If true, the potion effect will be ambient. | false |
| particles  | part      | If false, the potion effect will have no particles. | true |
| icon  | ic      | If false, the potion effect will have no icon. | true |
| target  | -      | The target entity to set on fire. | target or caster |

```yml
example_script:
  mechanics:
  - 'potion{type=INCREASE_DAMAGE;level=5;duration=80;ambient=true;particles=false;icon=true;target=caster}'
```

## Remove potion effect

Takes off a potion effect from the target entity. Potion effect names are available on the [Spigot javadocs](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html). 

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| effect   | eff, e, type, pe | Name of potion effect to take off | - |
| target  | -      | The target entity to set on fire. | target or caster |

```yml
example_script:
  mechanics:
  - 'remove_potion{effect=slowness;target=caster}'
```

## Set on fire

Sets the target entity on fire for a certain amount of time (in ticks).

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| ticks   | t, duration, dur, d, time      | Amount of time to set the entity on fire for, in ticks. | - |
| stack   | add      | If true, adds the provided ticks to the entity's current fire ticks instead of setting it. | false |
| max     | -      | If true, takes to the maximum between the current fire ticks and the provided ticks. | false | 
| min     | -      | If true, takes the minimum between the current fire ticks and the provided ticks. | false | 
| target  | -      | The target entity to set on fire. | target or caster |

`stack` has precedence over `max` and `min`, and `max` has precedence over `min`.

```yml
example_script:
  mechanics:
  - 'set_on_fire{ticks=20;stack=false;max=false;min=false;target=target}'
```

## Set no damage ticks

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| ticks   | t, duration, dur, d, time     | Duration of invulnerability in ticks | 10 |
| stack   | add      | If true, adds the provided ticks to the entity's no damage ticks instead of setting it. | false |
| max     | -      | If true, takes the maximum between the current no damage ticks and the provided ticks. | false | 
| min     | -      | If true, takes the minimum between the current no damage ticks and the provided ticks. | false | 
| target  | -      | The target entity | target or caster |

Makes the target entity invulnerable for the provided amount of time (in ticks).

```yml
example_script:
  mechanics:
  - 'set_no_damage_ticks{target=caster;ticks="40 + 20 * <modifier.extra>"}'
```