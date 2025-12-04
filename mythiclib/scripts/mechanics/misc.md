---
order: 2
---

# 🔧 Miscellaneous

::: warning
Under construction
:::

## Apply cooldown


In MMOItems/MMOCore, any object that has a cooldown (an item, parrying, dodging, a skill etc.) has a cooldown key associated to it (see [here](../variables.md#cooldownmap)). As long as it's not being used in MMOItems/MMOCore, you can claim any string key for your plugin and use it for anything.

MythicLib fully lets you setup cooldowns. Paired with cooldown conditions you can fully check, compute and apply cooldowns inside of your scripts.

Cooldown value is in seconds.
```yml
example_mechanic:
  mechanics:
  - 'apply_cooldown{path=myplugin_someskill;value=10}'
```

## Reduce cooldown of target

::: tip 
First learn above the mechanic above.
:::

`value` determines the amount of cooldown reduction, by default in seconds. Parameter `reduction` determines the "reduction mode" as explained below.

If the mode is set to `FLAT`, target cooldown will be reduced by a set amount of seconds. If the mode is set to `INITIAL`, target cooldown will be reduced by X% of its initial value. For an initial cooldown of 10s, a 20% cooldown reduction with mode `INITIAL` will reduce the target cooldown by `20% * 10 = 2s`.

If the mode is set to `REMAINING`, target cooldown will be reduced by X% of its remaining (not total) value. For a 10s cooldown, if 3s have passed, remaining cooldown is 7s. A 20% remaining cooldown reduction is equivalent to a flat `20% * (10 - 3) = 1.4s` cooldown reduction.

```yml
example_mechanic:
  mechanics:
  - 'reduce_cooldown{path=myplugin_someskill;value=5;reduction=FLAT}'
```

## Adding delay to your script

Delay is in **ticks**. ML will wait a certain number of ticks before executing the next mechanic. Make sure the delay parameter is above zero.

```yml
example_mechanic:
  mechanics:
  - 'delay{amount=10}'
```

## Dispatch a command

Set `from_console` to `true` to have the command dispatched by console instead, otherwise ML takes the script target entity. Set `op` to true to have the command ran as op. `target` is optional.

```yml
example_mechanic:
  mechanics:
  - 'dispatch_command{from_console=true;op=false;format="mmocore admin skill-points add <caster.name> 10";target=caster}'
```

## Play an entity effect

Entity effects available [on the Spigot javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/EntityEffect.html). For instance, `HURT` is very useful, it just simulates a 0-damage attack - perfect for improving skills with non-damaging effects -. `target` is the entity on which the effect will be played. If not provided, it defaults to the script target entity, or script caster.

```yml
example_script:
  mechanics:
  - 'entity_effect{effect=HURT;target=target}'
```

## Trigger a lightning strike

Setting `effect` to ``false`` makes the lightning deal no damage.

```yml
example_script:
  mechanics:
  - 'lightning_strike{effect=false;target_location=target}'
```

## Cast another script

This mechanic is pretty special. It can be used to cast another script will specific target entities and locations. It can also be used to modify the source location of a script.

All of its parameters are optional. You can provide an entity targeter (for the script target entity, through `target`) and two location targeters (one for the script source location through `source`, and one for the script target location through `target_location`).

```yml
example_script:
  mechanics:
  - 'script{name=other_script_name;target=......;target_location=.....;source=.....}'

# Other script being called
other_script_name:
  # ..
```

This can also be used to cast the same script multiple times in a row, while counting the amount of times it has been cast so far. The following script casts 12 times the script called `ite`. The variable `iteration_count` is used to count the amount of times the script has been cast so far. It can therefore be accessed using the placeholder `<iteration_count>`.
```yml
example_script:
  mechanics:
  - 'script{name=iterated_script;iterations=12;counter=iteration_count}'

# Script ran multiple times
iterated_script:
  mechanics:
  # Can use variable "iteration_count" inside this script
  - 'give_item{material=DIAMOND;amount=<var.iteration_count>;target=caster}'

```

## Give an item
Give a vanilla item to a player.

```yml
example_script:
  mechanics:
  - 'give_item{amount=<modifier.amount>;material=DIAMOND;target=caster}'
```

## Shoot an arrow

Have the player shoot an arrow. `from_item` is used by MMOItems for weapon types. `player_attack_damage` makes the arrow use the player's attack damage attribute as base damage. `velocity` is a multiplier for the arrow's speed. Default is 1.0 (normal speed). 

`damage_types` is a comma-separated list of damage types to apply to the arrow. By default, arrows deal physical/weapon damage unless modified in the MythicLib config file.,

`hit` is the name of a script to be executed when the arrow hits an entity or block. `land` is the name of a script to be executed when the arrow lands on the ground without hitting anything. `tick` is the name of a script to be executed every tick while the arrow is flying.



```yml
example_script:
  mechanics:
  - 'shoot_arrow{from_item=false;player_attack_damage=false;hit=on_hit_script;land=on_land_script;tick=on_tick_script;velocity=1.5;damage_types="physical,weapon"}'

on_hit_script:
  #.....

on_land_script:
  #.....

on_tick_script:
  mechanics:
  - 'particle{effect=FLAME}'
```

## Cancel event

If the script was triggered by an event (like EntityDamageByEntityEvent, PlayerInteractEvent, etc.), this mechanic will cancel that event. Otherwise, it will print out an error.

This can be used to prevent damage during an entity damage event, for instance.

```yml
example_script:
  mechanics:
  - 'cancel_event{}'
```