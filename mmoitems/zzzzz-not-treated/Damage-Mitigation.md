Damage mitigation in MMOItems is separated in three mechanics: **Blocking, Dodging and Parrying**. Any numeric value in that page can be edited in the main **MythicLib** plugin config file (_mitigation_ config section). In order to enhance compatibility with MMOCore, damage mitigation was moved over to MythicLib.

Whenever an attack damage is being lowered by mitigation, a particle effect plays in front of the player, and he is sent a message on the action bar (or via chat).

## Blocking
When blocking a melee or projectile attack, a player reduces damage taken by a significant amount. Both the block chance and block power (percentage of damage you are blocking) can be increased by items. Blocking power has a default value and a cap, meaning that if a player has no item giving him extra block power, he will block at least 20% of the damage taken. Blocking power can't exceed 75%.
The chance of blocking an attack is determined by the _Block Rating_ stat.
```
STEEL_BREASTPLATE:
    material: IRON_CHESTPLATE
    block-power: 10
    block-rating: 5
```

## Dodging
When dodging a melee or projectile attack, a player entirely **negates** damage taken and performs a quick dash backwards, allowing him to escape from the fight. The chance of dodging an attack is capped at 80%.

```
SWIFT_LEATHER_BOOTS:
    material: LEATHER_BOOTS
    dodge-rating: 10
```

## Parrying
Just like dodging, parrying entirely negates attack damage and knocks the attacker back.\
The knockback force can be edited in the config file.
```
DWARVEN_SHIELD:
    material: SHIELD
    parry-rating: 10
```

## Mitigation Cooldown Reduction
Every mitigation stat also features a cooldown reduction stat. By default, a player cannot dodge, parry or block more than one attack every few seconds. These cooldown stats lower that delay, which can be really useful if the player is running low on health.
```
ROGUE_AMULET:
    material: RED_DYE
    dodge-cooldown-reduction: 40
```