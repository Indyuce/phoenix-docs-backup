### Deal damage to an entity
Deals damage to the entity provided. This applies on-hit effects, crit strikes, damage mitigation... (fully compatible with MMOItems and MMOCore).

See available damage types [here](Damage System).
```
example_mechanic:
    type: damage
    amount: '100 * (1 + <modifier.extra> / 100)'
    damage_type: 'PHYSICAL,WEAPON'
    knockback: true
    ignore_immunity: false
    element: FIRE # Optional. Can be used to deal elemental damage
    target:
        type: nearby_entities
        radius: 3
```

### Multiply the current attack damage
If no damage type is provided the entire attack damage is modified. Otherwise only the specific portion of the attack due to the given damage type is affected. If an element name is provided, only damage due to that specific element will be affected.

You cannot provide both an element and a damage type. When providing an element name, the damage type parameter is ignored.

If `additive` is set to true, this damage buff will stack with stats like PvE damage, Undead Damage (which stacks additively i.e `10% + 10% <=> +20%`). Otherwise, buffs stack up geometrically i.e `110% * 110% = 121% <=> +21%`.
```
example_mechanic:
    type: multiply_damage
    amount: '1 + <modifier.extra> / 100'
    damage_type: PHYSICAL
    element: FIRE
    additive: false
```

### Apply potion effect
Potion effect names available [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html). Duration is provided in ticks.
```
example_mechanic:
    type: potion
    effect: INCREASE_DAMAGE
    level: 5
    duration: 80
    ambient: true
    particles: false
    icon: true
    target:
        type: target
```

### Set on fire
- Toggle on `stack` to add fire ticks instead of setting the entity fire ticks. This option is great for one-time abilities.
- When `max` is toggled on, MythicLib will take the highest value between the one provided and the current entity's fire ticks (you can only add fire ticks). This option is great for passive skills which should not stack ticks, but rather make sure the entity's fire ticks does not get below some threshold.
- When `min` is toggled on, ML will take the lowest value between the one provided and the current entity's fire ticks (you can only take off fire ticks)

Amount of time to be given in ticks.

```
example_mechanic:
    type: set_on_fire
    ticks: 20
    stack: false
    max: false
    min: false
    target:
        type: target
```