---
order: 2
---

# 🏹 Projectiles

## Shoot Arrow

Use this mechanic to have the skill caster fire an arrow.

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| from_item | - | When true, MMOItems will take into account the bow stats for crits, attack damage... | false |
| player_attack_damage | - | Whether to use the player's attack damage attribute as base damage for the arrow. | false |
| velocity | vel, speed, sp | Multiplier for the arrow's speed. | 1.0 |
| hit | - | Script called when the arrow hits an entity or block. | - |
| land | - | Script called when the arrow lands on the ground without hitting anything. | - |
| tick | - | Script called every tick while the arrow is flying. | - |
| damage_types | - | Comma-separated list of damage types to apply to the arrow. | `*` |

`*` The default damage types are the ones provided in the MythicLib config file for bow attacks.

The following script is used by MMOItems to handle attacks from the _Crossbow_ weapon type. It makes sure that arrows are only consumed when not in creative mode or when the arrow has the `MMOITEMS_DISABLE_ARROW_CONSUMPTION` tag. It also makes the arrow shoot faster based on the player's `arrow_velocity` stat, and adds a particle effect to the flying arrow.
```yml
crossbow_attack:
  public: true
  conditions:
    - 'ammo{item=ARROW;creative_infinite=true;item_ignore_tag=MMOITEMS_DISABLE_ARROW_CONSUMPTION}'
  mechanics:
    - 'take_ammo{item=ARROW;creative_infinite=true;item_ignore_tag=MMOITEMS_DISABLE_ARROW_CONSUMPTION}'
    - 'play_sound{sound=ENTITY_ARROW_SHOOT;pitch=.5}'
    - 'shoot_arrow{from_item=true;player_attack_damage=true;tick=crossbow_arrow_tick;velocity="non_zero(<stat.arrow_velocity>, 1) * 3"}'

crossbow_arrow_tick:
  mechanics:
    - 'particle{particle=CRIT;speed=.05}'

```

## Shulker Bullet

Use this mechanic to have the skill caster fire a shulker bullet.

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| life_span | lifetime, l, ticks, duration, dur, d | The lifespan of the shulker bullet in ticks. | 60 |
| hit_entity | - | Script called when the shulker bullet hits an entity. | - |

```yml
shoot_shulker_bullet:
  mechanics:
    - 'shoot_shulker_bullet{life_span=100;hit_entity=shulker_bullet_hit}'

shulker_bullet_hit:
  mechanics:
    - 'damage{dmg=10}'
```