---
order: 2
---

# 💫 Built-in Skills

MythicLib has a huge registry of about 90 default skills which combines MMOItems pre-6.7 abilities and MMOCore pre-1.9 skills.

Skills marked with <Badge type="info" text="mmocore" /> are only available when MMOCore is installed.

::: tip
Use CTRL+F to look for an ability with certain keywords.
:::

## Skills cast onto a location

| Ability  | Ability Description  | Ability Modifiers|
| ----------------- | ------------------------------------------------------- | ----------------------------------- |
| Arcane Hail| Arcane projectiles shower target area, dealing damage over time | damage, duration, radius   |
| Black Hole | Casts a black hole which attracts nearby units | radius, duration  |
| Blink    | Teleports you to target location in the blink of an eye  | range   |
| Contamination     | Contaminates target area for Xsec, dealing damage over time     | damage, duration  |
| Corrosion| Poisons nearby entities.    | duration, amplifier, radius|
| Corrupt  | Corrupts target area, dealing damage and wither| damage, duration, amplifier|
| Freeze | Freezes nearby mobs for X seconds.   | duration, amplifier, radius|
| Freezing Curse    | After a short delay, nearby enemies are frozen within target area | duration, damage, radius, amplifier  |
| Ice Spikes| Ice spikes summon from the ground, damaging and slowing hit enemies. | damage, slow |
| Ignite | Sets nearby entities on fire. | duration, max-ignite, radius |
| Life Ender | A devastating fire comet strikes the ground  | damage, knockback, radius  |
| Lightning Beam    | Lightning strikes the ground and damage nearby enemies.  | radius, damage    |
| Minor Explosion | A powerful burst deals damage to nearby enemies. | duration, damage, knockback, radius |
| Power Mark| A mark spreads around target location. Any damage dealt within marked zone accumulates damage. The mark explodes after X seconds, dealing X% of accumulated damage, stunning & knocking back nearby enemies. The higher the damage, the longer the stun. | stun, ratio, duration |
| Snowman Turret    | Creates a snowman tower that shoots nearby enemies    | duration, damage, radius   |

## Skills cast onto an entity

| Ability| Ability Description  | Ability Modifiers|
| --------------- | ------------------------------------------------------- | ----------------------------------- |
| Blind  | Blinds your opponent (vanilla potion effect)    | duration|
| Bloodbath| Takes food points from the target.  | amount  |
| Burn   | Burns the target down for a few seconds.| duration|
| Combo Attack     | Repeatedly slashes the target for X total damage. | damage, count|
| Confuse| Turns your opponent's camera by 90°      | \---    |
| Control | Slows the target. When left clicking, knocks him back in target direction.  | knockback, duration   |
| Death Mark      | The mark deals X damage split on Ysec (+slow). | duration, damage, amplifier|
| Deep Wound| Punctures target, damaged is increased based on target's missing health     | damage, extra|
| Furtive Strike   | Deals damage, greatly increased if target is isolated | damage, extra, radius |
| Greater Healings  | Better version of //Minor Healings//. | heal |
| Human Shield     | Reduces damage taken by ally, and redirects to you a portion of the blocked damage. | reduction, redirect, duration, low |
| Magma Fissure     | Casts a targeted magma fissure (sets on fire and deals damage)  | ignite, damage    |
| Minor Healings    | Heals for X health target/self if crouching.  | heal |
| Poison | Poisons your target for a short period of time.| duration, amplifier |
| Regen Ally | Gives X health back to an ally over Y seconds| heal, duration    |
| Shock  | Rapidly shakes your opponent's camera (useless for mobs) | duration|
| Slow   | Reduces your opponent's movement speed.  | duration, amplifier |
| Smite    | Calls lightning upon an evil foe   | damage  |
| Sparkle  | Sparkles spring from your opponent, damaging nearby entities (capped)    | damage, radius, limit      |
| Starfall | Casts a damaging falling star onto your target.| damage  |
| Stun   | Makes your opponent unable to move.   | duration|
| Tactical Grenade  | Casts a wave of land strikes which eventually hits your target  | radius, knock-up, damage   |
| Targeted Fireball | Casts a targeted damaging fireball which ignites your target    | damage, ignite    |
| Telekinesy| Target's movement is taken over. Left click to knock him back. | duration, knockback |
| Weaken  | Weakens target, increasing damage taken. Inherited from MMOCore | ratio, duration |
| Weaken Target   | Same as above, inherited from MMOItems.     | duration, extra-damage     |
| Wither | Temporarily applies Wither to target entity.    | duration, amplifier |

## Item Skills

Skills which require the caster to hold an item.

| Ability  | Ability Description| Ability Modifiers |
| ----------------- | ------------------------------------------------------------------------ | --------------------------------------------- |
| Item Bomb| You throw a bomb, damaging and slowing entities hit after a short delay  | slow-duration, slow-amplifier, damage, radius |
| Item Throw | Throws your item, damaging the first enemy it hits    | damage, force     |

## Skills with no target

These skills do not require a target entity or location, and can be cast at any time.

