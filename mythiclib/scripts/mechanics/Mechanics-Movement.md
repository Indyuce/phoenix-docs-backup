### Teleport an entity
This will teleport the target entity to target location.
```
example_mechanic:
    type: teleport
    y_offset: 0
    target:
        type: target
    target_location:
        type: custom
        x: -140
        y: 67
        z: 10
```

### Set the velocity of an entity
You need to use a variable in order to provide a position (<=> vector). In the following example, the vector is saved in the variable called `velocity1`.

```
example_mechanic:
    type: set_velocity
    target:
        type: target
    vector: velocity1
```