# Miscellaneous

::: warning
Under construction
:::

## If script caster can damage/target entity
This is a central check in MMO plugins. It is used to determine if the player can damage/buff another entity without this action being illegal. Imagine you don't want your player skills to damage players within the same party, this can be done using this condition. Similarly, you don't want players to be able to use heals or buffs onto enemies.

The very same condition is checked by MMOCore/MMOItems skills to make sure they aren't cast onto the wrong target which would constitute a gameplay flaw.

This checks many things:
- if the target is a living entity (i.e if it has a health bar)
- if the target is not an unkillable NPC from Citizens
- if the player is not in the same party/guild as the script target
- WorldGuard/Residence/bukkit vanilla PvP flags.

There are four different interaction types:
- `OFFENSE_SKILL` (skills that do damage)
- `OFFENSE_ACTION` (basic/melee/weapon attacks)
- `SUPPORT_SKILL` (skills that buff or heal, apply a positive effect on target)
- `SUPPORT_ACTION` (not used yet)
Everytime you use the `can_target` condition you need to specify the type of interaction so that MythicLib knows what to check in case you happen to use a supported party/guild plugin!

The following skill, called `slash`, deals 100 damage to nearby entities **only if they can actually be damaged by the script runner**.
```
slash:
    mechanics:
        execute_skill_onto_nearby_entities:
            type: skill
            name: slash_subskill
            target:
                type: nearby_entities
                radius: 3
                height: 1

slash_subskill:
    conditions: # Filters untargetable entities
        cantarget:
            type: can_target
            interaction_type: OFFENSE_SKILL
    mechanics:
        deal_damage:
            type: damage
            amount: 100
```

## Check for a player cooldown
This checks if a player has something on cooldown. You have to select some string identifier, called cooldown paths, for MythicLib to save your cooldown information.

If you'd like to check for cooldowns from MMOItems or MMOCore i.e item or skill cooldowns, please refer to [this wiki section](../variables.md#cooldownmap) which provides which cooldown path you need to use for which object.

MythicLib fully lets you setup cooldowns. Paired with cooldown mechanics (learn more in the _Mechanics_ wiki section) you can fully check, compute and apply cooldowns inside of your scripts.

```
example_condition:
    type: cooldown
    path: 'skill_life_ender' # This checks if the Life Ender skill is on cooldown!
```

## Check for the script caster's food level
Checks if the script caster has enough food. You could do the exact same condition using the `compare` generic condition but we're keeping this one for backwards compatibility.

```
example_condition:
    type: food
    amount: '10 + <caster.health> / 2'
```

## Check if attack which triggered the script has some damage type
Please first learn about [triggers](Triggers). When using the `ATTACK` trigger type, sine the script was triggered by an attack you can actually access information about this attack using the `<attack>` internal variable.

This condition can be used to check if the attack which triggered the script contains some type of damage. This is very useful for player skills which should for instance only apply on weapon attacks: you just have to check if the attack contains some `WEAPON` damage.

You can use multiple damage types. If the attack contains ANY of the damage type provided the condition will be met. It will throw a console error if the script was not triggered by an entity attack.

```
example_condition:
    type: has_damage_type
    types: 'WEAPON,PHYSICAL,PROJECTILE'
```

## Check if the target entity is living
Checks if the target entity has a health bar.

```
example_condition:
    type: is_living
```

## Check if the target entity is on fire
Use this to check if the script target entity is on fire. This will check for the script caster if `caster` is set to true (false by default);

```
example_condition:
    type: on_fire
    caster: false
```

## Permission check
Use this to check if the script caster has a specific permission.

```
example_condition:
    type: condition
    name: 'mmoitems.ability.fireball'
```

## Time check
Checks if the script world is within a certain time period: `DAY` (0 to 12000 ticks), `DUSK` (12000 to 13000), `NIGHT` (13000 to 23000) or `DAWN` (23000 to 24000). According to the wiki a Minecraft day lasts 20 minutes which is equivalent to 24k ticks.

This could be used for cool werewolf/dark mage passive skills which only trigger during the night!

```
example_condition:
    type: time
    period: NIGHT
```