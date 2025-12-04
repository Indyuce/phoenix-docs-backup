---
order: 3
---

# 🗡️ On-Hit Effects

_On-Hit Effects_ are special effects that trigger when a player deals damage to another entity (either a monster or a player).

For instance, _Skill_ and _Weapon Critical Strikes_ are considered on-hit effects. _Lifesteal_, which heals the attacker based on a percentage of the damage dealt, is another example of an on-hit effect. _Manasteal_, which restores mana to the attacker based on a percentage of the damage dealt, is also an on-hit effect.

Most on-hit effects directly depend on numerical player stats, such as _Critical Strike Chance_ or _Lifesteal Percentage_. In this page, we go over the built-in on-hit effects provided by MythicLib, as well as how to create custom ones.

## Builtin On-Hit Effects

MythicLib comes with several on-hit effects built in, including:
- _Weapon_ & _Skill Critical Strikes_
- _Lifesteal_, _Skill Vampirism_

## Custom On-Hit Effects

You can create your own custom on-hit effects by adding new sections to the `MythicLib/on_hit_effects.yml` file. Each section should follow the same structure as the built-in on-hit effects. The next section goes over the different parameters available for on-hit effects, using _Weapon Critical Strikes_ as an example.

While you can certainly recreate similar _On-Hit Effects_ using other plugins or scripting solutions, MythicLib aims to provide an easy-to-use framework finetuned to RPG server use cases.

## An Example

All on-hit effects are configured in the `MythicLib/on_hit_effects.yml` file. Each on-hit effect has its own section in the file, where you can customize its behavior and parameters. Let us go over the built-in config section for _Weapon Critical Strikes_ as an example:

```yml
weapon_crits:

  pre_attack: skill_crit_script_check

  # Formula for cooldown between two consecutive weapon crits (in seconds)
  # To disable cooldown, delete this line, or comment it out
  cooldown: '3 * (1 - <stat.critical_strike_cooldown_reduction> / 100)'

  # Chance to successfully perform a weapon crit
  # This formula should return a value between 0 and 1 (0 being 0% chance, 1 being 100% chance)
  # Note that, by default, weapon crit strike is capped at 80% (see stats.yml)
  roll: '<stat.critical_strike_chance> / 100'

  # Script/skill ran on weapon crit
  on_attack: weapon_crit_script
```

### Cooldown

The option `cooldown` indicates that such on-hit effect has a cooldown. It cannot occur more frequently than once every X seconds, where X is the value returned by the formula. The default formula for _Weapon Critical Strikes_ is `3 * (1 - <stat.critical_strike_cooldown_reduction> / 100)`, meaning that the base cooldown is 3 seconds, but it can be reduced by the player's _Critical Strike Cooldown Reduction_ stat.

This is an optional parameter. If you wish to disable the cooldown for an on-hit effect, simply delete the `cooldown` line or comment it out.

### Roll

The option `roll` is a formula that returns the chance of successfully performing the on-hit effect. The formula should return a value between 0 and 1, where 0 means 0% chance and 1 means 100% chance. In the case of _Weapon Critical Strikes_, the default formula is `<stat.critical_strike_chance> / 100`, meaning that if the player has 25% _Critical Strike Chance_, they have a 25% chance to perform a weapon critical strike on each attack.

This is an optional parameter. If you wish for the on-hit effect to always trigger (when not on cooldown), simply set the value to `1`.

### Pre-Attack Script

The script `pre_attack` is executed before the on-hit effect is rolled for. It can be used to set up any necessary variables or conditions for the on-hit effect. In the case of _Weapon Critical Strikes_, the default script is `skill_crit_script_check`, which makes sure that the attack contains either _Weapon_ or _Unarmed_ damage, as weapon crits only apply on these damage types.
```yml
skill_crit_script_check:
  conditions:
    - 'has_damage_type{types="skill"}'
```

This is an optional parameter. If you do not need any pre-attack setup, you can simply omit the `pre_attack` line.

::: info
Note that all built-in scripts used by on-hit effects are all located in the `MythicLib/script/on_hit_effects` config file. You can view and edit them as you wish.
:::

### Attack Script

Last but not least, the script `on_attack` is executed when the on-hit effect successfully triggers. This script only executes if the following conditions are met:
- the on-hit effect is not on cooldown,
- the roll check is successful,
- any conditions specified in the `pre_attack` script are met,
- the Bukkit event `OnHitEffectEvent` is not cancelled by any plugin.

In the case of _Weapon Critical Strikes_, the default script is `weapon_crit_script`, which applies the critical strike damage multiplier to the attack.
```yml
weapon_crit_script:
  mechanics:
    # increase weapon/unarmed damage by crit power
    - 'set_double{var=crit_coef;val="<stat.critical_strike_power> / 100"}'
    - 'multiply_damage{scalar="<crit_coef>";dtype=WEAPON}'
    - 'multiply_damage{scalar="<crit_coef>";dtype=UNARMED}'

    # play sound and particle effect
    #Uncomment for an action bar message
    #- 'action_bar{m="&6You landed a crit for &c<attack.damage> &6damage!";target=caster;priority=40;duration=30}'
    - "play_sound{sound=ENTITY_PLAYER_ATTACK_CRIT;volume=1;pitch=1}"
    - "particle{particle=CRIT;amount=32;offset_x=.5;offset_y=.5;offset_z=.5;speed=0.5;target_location={type=target;position=BODY}}"
```

### Skip Event

This is an optional parameter for performance. Set `skip_event` to `true` to skip firing the `OnHitEffectEvent` Bukkit event when this on-hit effect triggers. This way, this on-hit event cannot be listened to or cancelled by any plugin.

