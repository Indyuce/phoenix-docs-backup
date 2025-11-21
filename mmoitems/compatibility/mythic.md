---
order: 2
---


# 🧟 MythicMobs

## Arrow Volley Mechanic

Similar to the mythicmobs' arrow volley mechanic, this mechanic fires forth a bunch of arrows at desired spread, from the desired offset. However, **this scales the arrows with stats of the player** such that the arrows fired have the same effect of firing it manually with a bow.

Note that the arrows will get stat bonuses from all player equipment, including any weapon the player is currently wielding, even if its not a bow.


| Attribute           | Aliases | Description                                                                                                                                                                        | Default Value |
|---------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| amount | arrows, a | Number of arrows that will be fired. | 20 |
| spread | s | Spread of the arrows, use large values to notice. | 45 |
| fireticks| ft, f | Ticks the arrows will remain on fire. | 0 |
| removeDelay | rd, r | Arrows will be removed after this many ticks. | 200 |
| velocity | v | Speed of the arrows. | 20 |
| statsScale | ss | Multiply the damage dealt by each arrow by this factor. | 1 |
| scalePerArrow | spa | Stats Scale attribute supports placeholders, setting this to true will parse those placeholders again for every arrow. | false |
| arrowItem | item. ai | Filter of the item to fire, preferably an arrow. Important for some plugins. | v ARROW ~ |
| fullEvent | fe | Setting this to true will cause the arrows to call the EntityShootBowEvent event for every arrow, which makes ALL plugins detect it and perform operations as if the player had actually fired a bow like this. With the default value of 'false', only MMOItems runs these calculations, which means that if you have other plugins like mcMMO they will not apply their effects to arrows, which might be desirable or not per your situation. | false |


These options affect the location the arrows are fired from, though they will always be directed at the target of the skill.

| Attribute        | Aliases       | Description                                                | Default Value |
|------------------|---------------|------------------------------------------------------------|---------------|
| fromOrigin | fo | Arrows are fired from the origin of the skill. | false |
| startXOffset | sxo | Shifts arrow spawn in the X coordinate. | 0 |
| startYOffset | syo | Shifts arrow spawn in the Y coordinate. | 3 |
| startZOffset | szo | Shifts arrow spawn in the Z coordinate. | 0 |
| startFOffset | sfo | Shifts arrow spawn forward relative to the caster. | 0 |
| startSOffset | sso | Shifts arrow spawn rightward relative to the caster. | 0 |

_Note that this mechanic only works for players, and will reduce to the MythicMobs' usual ArrowVolley if fired by a NPC or monster, and will only support the parameters from that mechanic (most notably, the offsets for the spawn location of arrows won't work)._

<details>
<summary>Example Usage</summary>

A dreadful arrow rain of Black Arrow MMOItems that are each scaled to do only 20% of the damage they would do normally. _Requires other plugins like XBow2RL for the arrow item to matter._

```yml
ExampleSkill:
  Skills:
  - MMOItemsVolley{amount=10;spread=30;fireTicks=20;removeDelay=100;velocity=20;syo=1.2;sso=2} @Forward{f=15.0;y=0.0}
```

Makes the player fire a bunch of arrows from their right side. Each arrow deals the same damage as if the player had fired them from their bow.
```yml
ExampleSkill2:
  Skills:
  - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation
  - delay 2
  - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation
  - delay 2
  - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation
  - delay 2
  - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation
```
</details>

## onMMOItemUse Aura

Similar to the mythicmobs' onShoot Aura that fires when you fire a bow, this aura will trigger when the player uses any of the special attacks of MMOItems weapons (not when they hit a monster, when they fire)

Note that this will never trigger for monsters, as monsters cannot use special attacks.

| Attribute           | Aliases | Description                                                                                                                                                                        | Default Value |
|---------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| skill | s | Name of the skill that will run when the aura triggers, the **called skill**. | (none) |
| weapons | w | What kind of weapons are you listening for (Comma separated list with no spaces)? CROSSBOW, GAUNTLET, LUTE, MUSKET, STAFF, or WHIP | MUSKET |
| cancelEvent | ce | Cancels the event, preventing the weapon from actually firing. | false |

#### Called Skill Metadata
| Meta   | Description               |
|--------|---------------------------|
| Caster | No change, the caster of the onMMOItemUse mechanic |
| Target | No change, the target receiving the onMMOItemUse aura. |
| Trigger | Enemy that will get hit by the attack of this weapon, only supported for GAUNTLET, MUSKET, STAFF, and WHIP. |
| Origin | No change, wherever the origin was previously. |

(See example below for usage)

<details>
<summary>Example Usage</summary>

The next time the player right-clicks with a gauntlet, they will execute a combo punch.
```yml
ExampleSkill:
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
```

Makes staff attacks cause green explosions for the next 15 seconds

```yml
ExampleSkill2:
  Skills:
  - onMMOItemUse{d=300;s=GreenExplosion;w=STAFF,WHIP} @Self
```
</details>


## Drop Tables

You can add items from MI to MythicMobs drop tables: more info on [this page](Item%20Drop%20Tables#adding-mmoitems-to-mythicmobs-drop-tables).