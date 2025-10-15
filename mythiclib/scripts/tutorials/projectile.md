## A simple projectile
```
Bullet: # This is a script name, this can be whatever you'd like. This is also the skill ID and can be cast with the command */ml cast BULLET*
    public: true # This allows for the script to be used by MMOCore and casted with /ml cast
    mechanics: 
        Projectile: # This is a mechanic registry name, this name can be whatever you want. 
            type: projectile # This will tell the script to use the projectile mechanic.
            source: # This allows you to set where the projectile should come from. This is Optional.
                type: caster # Sets the caster as source of the projectile.
                position: EYES # Where on the caster it should come from.   
            tick: bullet_tick #The script it will execute every tick.
            hit_entity: bullet_hit # The script execute when hitting an entity.
            hit_block: bullet_cancel # The script execute when hitting a block.
            stop_on_block: true # Whether or not to stop the Projectile when it hits a block.
            offense: true # Makes this script an offensive skill, meaning it will not hit party/guild members.
            hits: 1 # The maximum amount of entities this projectile will hit before dissappearing.
            ignore_passable: false # If it should ignore passable blocks.
            speed: 3 # How fast the Projectile travels.
            size: 0.1 # How big the projectile appears when using particles.
            step: 0.2 # Distance between two calls of the tick script.
            life_span: 60 # How long this projectile will last. In ticks.
           

bullet_tick: # This is another script name, this was called upon in the previous script.
    mechanics:
        showparticlesone: # Another mechanic registry name.
            type: particle # This will tell the script to use the particle mechanic.
            particle: COMPOSTER # What particle should be shown.
            amount: 4 # How many particles it should show.
            x: .1 # This sets how far the particles can move on the x-axis on both sides around the source.
            y: .1 # This sets how far the particles can move on the y-axis on both sides around the source.
            z: .1 # This sets how far the particles can move on the z-axis on both sides around the source.

bullet_cancel:
    mechanics:
        showparticlestwo: # Another mechanic registry name.
            type: particle # This will tell the script to use the particle mechanic. 
            particle: VILLAGER_ANGRY # What particle should be shown.
            amount: 10 # How many particles it should show.
            x: .5 # This sets how far the particles can move on the x-axis on both sides around the source.
            y: .5 # This sets how far the particles can move on the y-axis on both sides around the source.
            z: .5 # This sets how far the particles can move on the z-axis on both sides around the source.

bullet_hit: 
    mechanics:
        dealdamage: # Another mechanic registry name.
            type: damage # This will tell the script to use the damage mechanic. 
            amount: 10 # How much damage it should deal.
            knockback: true # Whether or not to knock the enemy back when damaged.
            preventimmunity: false # Whether or not to ignore immunity frames.
            

```
### A video representation of what this script will do. 
Soon.

Now that we have a general understanding of the projectile mechanic and its features we can move on to using more mechanics that get triggered by the projectile hitting an entity. In this next example we will be covering how to put delay in script execution, how to make a script execute another script and the teleportation mechanic.

