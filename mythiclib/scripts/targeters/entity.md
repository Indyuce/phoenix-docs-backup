
# Entity Targeters

## Caster

Use this targeter to target the skill caster.

```
example_use:
    type: caster
```

## Cone

Targets entities in a cone, given a cone `angle` and `radius` which are numeric parameters. You can use math formulas for these parameters. The angle is given in degrees. The `source` parameter is optional, you may provide the starting point of the cone using a location targeter. It is set by default to the caster's position.

The `direction` parameter is also optional, you need to provide the cone's direction using a location targeter. It is set to the caster's eye direction by default.

```
example_use:
    type: cone
    radius: 1
    angle: .3
    source:
        type: caster
        position: BODY
    direction:
        type: custom
        x: 0
        y: 0
        z: 1
```

## Nearby entities

Use this to target entities around a specific location given a radius and height. This basically takes all entities in a **cylinder** around a center location.

Setting the `source` parameter to true will use the script source location as center location. If set to false, ML will first try to use the script target location as center location.

By default, the `nearby_entities` targeter ignores the caster/entity skill target. If you toggle off `ignore_caster`, the skill caster/entity skill target will be taken into account by this targeter.
```
example_use:
    type: nearby_entities
    radius: 10
    height: 5
    source: false
    ignore_caster: true
```

## Nearest Entity

Takes the entity closest to the script target location.

Setting the `source` parameter to true will use the script source location as center location. If set to false, ML will first try to use the script target location as center location.

```
example_use:
    type: nearest_entity
    radius: 10
    source: false
```

## Target entity

One of the simplest targeter, used to target the script target.

```
example_use:
    type: target
```

## Looking at

Targets the entity the caster is looking at. It is possible that no entity is found. There is an equivalent targeter for blocks instead.

```
example_use:
    type: looking_at
    range: '0.2 + 0.3'
    size: '50 + 10'
    ignore_passable: true # Should it ignore or stop on semi-transparent blocks like fences
```

## Variable target

If an entity happens to be stored as a variable in a script, you can access it using this targeter. This has no use yet.

```
example_use:
    type: variable
    name: variable_name_here
```