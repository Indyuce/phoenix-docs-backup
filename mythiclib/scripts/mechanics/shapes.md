---
order: 6
---

# 📐 Shapes

::: warning
Under construction
:::

To get used to these mechanics, which can get really complex, but are really fun to configure, use a simple tick script to see what shape the mechanic draws!

```yml
simple_tick:
  mechanics:
  - 'display_particle{particle=FLAME}'
```

## Helix

The script indicated by the `end` config option is called when the helix is fully drawn.

```yml
example_mechanic:
    type: helix
    source: # Optional. Location targeter required
        type: source
    direction: # Optional. Location targeter required
        type: custom
        x: 1
        y: 0
        z: 0
    tick: simple_tick
    end: another_script

    # More options
    yaw: 360 # Amount of degrees 
    height: 3 # Height of helix
    radius: '2 + <caster.health> / 100'

    points: 40 # Amount of points displayed in one spiral
    time_interval: 1 # Interval of time (ticks) between two points
    points_per_tick: 1 # Amount of points displayed every interval
    helixes: 4 # Amount of spirals, 1 by default
```

## Parabola
A parabola displayed between two locations. You can configure the height of the parabola and the speed at which it is displayed.

```yml
example_mechanic:
    type: parabola
    source: # Location targeter required. Starting point of parabola
        type: caster
        position: BODY
    target: # Location targeter required. End point of parabola
        type: target
        position: BODY

    tick: simple_tick
    end: another_script # Called when reaching the end
    height: 10 # Height of parabola
    speed: 3 # Horizontal speed
```

## Projectile
A projectile that stops onto the first hit block/entity. You have to specify the type of interaction that your projectile corresponds to (offensive skill, support skill etc. - learn more about it [here](../conditions/misc.md#if-script-caster-can-damagetarget-entity)).

```yml
example_mechanic:
    type: projectile
    
    source: # Optional. Location targeter required
        type: caster
        position: EYES
    direction: # Optional. Location targeter required

    tick: simple_tick
    hit_entity: some_script # Called when hitting an entity
    hit_block: some_other_script # Called when hitting a block
    stop_on_block: true

    offense: true
    hits: 1 # Maximum amount of hit entities. Will disappear on last entity hit
    ignore_passable: false # It it should ignore passable blocks
    speed: 1 # 1 by default
    size: 0.2
    step: 0.2 # Distance between two calls of the tick script
    life_span: 60 # In ticks
```

## Raycast

Raycasts are invisible rays that are shot from the player's eye location. They stop on first block or entity hit.

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| range   | rng, length, len, distance, dist | Length of the raycast | 50 |
| size    | width, wide     | Width of the raycast | 0.2 |
| step_size    | step, st, ss | Distance between two calls of the tick script | 0.4 |
| ignore_passable | ip | Whether passable blocks should be ignored | false |
| neutral | - | Whether the raycast is neutral (does not check for friendly fire) | false |
| offense | - | Whether the raycast is offensive (checks for friendly fire) | true |
| tick | - | Script called every step of the raycast | none |
| hit_entity | - | Script called when hitting an entity | none |
| hit_block | - | Script called when hitting a block | none |



```yml
example_script:
  mechanics:
  - 'raytrace{tick=simple_tick;hit_entity=some_other_script_name;range=50;size=0.2;step=0.4;ignore_passable=false}'
```

## Slash
Performs what looks like a weapon slash in front of the script caster

```yml
example_mechanic:
    type: slash

    tick: simple_tick
    end: some_other_script

    length: 4 # Slash length
    angle: -30 # Angle of the slash
    distance: 3 # Distance to the player

    # Same options as in the Helix mechanic
    points: 20
    time_interval: 1
    points_per_tick: 3
```

## Sphere

::: warning
Under construction
:::
