---
order: 12
---

# Healing, Helix Particles

::: warning
Under Construction
:::

```yml
healing_aura:
    public: true
    mechanics:
        helix:
            type: helix # This will load the helix mechanic.
            source: 
                type: caster
            direction: 
                type: custom
                x: 0
                y: 3
                z: 0
            tick: heal_tick # The script that will be executed on every tick.
            end: caster_heal # The script that will be executed when the helix reaches its end point.
            yaw: 360 # The amount of degrees a helix will turn within it's height parameter. 
            height: 3 # The height of helix.
            radius: 1.5 # How far away the helixes will be from the target.
            points: 40 # Amount of points displayed in one spiral.
            time_interval: 1 # Interval of time (ticks) between two points
            points_per_tick: 1 # Amount of points displayed every interval
            helixes: 4 # Amount of helix, the default is 1.

heal_tick:
    mechanics:
        particle:
            type: particle
            particle: COMPOSTER
            amount: 1
            speed: 0
            x: .1
            y: .1
            z: .1

caster_heal:
    mechanics:
        heal:
            type: heal # This will tell the script to use the healing mechanic.
            amount: '<caster.health> / 5' # This is the amount of health given to the target, this example would be the caster's max health divided by 5, so 20%.
            reason: CUSTOM # The source of the healing.
            target:
                type: caster # This would make the caster receive the healing.
```

## A more advanced helix-based skill
```yml
helix_staircase:
    public: true
    mechanics:
        helix:
            type: helix
            source:
                type: caster
            direction:
                type: custom
                x: 0
                y: 3
                z: 0
            tick: helix_stair
            end: poof
            yaw: 360 
            height: 5
            radius: 3
            points: 40 
            time_interval: 1 
            points_per_tick: 1 
            helixes: 8

helix_stair:
    mechanics:
        raytrace:
            type: raytrace # This will load the raytrace mechanic.
            source:
                type: target_location
            target:
                type: caster
                position: BODY
            tick: stair # The script that will be executed on every tick.
            hit_entity: heal # The script that will be executed when the raytrace crosses an entity.
            range: 50 # How far the raytrace will go.
            size: 0.2 # How big the raytrace is, more visible when using particles.
            step: 0.4 # 

stair:
    mechanics:
        particles:
            type: particle
            particle: COMPOSTER
            amount: 10
            

poof:
    mechanics:
        particlepoof:
            type: particle
            target:
                type: circle
                radius: 3
                amount: 32
                height: 5
            particle: CLOUD
            speed: 0

heal:
    mechanics:
        heal:
            type: heal
            amount: '<caster.health> / 100'
            reason: CUSTOM
            target:
                type: caster
```

Now we know how to use use the the healing mechanic, next we'll learn how to use the next shape mechanic. The slash mechanic.