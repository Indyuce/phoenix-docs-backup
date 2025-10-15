### Caster

Use this to target the script caster's location. By using the `position` argument you can have the position more precise on the player's body (from lowest to highest): `FEET`, `BODY` (half way up), `EYES` (at eyes height), `TOP`. It is set to `BODY` by default.

```
example_use:
    type: caster
    position: EYES
```

### Circle

Use it to run a script multiple times with a set distance away from a center location. `amount` is the amount of locations computed by the targeter.

Setting the `source` parameter to true will use the script source location as center location. If set to false, ML will first try to use the script target location as center location.

```
display_fire_circle:
    type: particle
    particle: FLAME
    target:
        type: circle
        radius: 10
        amount: 20
        source: false
```

### Custom position

Very helpful, using this targeter you can input the position X, Y and Z manually. Setting `relative` to true will **add** to your position the target script position, or caster position if `source` is set to false. `relative` means the position you are inputing is defined "relative" to the script source location.

For instance, the following example returns one block above the script source location.

```
example_use:
    type: custom
    x: 0
    y: 1
    z: 0
    source: true
    relative: true
```

### Source location

Use it to target the script source location. It is usually the location of the player who ran the script initially. No extra parameters.

```
example_use:
    type: source
```

### Target entity location

The location of the script target entity. By using the `position` parameter you can have the position more precisely placed on the entity body (from lowest to highest): `FEET`, `BODY` (half way up), `EYES` (at eyes height), `TOP`. It is set to `BODY` by default.

```
example_use:
    type: target
    position: BODY
```

### Target location

Targets the script target location.

```
example_use:
    type: target_location
```

### Location variable

If a location/position happens to be stored as a variable in a script, you can access it using this targeter.

```
example_use:
    type: variable
    name: variable_name_here
```