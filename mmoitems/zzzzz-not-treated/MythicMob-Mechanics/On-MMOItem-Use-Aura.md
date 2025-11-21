Similar to the mythicmobs' onShoot Aura that fires when you fire a bow, this aura will trigger when the player uses any of the special attacks of MMOItems weapons (not when they hit a monster, when they fire)

Note that this will never trigger for monsters, as monsters cannot use special attacks.

Attributes
----------

| Attribute           | Aliases | Description                                                                                                                                                                        | Default Value |
|---------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| skill | s | Name of the skill that will run when the aura triggers, the **called skill**. | (none) |
| weapons | w | What kind of weapons are you listening for (Comma separated list with no spaces)? CROSSBOW, GAUNTLET, LUTE, MUSKET, STAFF, or WHIP | MUSKET |
| cancelEvent | ce | Cancels the event, preventing the weapon from actually firing. | false |

Called Skill Metadata
----------
| Meta   | Description               |
|--------|---------------------------|
| Caster | No change, the caster of the onMMOItemUse mechanic |
| Target | No change, the target receiving the onMMOItemUse aura. |
| Trigger | Enemy that will get hit by the attack of this weapon, only supported for GAUNTLET, MUSKET, STAFF, and WHIP. |
| Origin | No change, wherever the origin was previously. |

(See example below for usage)

Examples
--------

      Skills:
      - onMMOItemUse{auraName=Flash;d=600;c=1;s=ComboPunch;w=GAUNTLET;;cE=true} @Self
      
    ComboPunch: 
      Skills:
      
      # Punch
      - velocity{m=set;x=0.15;y=0.02;z=0} @Trigger
      - mmodamage{a=7;preventImmunity=true;t=PHYSICAL,SKILL} @Trigger
      - effect:sound{s=entity.player.attack.knockback;volume=1.2;pitch=1.25}
      - effect:particles{particle=largeexplode;amount=1;hS=0.4;vS=0.2;speed=0.01;y=1.3} @Trigger
      - delay 5
      
      # Punch
      - velocity{m=set;x=-0.15;y=0.02;z=0} @Trigger
      - mmodamage{a=7;preventImmunity=true;t=PHYSICAL,SKILL} @Trigger
      - effect:sound{s=entity.player.attack.knockback;volume=1.2;pitch=1.25}
      - effect:particles{particle=largeexplode;amount=1;hS=0.4;vS=0.2;speed=0.01;y=1.3} @Trigger
      - delay 5
      
      # Punch
      - velocity{m=set;x=0.15;y=0.02;z=0} @Trigger
      - mmodamage{a=7;preventImmunity=true;t=PHYSICAL,SKILL} @Trigger
      - effect:sound{s=entity.player.attack.knockback;volume=1.2;pitch=1.25}
      - effect:particles{particle=largeexplode;amount=1;hS=0.4;vS=0.2;speed=0.01;y=1.3} @Trigger
      - delay 10
      
      # Throw
      - throw{velocity=20;velocityY=7} @Trigger
      - mmodamage{a=13;preventImmunity=true;t=PHYSICAL,SKILL} @Trigger
      - effect:sound{s=entity.player.attack.knockback;volume=1.2;pitch=1}
      - effect:sound{s=entity.player.attack.knockback;volume=1.2;pitch=0.5}
      - effect:particles{particle=largeexplode;amount=1;hS=0.4;vS=0.2;speed=0.01;y=1.3} @Trigger

The next time the player right-clicks with a gauntlet, they will execute a combo punch.


      Skills:
      - onMMOItemUse{d=300;s=GreenExplosion;w=STAFF,WHIP} @Self

Makes staff attacks cause green explosions for the next 15 seconds