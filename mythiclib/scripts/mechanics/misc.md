# 🔧 Miscellaneous

### Apply cooldown
First read the mechanic above.
In MMOItems/MMOCore, any object that has a cooldown (an item, parrying, dodging, a skill etc.) has a cooldown key associated to it (see [here](../variables.md#cooldownmap)). As long as it's not being used in MMOItems/MMOCore, you can claim any string key for your plugin and use it for anything.

MythicLib fully lets you setup cooldowns. Paired with cooldown conditions you can fully check, compute and apply cooldowns inside of your scripts.

Cooldown value is in seconds.
```
example_mechanic:
    type: apply_cooldown
    path: 'myplugin_someskill'
    value: 10
```

### Reduce cooldown of target
First read the mechanic above.

`value` determines the amount of cooldown reduction, by default in seconds. Parameter `reduction` determines the "reduction mode" as explained below.

If the mode is set to `FLAT`, target cooldown will be reduced by a set amount of seconds. If the mode is set to `INITIAL`, target cooldown will be reduced by X% of its initial value. For an initial cooldown of 10s, a 20% cooldown reduction with mode `INITIAL` will reduce the target cooldown by `20% * 10 = 2s`.

If the mode is set to `REMAINING`, target cooldown will be reduced by X% of its remaining (not total) value. For a 10s cooldown, if 3s have passed, remaining cooldown is 7s. A 20% remaining cooldown reduction is equivalent to a flat `20% * (10 - 3) = 1.4s` cooldown reduction.

```
example_mechanic:
    type: reduce_cooldown
    path: 'myplugin_someskill'
    value: 5
    reduction: FLAT
```

### Adding delay to your script
Delay is in **ticks**. ML will wait X ticks before executing the next mechanic.

```
example_mechanic:
    type: delay
    amount: 10
```

### Dispatch a command
Set `from_console` to true to have the command dispatched by console instead, otherwise ML takes the script target entity. Set `op` to true to have the command ran as op.
```
example_mechanic:
    type: dispatch_command
    from_console: true
    op: false
    format: 'mmocore admin skill-points add <caster.name> 10'
    target: # Optional. Entity targeter needed here
        type: caster
```

### Play an entity effect
Entity effects available [here](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/EntityEffect.html). `HURT` is very useful, it just simulates a 0-damage attack - perfect for improving skills with non-damaging effects -.

```
example_mechanic:
    type: entity_effect
    effect: HURT
    target:
        type: target
```

### Trigger a lightning strike
Setting `effect` to false will make the lightning deal no damage.
```
example_mechanic:
    type: lightning_strike
    effect: false
    target_location:
        type: target
```

### Cast another script
This mechanic is pretty special. It can be used to cast another script will specific target entities and locations. It can also be used to modify the source location of a script.

All of its parameters are optional. You need to provide either entity or location targeters for each.

```
example_mechanic:
    type: script
    name: other_script_name
    target: # Entity targeter required
    target_location: # Optional. Location targeter required
    source: # Optional. Location targeter required
```

This can also be used to cast the same script multiple times in a row, while counting the amount of times it has been cast so far. The following script casts 12 times the script called `ite`. The variable `iteration_count` is used to count the amount of times the script has been cast so far. It can therefore be accessed using `<var.iteration_count>`.
```
example_mechanic:
    type: script
    name: ite
    iterations: 12
    counter: 'iteration_count'
```

### Give an item
Give a vanilla item to a player.

```
example_mechanic:
    type: give_item
    amount: '<modifier.amount>'
    material: DIAMOND
    target:
        type: caster
```