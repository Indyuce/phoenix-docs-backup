---
order: 8
---

# 🎨 Visual

::: warning
Under construction
:::

## Send a message to a player

This supports PAPI placeholders and color codes.

```yml
example_mechanic:
    type: tell
    format: 'Hello world!'
    target:
        type: caster
```

## Play a sound at target location

Sound list [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Sound.html). Pitch ranges from 0.5 (low) to 2 (high).

```yml
example_mechanic:
    type: sound
    sound: ENTITY_ENDER_DRAGON_FLAP
    pitch: 2
    volume: 1
    target:
        type: target_location
```

This mechanics also supports custom sound.

```yml
#Custom Sound
example_mechanic:
    type: sound
    sound: minecraft:custom.effects.sound
    pitch: 2
    volume: 1
    target:
        type: target_location
```

## Spawn a particle

Particle list [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Particle.html).

```yml
example_mechanic:
    type: particle
    target:
        type: circle
        radius: 3

    particle: FLAME
    amount: 30
    speed: 0.2
    x: 0
    y: 0
    z: 0
```

Particles can be summoned with initial velocity by setting amount to 0. You can also use this to summon colored particles (`REDSTONE` particles notably). Integers provided in the `color` config section are in RGB format, from 0 to 255.

```plaintext
example_mechanic:
    type: particle
    target:
        type: circle
        radius: 3

    particle: REDSTONE
    amount: 1
    speed: 0
    x: 0
    y: 0
    z: 0
    color: # Color goes here.
        red: 255
        green: 220
        blue: 0
```

Or particles requiring block data (`BLOCK_CRACK`, `BLOCK_DUST` and `BLOCK_MARKER notably)`. You can find the list of materials that you can use in the `block` option [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html).

```plaintext
example_mechanic:
    type: particle
    target:
        type: circle
        radius: 3

    particle: BLOCK_CRACK
    amount: 1
    speed: 0
    x: 0
    y: 0
    z: 0
    block: PACKED_ICE
```

## Send an action bar message

This supports PAPI placeholders and color codes. For message priority and duration, please refer to the [Messages](../../features/player-messages.md#send-to-action-bar) wiki page.

```yml
example_script:
  mechanics:
    - 'action_bar{target=caster;format="&aYou have been hit for &c<damage> &adamage!";priority=30;duration=30}'
```
