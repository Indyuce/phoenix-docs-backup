There are four player resources in MMOCore which all have different objectives: health, mana, stamina and stellium. [Stellium](Waypoints) can be used to warp across waypoints. Mana and stamina can be used to cast spells and use items.

Note: all following config samples are to be placed in a class config file like `classes/Mage.yml`.

## Resource Regeneration
MMOCore has **two** types of resource regen. First of all, every class has a base **flat** resource regeneration stat, for any of the four resource. For instance, _10 Stamina Regen_ means that players regenerate 10 stamina every second. If you toggle on the `off-combat-stamina-regen` class option, players will only regenerate that flat amount when they are out of combat.\
Every class also has another regeneration stat, like `Max Health Regeneration` which is expressed in % max health per second. It is the percentage of your maximum health that you will regenerate every second. This second stat stacks up with the first regen.

Default Mage Setup:
```yaml
options:
    off-combat-health-regen: true

attributes:
    health-regeneration:
        base: 0.13
        per-level: 0
    max-health-regeneration:
        base: 0.13
        per-level: 0
```
Mages only regenerate their health when they are out of combat, as they are rather weak and must concentrate to get their forces back. Mages have a base regen of 0.13 health/sec.

## Special Resource Regeneration
The second type of regeneration in MMOCore can almost be considered a passive skill. Classes can be setup to have a resource regeneration which scales on the player's missing/max health/stamina/mana. That way, classes have a base regen value, plus some extra % of their missing/max resource when they are out of combat.

This can be particularly useful if you want to develop new classes which have a special type of resource. For instance, warriors with _Rage_ instead of _Mana_, can have their Rage slowly decrease when out of combat at a more flexible rate.

The rate at which the resources regenerate (or degenerate) can be configured as well. You can also make it so that regen also applies when in combat by toggling off the `off-combat` option. **Unlike the first type of resource regen, this one is completely independant of the items the player is wearing. It only depends on the player's level which is why it is more of a passive skill.**

```yaml
resource:
    health:
        type: MAX
        value:
            base: 10
            per-level: 1
            max: 20
        off-combat: true
```
That would be a really OP melee fighting class where players would regen from 10 to 20%, based on their current level, of their maximum health when out of combat.

The `type` option is either `MAX` or `MISSING` depending on what you want the resource regen to scale on.

| Type    | Description                           |
|---------|---------------------------------------|
| MAX     | Regen scales with max resource        |
| MISSING | Regen scales with missing resource    |

The `value` config section corresponds to the % regenerated every second. You may use the `min` and `max` options to create bounded linear functions of the player level.