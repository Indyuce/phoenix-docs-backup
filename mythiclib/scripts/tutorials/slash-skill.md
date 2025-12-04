---
order: 13
---

# Sword Slash

::: warning
Under Construction
:::

```yml
sword_slash:
    public: true
    mechanics:
        slash:
            type: slash # This will load the slash mechanic.
            tick: slash_particle # The script that will be executed on every tick.
            length: 4 # Slash length.
            angle: -30 # Angle of the slash.
            distance: 1.5 # Distance to the player.
            points: 20 # How many points the slash will have.
            time_interval: 1 # How long it takes for the next point on the slash to load.
            points_per_tick: 3 # How many points will be loaded per tick
        delay:
            type: delay # This loads the delay mechanic.
            amount: 5 # How long the delay should be.
        dealdamage:
            type: damage
            amount: 10 
            knockback: true 
            preventimmunity: false
            target: 
                type: cone # This will make the target a cone in front of the caster.
                radius: 3 # This is how far the cone goes from the caster.
                angle: 25 # How wide the cone should be.
            source:
                type: caster
                position: EYES
 
slash_particle:
    mechanics:
        particle:
            type: particle
            particle: REDSTONE
            amount: 5
```

## Triple Sword Slash
```yml
triple_sword_style:
    public: true
    mechanics:
        slash_one:
            type: slash
            tick: slash_particle_turquoise
            length: 4 
            angle: 90 
            distance: 1.5
            points: 20 
            time_interval: 1
            points_per_tick: 3
        slash_two:
            type: slash
            tick: slash_particle_purple
            length: 5
            angle: 30 
            distance: 1.5 
            points: 20
            time_interval: 1
            points_per_tick: 3
        slash_three:
            type: slash
            tick: slash_particle_blue
            length: 5 
            angle: 150 
            distance: 1.5
            points: 20
            time_interval: 1
            points_per_tick: 3
        delay:
            type: delay
            amount: 5
        dealdamage:
            type: damage
            amount: 10 
            knockback: true 
            preventimmunity: false
            target: 
                type: cone
                radius: 3
                angle: 25
            source:
                type: caster
                position: EYES
        applyeffect:
            type: potion
            effect: WEAKNESS
            level: 2
            duration: 80
            ambient: true
            particles: true
            icon: true
            target: 
                type: cone
                radius: 3
                angle: 25
        dealdamage:
            type: damage
            amount: 10 
            knockback: true 
            preventimmunity: false
            target: 
                type: cone
                radius: 3
                angle: 25
            source:
                type: caster
                position: EYES
        applyeffect:
            type: potion
            effect: POISON
            level: 2
            duration: 80
            ambient: true
            particles: true
            icon: true
            target: 
                type: cone
                radius: 3
                angle: 25
        dealdamage:
            type: damage
            amount: 10 
            knockback: true 
            preventimmunity: false
            target: 
                type: cone
                radius: 3
                angle: 25
            source:
                type: caster
                position: EYES
        applyeffect:
            type: potion
            effect: WITHER
            level: 2
            duration: 80
            ambient: true
            particles: true
            icon: true
            target: 
                type: cone
                radius: 3
                angle: 25

slash_particle_turquoise:
    mechanics:
        particle:
            type: particle
            particle: REDSTONE
            amount: 5
            color: # Color goes here.
                red: 19
                green: 116
                blue: 148
                
slash_particle_purple:
    mechanics:
        particle:
            type: particle
            particle: REDSTONE
            amount: 5
            color: # Color goes here.
                red: 100
                green: 21
                blue: 173
                
slash_particle_blue:   
    mechanics:
        particle:
            type: particle
            particle: REDSTONE
            amount: 5    
            color: # Color goes here.
                red: 18
                green: 86
                blue: 196            
```
