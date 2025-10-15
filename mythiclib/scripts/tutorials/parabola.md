## A rainbow skill
```
rainbow:
    public: true
    mechanics:
        parabola:
            type: parabola #This calls upon the parabola mechanic.
            source: 
                type: custom
                x: '10'
                y: 0
                z: 0
                source: false
                relative: true
            target: 
                type: custom
                ignore_passable: true
                x: '-10'
                y: 0
                z: 0
                source: false
                relative: true
            start: Cloud_one #The script that will be executed when this script triggers.
            tick: Rainbow_tick 
            end: Cloud_two #The script that will be executed when the parabola reaches its end-point.
            height: 10 # Height of the parabola 
            speed: 5 # Speed at which the parabola travels along its path.

Cloud_one:
    mechanics:
        particleone:
            type: particle
            target:
                type: circle # This will target the outer ring of a circle shape.
                radius: 2 # The radius of the circle.
                amount: 32 # How many particles/points on the ring it will create.
            particle: CLOUD # The particle it will use.
            speed: 0


Cloud_two:
    mechanics:
        particletwo:
            type: particle
            target:
                type: circle
                radius: 2
                amount: 32
            particle: CLOUD
            speed: 0

Rainbow_tick:
    mechanics:
        particlered:
            type: particle #This calls upon the particle mechanic.
            particle: REDSTONE # Tells the script to use the redstone particle.
            amount: 10 # Tells the script to spawn 10 redstone particles per trigger.
            speed: 0 # At what speed the particles fly outwards from its original position.
            x: 0
            y: 0.75
            z: 0
            color: # The colour your redstone particles will be, note that this can only be used on redstone particles and spell_mob particles.
                red: 252 # R value of RGB color code
                green: 15 # G value of RGB color code
                blue: 3 # B value of RGB color code
            target:
                type: custom # Allows for custom location targeting.
                x: 0 # How many blocks away on the x-axis it should target according to the trigger position. Only when relative is true, otherwise it will target a specific y location within your world.
                y: 3.5 # How many blocks away on the y-axis it should target according to the trigger position. Only when relative is true, otherwise it will target a specific y location within your world.
                z: 0 # How many blocks away on the z-axis it should target according to the trigger position. Only when relative is true, otherwise it will target a specific y location within your world.
                source: false
                relative: true # Makes the x,y,z values be relative to the trigger position.
        particleorange:
            type: particle
            particle: REDSTONE
            amount: 10
            speed: 0
            x: 0
            y: 0.75
            z: 0
            color: # Color goes here.
                red: 250
                green: 144
                blue: 5
            target:
                type: custom
                x: 0
                y: 2.5
                z: 0
                source: false
                relative: true                
        particleyellow:
            type: particle
            particle: REDSTONE
            amount: 10
            speed: 0
            x: 0
            y: 0.75
            z: 0
            color: # Color goes here.
                red: 247
                green: 227
                blue: 5
            target:
                type: custom
                x: 0
                y: 1.5
                z: 0
                source: false
                relative: true
        particlelightgreen:
            type: particle
            particle: REDSTONE
            amount: 10
            speed: 0
            x: 0
            y: 0.75
            z: 0
            color: # Color goes here.
                red: 154
                green: 247
                blue: 5
            target:
                type: custom
                x: 0
                y: 0.5
                z: 0
                source: false
                relative: true                
        particlegreen:
            type: particle
            particle: REDSTONE
            amount: 10
            speed: 0
            x: 0
            y: 0.75
            z: 0
            color: # Color goes here.
                red: 19
                green: 247
                blue: 2
            target:
                type: custom
                x: 0
                y: -0.5
                z: 0
                source: false
                relative: true                
        particlelightblue:
            type: particle
            particle: REDSTONE
            amount: 10
            speed: 0
            x: 0
            y: 0.75
            z: 0
            color: # Color goes here.
                red: 2
                green: 250
                blue: 130
            target:
                type: custom
                x: 0
                y: -1.5
                z: 0
                source: false
                relative: true                
        particleblue:
            type: particle
            particle: REDSTONE
            amount: 10
            speed: 0
            x: 0
            y: 0.75
            z: 0
            color: # Color goes here.
                red: 2
                green: 180
                blue: 250
            target:
                type: custom
                x: 0
                y: -2.5
                z: 0
                source: false
                relative: true
```
### A video representation of what this script will do. 
Soon.

## A potion splash using parabolas
```
potion_throw:
    public: true
    mechanics:
        parabola:
            type: parabola
            source:
                type: caster
                position: BODY
            target: # Location targeter required. End point of parabola
                type: looking_at
                length: 6
            start: throw
            tick: throw_tick
            end: potion_Splash
            height: 5 # Height of parabola
            speed: 3 # Horizontal speed

throw:
    mechanics:
        particle_throw:
            type: particle
            particle: SPELL
            amount: 1
            speed: 0
            x: 0
            y: 0
            z: 0
                

potion_Splash:
    mechanics:
        particle_poof:
            type: particle
            target:
                type: circle
                radius: 3
                amount: 32
            particle: CLOUD
            speed: 0
        particle_splash:
            type: particle
            target:
                type: circle
                radius: 2
                amount: 32
            particle: SPELL_MOB
            color:
                red: 31
                green: 94
                blue: 12
        dealdamage:
            type: damage
            amount: 10
            knockback: true
            preventimmunity: false
            target:
                type: nearby_entities # This will target all nearby enemies within the set range.
                radius: 3 # How many blocks away from the caster it will target.
                height: 3 # How many block up from the caster it will target.
                source: false
        applyeffect:
            type: potion # This will load the potion mechanic.
            effect: POISON # Which potion effect it should use.
            level: 2 # What level the potion effect should be.
            duration: 80 # How long the potion effect will last in ticks
            ambient: true
            particles: true # Whether or not it should show the particle effect of the potion.
            icon: true # Whether or not it should show the icon of the potion effect. (only for players)
            target:
                type: nearby_entities
                radius: 3
                height: 3
                source: false


throw_tick:
    mechanics:
        particle_tick:
            type: particle
            target:
                type: circle
                radius: 2
                amount: 32
            particle: SPELL_MOB
            color: # Color goes here.
                red: 31
                green: 94
                blue: 12
```
### A video representation of what this script will do. 
Soon.

Now we know how to use use the right script lay out and how to colour certain particles, so we'll move on to the next shape mechanic. In this next example we will be covering how to set up the helix mechanic and how to use the healing mechanic.