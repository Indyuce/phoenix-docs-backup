Raycasts are invisible rays that are shot from the player's eye location. They stop on first block or entity hit. `tick` is the script that is called along that invisible line. `hit_entity` is the script called when hitting an entity. `hit_block` is the script called when hitting a block.

### Entity & block raycasts
A raycast that stops on both entities and blocks.
```
example_mechanic:
    type: raytrace_blocks
    tick: some_script_name
    hit_entity: some_other_script_name
    hit_block: another_script_name

    # Other raycast options
    range: 50
    size: 0.2
    step: 0.4
    ignore_passable: false # False by default
```

### Block raycasts
Only stops on blocks.
```
example_mechanic:
    type: raytrace_blocks
    tick: some_script_name
    hit_block: another_script_name

    # Other raycast options
    range: 50
    step: 0.4
    ignore_passable: false # False by default
```

### Entity raycasts
Only stops on entities.
```
example_mechanic:
    type: raytrace_blocks
    tick: some_script_name
    hit_entity: some_other_script_name

    # Other raycast options
    range: 50
    size: 0.2
    step: 0.4
```