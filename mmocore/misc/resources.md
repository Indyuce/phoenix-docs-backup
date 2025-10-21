# 💖 Player Resources

There are four player resources in MMOCore, with different objectives. These resources regenerate over time.
- **health**
- **mana** and **stamina**, used to cast [skills](../skills/intro.md) and use items
- **stellium**, used for [waypoints](../features/waypoints.md)

## Base Resource Regen

MMOCore has **two** types of resource regen. First of all, every class has a base **flat** resource regeneration stat, for any of the four resource. For instance, _10 Stamina Regen_ means that players regenerate 10 stamina points every second. If you toggle on the `off-combat-stamina-regen` class option, players will only regenerate that flat amount when they are out of combat.

Every class also has another regeneration stat, like `Max Health Regeneration` which is expressed in % max health per second. It is the percentage of your maximum health that you will regenerate every second. This second stat stacks up with the first regen.

```yaml
# classes/mage/mage.yml

options:
  off-combat-health-regen: true

attributes:
  health-regeneration:
    base: 0.13
    per-level: 0
  max-health-regeneration:
    base: 1
    per-level: 0
```

In the default MMOCore config, mages only regenerate their health when they are out of combat, _as they are rather weak and must concentrate to get their forces back_. Mages have a base regen of 0.13 health + 1% of their max health/sec.

## Special Resource Regen

This second type of resource regen in MMOCore can almost be considered a passive skill. Classes can be setup to have special type of resource regen, that scales on the player's amount of max/missing resource. This special resource regen can also be toggled off during combat.

This can be particularly useful if you want to develop new classes which have a special type of resource. For instance, warriors with _Rage_ instead of _Mana_, can have their Rage slowly decrease when out of combat at a more flexible rate.

The rate at which the resources regenerate (or is lost) can be configured as well. You can also make it so that regen does not apply when in combat, by toggling off the `off-combat` option. **Unlike the first type of resource regen, this one is completely independant of the items the player is wearing. It only depends on the player's level.**

```yaml
resource:

  # Health resource
  health:
    type: MAX
    value:
      base: 10
      per-level: 1
      max: 20
    off-combat: true

  # Mana resource
  mana:
    type: MISSING
    #......

  # Other resources....
```
That would be a really OP melee fighting class where players would regen 10-20% of their maximum health (based on their current level) every second, when out of combat.

The `type` option is either `MAX` (scales with max resource) or `MISSING` (scales with missing resource) depending on what you want the resource regen to scale on. The `value` entry corresponds to the % of resource regenerated every second. You may use the `min` and `max` options to create bounded linear functions of the player level.