
# Entity Targeters

## Caster

Use this targeter to target the skill caster. This targeter has no parameter so you can use just `target=caster` instead of `target={type=caster}`.

```yml
message_script:
  public: true
  mechanics:
  - message{format="Hello world!";target=caster}
```

## Cone

Targets entities in a cone, given a cone `angle` and `radius` which are numeric parameters. You can use math formulas for these parameters. The angle is given in degrees. The `source` parameter is optional, you may provide the starting point of the cone using a location targeter. It is set by default to the caster's position.

The `direction` parameter is also optional, you need to provide the cone's direction using a location targeter. It is set to the caster's eye direction by default.

```yml
cone_slash_attack:
  public: true
  mechanics:
  - 'damage{amount=10;source=caster;target={type=cone;radius=3;angle=90}}'
```

## Nearby entities

Use this to target entities around a specific location given a radius and height. This basically takes all entities in a **cylinder** with height `height` and radius `radius` around a center location.

Setting the `source` parameter to `true` will use the script source location as center location. If set to `false`, ML will first try to use the script target location as center location.

By default, the `nearby_entities` targeter ignores the caster/entity skill target. If you toggle off `ignore_caster`, the skill caster/entity skill target will be taken into account by this targeter.
```yml
aoe_damage_skill:
  public: true
  mechanics:
  - 'damage{amount=10;target={type=nearby_entities;radius=10;height=5;ignore_caster=true}}'
```

## Nearest Entity

Takes the entity closest to the script target location, with a maximum range of `radius`.

Setting the `source` parameter to true will use the script source location as center location. If set to false, ML will first try to use the script target location as center location.

```yml
damage_to_nearest_entity:
  public: true
  mechanics:
  - 'damage{amount=10;target={type=nearest_entity;radius=10}}'
```

## Target entity

One of the simplest targeter, used to target the script target.

```yml
damage_to_target:
  public: true
  mechanics:
  - 'damage{amount=10;target=target}'
```

## Looking at

Targets the entity the caster is looking at. It is possible that no entity is found, in which case the mechanic using this targeter will not be executed. `size` is the size of the raytrace, setting it to `1` means that you will hit entities which bounding boxes are at most 1 block away from your line of sight. `length` is the maximum distance at which an entity can be targeted. `ignore_passable` can be used to ignore passable blocks like tall grass or flowers.

```yml
damage_on_line_of_sight:
  public: true
  mechanics:
  - 'message{format="test"}'
  - 'damage{amount=10;target={type=looking_at;size="0.2 + 0.3";length="50 + 30";ignore_passable=false}}'
```

## Variable target

If an entity happens to be stored as a variable in a script, you can access it using this targeter.

```yml
damage_to_self:
  public: true
  mechanics:
  - 'damage{amount=10;target={type=variable;name="caster"}}' # variable name with 'caster' returns the skill caster
```