| Ability  | Ability Description| Ability Modifiers |
| ----------------- | ------------------------------------------------------------------------ | --------------------------------------------- |
| Arcane Rift| Casts a damaging void rift which slows enemies on it  | damage, duration, amplifier, speed   |
| Blizzard | Casts a flurry of damaging snowballs  | duration, damage, inaccuracy, force  |
| Bouncy Fireball   | A bouncy Mario fireball which explodes on 3rd impact  | damage, ignite, speed, radius |
| Bunny Mode | You bounce on ground      | duration, jump-force, speed|
| Burning Hands     | Summons a cone of deadly flames from the tip of your fingers    | damage, duration  |
| Chicken Wraith    | Casts a flurry of chicken eggs, dealing damage | duration, damage, inaccuracy, force  |
| Circular Slash    | Damages nearby enemies and knocks them back  | damage, radius, knockback  |
| Corrupted Fangs   | Casts a damaging spell just like the Evoker  | damage  |
| Cursed Beam| A deadly cursed projectile which withers nearby enemies. | damage, duration  |
| Earthquake | A seismic wave which damages and slows down hit enemies  | damage, duration, amplifier|
| Empowered Attack | Charges your weapon with lightning. Your next attack deals extra damage and spreads onto nearby enemies | radius, ratio, extra  |
| Evade    | You become immune to damage till you attack again/end of duration | duration|
| Explosive Turkey  | Summons a chicken which explodes upon block contact   | damage, radius, knockback  |
| Fire Meteor| Summons a deadly fire meteor from the sky    | damage, knockback, radius  |
| Fire Rage | Slow down and arm your hands with three fire bolts.      | count, damage, ignite |
| Fire Storm| Fire projectiles cast on the target, dealing damage.     | ignite, damage |
| Fireball | Damaging & igniting fireball. Shatters into damaging flame shards | damage, ignite, ratio |
| Firebolt | Casts a simple damaging firebolt.  | damage, ignite    |
| Firefly  | Dashes to your cursor, exploding upon contact with an enemy     | damage, duration, knockback|
| Frog Mode| You bounce on water for X seconds  | duration, jump-force, speed|
| Frozen Aura| During X seconds, nearby enemies are slowed down for 2sec| duration, amplifier, radius|
| Grand Heal | Restores some health to you and nearby players | heal, radius      |
| Heal     | Restores some health      | heal    |
| Heavy Charge      | You charge forward, dealing damage and knockback to the first entity hit | damage, knockback |
| Hoearthquake      | An earthquake hoes grass on its path  | \---    |
| Holy Missile      | Summons a damaging holy missile    | damage  |
| Ice Crystal| Casts a damaging ice crystal which slows the first enemy it hits| duration, amplifier, damage|
| Leap     | Powerfully leaps in the air | force   |
| Light Dash | Dashes forwards, dealing damage to hit entities| damage, length    |
| Magical Path      | Allows flight for a set period of time| duration|
| Magical Shield    | Reduces damage taken by nearby entities by X% for Y seconds     | power, radius, duration    |
| Overload | Summons a lightning shockwave around you, dealing damage | damage, radius    |
| Present Throw     | Casts an explosive christmas present  | damage, radius, force      |
| Shadow Veil| You vanish for a few seconds (PvP only)      | duration|
| Shockwave| Summons a shockwave which knocks up enemies hit| knock-up, length  |
| Shulker Missile   | Casts multiple deadly shulker missiles| damage, effect-duration    |
| Sky Smash| Powerful strikes which damage & knock up hit entities | knock-up, damage  |
| Swiftness| Increases your movement speed temporarily    | duration, amplifier |
| Throw Up | Throw damaging pieces of rotten flesh | damage, duration  |
| Thrust   | Thrust forwards with your sword, dealing damage| damage  |
| TNT Throw| (Block damage\!) Casts a primed TNT| force   |
| Void Zapper | Casts a linear projectile which bounces on surfaces, inflicting damage and knockback | damage, knockback, length, max, extra |
| Warp     | Point the ground & teleport to target location. | range |

## Passive Skills

These skills cannot be actively cast - they are passively triggered by specific events, like player attacks.

| Skill   | Description | Modifiers    |
|------------------|---------------------------------------------------------------------------------------------------------|-----------------------|
| Ambers  | Ambers drop when dealing magic damage. Grants X% [max mana](../../mmocore/misc/resources.md) back when picked up.  <Badge type="info" text="mmocore" />     | percent      |
| Backstab| Backstabs deal X% extra damage.| extra |
| Fire Berserker   | Passively deals increased damage when on fire.  | extra |
| Neptune's Gift   | [Resource](../../mmocore/misc/resources.md) regeneration is increased when standing in water. <Badge type="info" text="mmocore" /> | extra |
| Sneaky Picky     | Deal additional damage when delivering the first blow during a fight (when entering [Combat Logging](../../mmocore/features/combat.md)). <Badge type="info" text="mmocore" /> | extra |
| Vampirism| 10% of the attack damage is given back as health. | drain |