## A more advanced projectile
```
bullet_hell:
    public: true
    mechanics:
        Projectile:
            type: projectile
            source:
                type: caster
                position: EYES
            tick: bullets_tick
            hit_entity: first_bullet 
            hit_block: cancel 
            stop_on_block: true
            offense: true
            hits: 1 
            ignore_passable: false 
            speed: 5 
            size: 0.1
            step: 0.2 
            life_span: 60 # In ticks
           
            
bullets_tick:
    mechanics:
        showparticles:
            type: particle
            particle: FLAME
            amount: 10
            x: .2
            y: .2
            z: .2


            
cancel:
    mechanics:
        showparticles:
            type: particle
            particle: VILLAGER_ANGRY
            amount: 10
            x: .5
            y: .5
            z: .5

first_bullet: #This is a secondary projectile script that will be executed after hitting an enemy.
    public: true
    mechanics:
        Location_one:
            type: teleport # This tells the script to use the teleportation mechanic.
            y_offset: 0 # How far up from the target location should the target be teleported.
            target: # Who to teleport.
                type: caster
            target_location: # Where to teleport the target to.
                type: custom # What kind of location targeter to use.
                x: 5 # Where to teleport the target to on the x-axis.
                y: 6 # Where to teleport the target to on the y-axis.
                z: 0 # Where to teleport the target to on the z-axis.
                source: false # 
                relative: true # Whether or not the target location should be relative to the target. location.
        delay:
            type: delay # This tells the script to set a delay between the previous and next mechanic.
            amount: 5 # How long the delay should be ticks.
        Bullet1:
            type: projectile
            source: # Optional. Location targeter required
                type: custom
                x: 5
                y: 6
                z: 0
                source: false
                relative: true
            hit_entity: bullethitone
            tick: bullet_tick
            hit_block: cancel
            stop_on_block: true
            stop_on_entity: true
            offense: true
            hits: 1 # Maximum amount of hit entities. Will disappear on last entity hit
            ignore_passable: false # It it should ignore passable blocks
            speed: 5 # 1 by default
            size: 0.1
            step: 0.2 # Distance between two calls of the tick script
            life_span: 60
            target:
                type: target
                position: EYES


bullethitone:
    mechanics:
        dealdamage:
            type: damage
            amount: 10
            knockback: false
            ignore_immunity: false
        showparticles:
            type: particle
            particle: LAVA
            amount: 5
        delay:
            type: delay
            amount: 5
        secondbullet:
            type: script # This mechanic will execute another script.
            name: second_bullet # The name of the script that has to be executed.
            iterations: 1 # How many times the script should be executed.
            counter: 'iteration_count2' # 


second_bullet:
    public: true
    mechanics:
        Location_two:
            type: teleport
            y_offset: 0
            target:
                type: caster
            target_location:
                type: custom
                x: -5
                y: 6
                z: 0
                source: false
                relative: true
        delay:
            type: delay
            amount: 5
        Bullet2:
            type: projectile
            source: # Optional. Location targeter required
                type: custom
                x: -5
                y: 6
                z: 0
                source: false
                relative: true
            hit_entity: bullethittwo
            tick: bullet_tick
            hit_block: cancel
            stop_on_block: true
            stop_on_entity: true
            offense: true
            hits: 1 # Maximum amount of hit entities. Will disappear on last entity hit
            ignore_passable: false # It it should ignore passable blocks
            speed: 5 # 1 by default
            size: 0.1
            step: 0.2 # Distance between two calls of the tick script
            life_span: 60
            target: # Entity targeter required
                type: target
                position: EYES

                
bullethittwo:
    mechanics:
        dealdamage:
            type: damage
            amount: 10
            knockback: false
            ignore_immunity: false
        delay:
            type: delay
            amount: 5
        thirdbullet:
            type: script
            name: third_bullet
            iterations: 1
            counter: 'iteration_count3'

third_bullet:
    mechanics:
        Location_three:
            type: teleport
            y_offset: 0
            target:
                type: caster
            target_location:
                type: custom
                x: 0
                y: 9
                z: 0
                source: false
                relative: true
        delay:
            type: delay
            amount: 5
        Bullet3:
            type: projectile
            source: # Optional. Location targeter required
                type: custom
                x: 0
                y: 9
                z: 0
                source: false
                relative: true
            hit_entity: bullethitthree
            tick: bullet_tick
            hit_block: cancel
            stop_on_block: true
            stop_on_entity: true
            offense: true
            hits: 1 # Maximum amount of hit entities. Will disappear on last entity hit
            ignore_passable: false # It it should ignore passable blocks
            speed: 6 # 1 by default
            size: 0.1
            step: 0.2 # Distance between two calls of the tick script
            life_span: 60
            target: # Entity targeter required
                type: target
                position: EYES    


bullethitthree:
    mechanics:
        dealdamage:
            type: damage
            amount: 10
            knockback: false
            ignore_immunity: false
        back_to_start_location:
            type: teleport
            target:
                type: caster
            target_location:
                type: custom
                x: 5
                y: 0
                z: 0
                source: false
                relative: true
```
### A video representation of what this script will do. 
Soon.

Now that we know how to implement a good deal of mechanics like damage and particles it's time to move on to the next shape mechanic. In this next example we will be covering how to set up the parabola mechanic and how to use colored particles.
