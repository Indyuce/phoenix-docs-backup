---
order: 3
---

# 🚶 Movement

## Teleport an entity

This will teleport the target entity to target location.

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| target_location    | -      | Location targeter required. Where to teleport. | target location |
| target |  -       | Entity targeter required. Entity to teleport. | caster |
| y_offset | -      | Y offset applied to the target location. | 0 |

```yml
example_mechanic:
  mechanics:
  - 'teleport{y_offset=0;target=caster;target_location={type=custom;world=world;x=-140,y=67,z=10}}'
```

## Set the velocity of an entity

You need to use a variable in order to provide a position (<=> vector). In the following example, the vector is saved in the variable called `velocity1`.

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| target |  -       | Entity targeter required. Entity to set the velocity of. | caster |
| value | val, v, vector, vec, velocity, vel      | Name of variable containing the vector (position) to set the velocity to. | none |

```yml
example_mechanic:
  mechanics:
  - 'set_vector{var=velocity1;x=0;y=1;z=0}'
  - 'set_velocity{target=caster;value=velocity1}'
```
