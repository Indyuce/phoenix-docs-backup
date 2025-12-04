


# ⚔️ Damage

## PlayerAttackEvent
A `PlayerAttackEvent` bukkit event is called everytime a player deals damage to another entity. The event contains all the info about the player attacking, the damage being dealt and the attack target.

`AttackMetadata` contains:
- the player attacking
- the entity being attacked
- a cached map of the player statistics which was generated when the player cast the skill/attack
- an instance of DamageMetadata

`DamageMetadata` handles all the damage calculations. When accessing this class you can:
- increase any damage due to a specific type by X%
- add extra elemental/typed damage packets
- get all the damage values

A damage metadata is composed of a set of damage packets. A damage packet is one double indicating the amount of damage dealt as well as a set of damage types. This packet method lets MythicLib distinguish damage sources and only apply modifiers to some of them.

Using damage packets, you can have your skill deal like 10 weapon-physical damage + 15 skill-magical damage, under one DamageMetadata. And if the player happens to have a stat like +50% Skill Damage, this stat will only apply to the packets which have at least SKILL as damage type! This allows for insane on-hit extra RPG styled damage calculations. Example use:

```java
@EventHandler
public void onAttack(PlayerAttackEvent event) {
    AttackMetadata attack = event.getAttack();
    DamageMetadata damage = attack.getDamage();

    damage.add(10, DamageType.WEAPON, DamageType.PHYSICAL); // add 10 weapon-physical damage
    damage.multiplicativeModifier(1.5, DamageType.SKILL); // increase skill damage by 50%
    damage.collectTypes().foreach(type -> whatever); // collect all damage types present in the damage packets
}
```

## Using DamageManager
It's the class MythicLib uses to centralize all the player attacks from MMOItems and MMOCore. The following code snippet can be used to force a player to deal damage to a certain entity. You first have to specify the damage you want to deal, as well as the damage types. Then cache the player's statistics before defining the AttackMetadata and registering it using MythicLib's damage manager.
```java
PlayerData playerData = /* TODO */; // player attacking

DamageMetadata damage = new DamageMetadata(12, DamageType.SKILL, DamageType.MAGIC);
StatMap.CachedStatMap statMap = playerData.getMMOPlayerData().getStatMap().cache(EquipmentSlot.MAIN_HAND);
AttackMetadata attack = new AttackMetadata(damage, statMap);

boolean knockback = true; // If you want your attack to deal knockback
LivingEntity target = ...; // Entity being targeted

MythicLib.plugin.getDamage().damage(damage, target, knockback); // Finally deal damage
```

## Compatibility with other plugins which have a damage system
Take any other plugin which implement magic skills like Fabled or Heroes. MMOCore needs a way to detect when a player damages an entity using a skill, so that it can apply the `Skill Damage` stat for instance. It's what the `DamageManager` class is all about: monitoring all damage dealt by players.

Other plugins with have a damage system need to register their damage info in MythicLib whenever an entity is damaged by a player, so that MythicLib knows that some custom damage is being applied. If MythicLib detects player damage but cannot find the source plugin, it is considered a melee weapon attack.

In order to register that damage info in MythicLib, you need to create an instance of the `DamageHandler` class and register it in the `DamageManager` instance of MythicLib using the following method:
`MythicLib.plugin.getDamage().registerHandler(damageHandler);`\
A damage handler can be registered at any time **after MythicLib has loaded**.

## Damage Mitigation

Whenever a mitigation type is triggered by a player, an instance of `DamageMitigationEvent` is called. You can retrieve the mitigation type using `event#getType()`. This event is cancellable.

## On-Hit Effects

Whenever an on-hit effect is triggered, an instance of `OnHitEffectEvent` is called. You can retrieve the on-hit effect using `event#getEffect()`. This event is cancellable.

## Damage Indicators

When an indicator displays on an entity, an instance of `IndicatorDisplayEvent` is called. You can retrieve the indicator message using `event#getMessage()` and set it using `event#setMessage(String)`. This event is cancellable.
