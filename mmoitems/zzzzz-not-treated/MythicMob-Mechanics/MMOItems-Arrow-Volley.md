Similar to the mythicmobs' arrow volley mechanic, this mechanic fires forth a bunch of arrows at desired spread, from the desired offset. However, **this scales the arrows with stats of the player** such that the arrows fired have the same effect of firing it manually with a bow.

Note that the arrows will get stat bonuses from all player equipment, including any weapon the player is currently wielding, even if its not a bow.


Attributes
----------

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

  
===== Offset Options =====  
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

(See example below for usage)

Examples
--------

      Skills:
      - MMOItemsVolley{amount=10;spread=30;fireTicks=20;removeDelay=100;velocity=20;syo=1.2;sso=2} @Forward{f=15.0;y=0.0}

Makes the player fire a bunch of arrows from their right side. Each arrow deals the same damage as if the player had fired them from their bow.

      Skills:
      - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation
      - delay 2
      - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation
      - delay 2
      - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation
      - delay 2
      - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation

A dreadful arrow rain of Black Arrow MMOItems that are each scaled to do only 20% of the damage they would do normally. _Requies other plugins like XBow2RL for the arrow item to matter._