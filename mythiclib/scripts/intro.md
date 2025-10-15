---
order: 1
---

# 📜 Introduction

MythicLib provides a custom scripting language that allows you to perform actions, check conditions... to create custom behaviours for all MMO plugins. Scripts can be used to send messages, play particle effects, check for conditions, damage other entities, and many other things.

Scripts perform specific actions which are called [mechanics](mechanics/intro.md). You can also setup [conditions](mechanics/intro.md) which have to be met for the script to run. Some mechanics require parameters like entities or positions: for instance if you'd like to spawn a particle at a given position, you need to specify that exact position, which is done using [targeters](targeters/intro.md). There are targeters for both entities and locations.

MythicLib scripts also feature [variables](variables.md) which you can use to save temporary information or do computations. For instance MythicLib has a wide variety of mechanics that you can use for vector calculation.

MythicLib scripts can also be turned into MMOCore class skills or MMOItems item abilities, more information on this [wiki page](../skills/custom/mythiclib.md).

## Very Important!

::: warning
**Scripts are not skills!** You can turn scripts into skills, but not the other way around. MythicLib scripts are a way to implement skills which will then be used in MMOCore or MMOItems. Fabled and MythicMobs also provide their script/skill systems. Overall, the MythicLib scripting language is less capable but great for handling basic tasks and too-not-complex skills. You don't need to install anything else to use MythicLib scripts, they are built-in and ready to use.
:::

The primary goal of the MythicLib custom skill system is the ability to register skills with the plugin which you like to program the most with. If MMOItems or MMOCore asks you to use ML scripts you can always use MythicMobs or SkillAPI instead to have custom scripts executed.

Since scripts are used in MMOCore and MMOItems, they are heavily oriented towards creating custom abilities, skills or attack effects. Therefore, they feature premade tools like shaped mechanics which let you easily display cool particle effects, raycasts, projectiles etc.

## Script Example

```yml
teststaff: # The name of your script/the skill ID for MMOCore usage, this should be in full caps for MMOCore. (also called up with /ml cast *skill ID*)
    public: true  # Makes the skill usable by MMOCore and /ml cast *skill ID*.
    mechanics:
        raycast: # This is a mechanic name. (this name can be whatever you want as long as it isn't the same as any other mechanic name in the file.)
            type: raytrace # This tells the script what mechanic to use, a list of mechanics can be found in the mechanics tab.
            hit_entity: teststaff_hit_entity # This calls upon another script when hitting an entity.
            tick: teststaff_tick # This calls upon another script on every tick. (A second is 20 ticks.)
            size: 1

teststaff_hit_entity: # The name of a script, used to call upon this script in another script.
    mechanics:
        dealdamage: 
            type: damage # What mechanic to use.
            amount: 10 # Sets the damage/mechanic parameter.
        showparticles: # This is another mechanic name.
            type: particle # What mechanic to use.
            particle: LAVA # This sets which particle it should show/parameter 1.
            amount: 32 # This sets the amount of particles to use/parameter 2.

teststaff_tick: # The name of a script, used to call upon this script in another script.
    mechanics:
        showparticles:
            type: particle
            particle: REDSTONE 
            amount: 4 
            x: .5 # This sets how far the particles can move on the x-axis on both sides around the source.
            y: .5 # This sets how far the particles can move on the y-axis on both sides around the source.
            z: .5 # This sets how far the particles can move on the z-axis on both sides around the source.
```

When a player runs the `teststaff` script it will send out a ray of redstone particles to the first entity in the casters line of sight and then at said entity and deals 10 damage.

You can then reload your ML scripts using `/ml reload` and cast your new skill using `/ml cast YOUR_SCRIPT_NAME_HERE`

## Numeric Parameters

```yml
dealdamage:
    type: damage
    amount: '10 + <var.damage> / 2'
    target:
        type: caster
    knockback: false
    type: MAGIC,ON_HIT
```

Many mechanics include "numeric parameters": the amount of damage dealt by the `damage` mechanic, the duration in ticks of a potion effect being applied, the radius of a particle sphere...

99% of these mechanics fully support mathematical formulas. This means that you can use numbers in conjunction with commonly used operators, math functions, and even PAPI placeholders to unlock full configurability with your custom skills. Numerical formulas also support [internal variables](variables.md) as described below.

## Text Parameters

Mechanics which require strings support placeholders from PlaceholderAPI, although these are not the only placeholders you can use. MythicLib also has [internal variables](variables.md) that you can access using `<...>` instead of the usual `%...%` format from PlaceholderAPI.

```yml
tellmsg:
    type: tell
    format: 'Skill was cast at <source.x> - <source.y> - <source.z> by %player_name%!!'
    target:
        type: caster
```

## JSON/YAML Syntaxes

The two following formats for a skill are totally equivalent and both will work just fine, so you might just use the one you like the best. If you are more familiar with MythicMobs, use the second one. If you are more familiar with pure YAML or even SkillAPI, use the first one. The second JSON-ish format is only available starting with MythicLib 1.6.2+ development builds.

```yml
staff_attack:
    public: true
    mechanics:
        raycast:
            type: raytrace
            hit_entity: staff_attack_hit_entity
            tick: staff_attack_tick
            size: 1
    conditions: {}
```

The second format uses a string list to store the script mechanics and conditions instead of configuration sections. This format is more compact but readability can be a little harder.
```yml
staff_attack:
    public: true
    mechanics:
    - 'raytrace{type=raytrace;hit_entity=staff_attack_hit_entity;tick=staff_attack_tick;size=1}'
    conditions: []
```