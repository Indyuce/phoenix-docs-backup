---
order: 2
---

# 💥 Triggers

When using custom scripts in MMOItems and MMOCore you might sometimes specify when a specific script should be executed: when damaging an entity, when being damaged, when crouching etc. This is done using trigger types.



## Available Triggers

These are the trigger types (they used to be called _casting modes_ in MMOItems) that you will be able to use in MMO plugins to define when some skill is supposed to run.

Some triggers are only available when MMOCore is installed. As long as MMOCore is installed, you can freely use them in any of the MMO plugins.

| Skill Trigger | Description | Trigger Target | Trigger Target Block |
|---------------|-------------|----------------|----------------------|
| **Combat Triggers** |  |  |  |
| KILL_ENTITY | Activates the skill when a player kills an entity | The killed entity | \- |
| KILL_PLAYER | Activates the skill when a player kills an player | The killed player | \- |
| ATTACK | Activates the skill when the player attacks something | The entity the player attacked | \- |
| DAMAGED | Activates the skill when the player takes damage | \- | \- |
| DAMAGED_BY_ENTITY | Activates the skill when the player takes damage from an entity | The entity that damaged the player | \- |
| DEATH | Activates the skill when the player dies | \- | \- |
| **Projectile Triggers** |  |  |  |
| SHOOT_TRIDENT | When the player shoots a trident | The projectile | \- |
| TRIDENT_TICK | Activates every tick when a trident is still midair | The projectile | \- |
| TRIDENT_LAND | When a trident lands on the ground | The projectile | \- |
| TRIDENT_HIT | When a thrown trident hits an entity | The hit entity | \- |
| SHOOT_BOW | When the player fires an arrow | The projectile | \- |
| ARROW_TICK | Activates every tick when an arrow is still midair | The projectile | \- |
| ARROW_LAND | When an arrow lands on the ground | The projectile | \- |
| ARROW_HIT | When a fired arrow hits an entity | The hit entity | \- |
| **Click Triggers** |  |  |  |
| RIGHT_CLICK | On player right click | \- | \- |
| LEFT_CLICK | On player left click | \- | \- |
| SHIFT_RIGHT_CLICK | On player right click while sneaking | \- | \- |
| SHIFT_LEFT_CLICK | On player left click while sneaking | \- | \- |
| **Block Triggers** |  |  | \- |
| BREAK_BLOCK | Activates the skill when a player break block | \- | Location of mined block |
| PLACE_BLOCK | Activates the skill when a player place block | \- | Located of placed block |
| **MMOCore Triggers** |  |  |  |
| ENTER_COMBAT | Activates the skill when a player enter combat | \- | \- |
| QUIT_COMBAT | Activates the skill when a player quit combat | \- | \- |
| **Item Triggers** |  |  |  |
| DROP_ITEM | Activates the skill when a player press Q | The dropped item | \- |
| SHIFT_DROP_ITEM | Activates the skill when a player press Shift + Q | The dropped item | \- |
| SWAP_ITEMS | Activates the skill when a player press F | \- | \- |
| SHIFT_SWAP_ITEMS | Activates the skill when a player press Shift + F | \- | \- |
| ~~EQUIP_ARMOR~~ | Activates the skill when a player enquip armor | The player | \- |
| ~~UNEQUIP_ARMOR~~ | Activates the skill when a player unenquip armor | The player | \- |
| **Miscellaneous** |  |  |  |
| LOGIN | Activates the skill when a player logins | \- | \- |
| SNEAK | Activates the skill when a player sneaks | \- | \- |
| TELEPORT | Activates the skill when a player teleport | \- | The target teleport location |
| TIMER | Casts the skill every X ticks | \- | \- |


## When a script is triggered

Some trigger types provide special properties to the script they trigger. For instance, when using the `ATTACK` trigger type, the `<target>` variable can be accessed to work with the attack target. `<attack.damage>` returns the attack damage. More precisely, some internal variables only exist when specific trigger types are used.

Trigger types featuring entities/projectiles like `ATTACK`, `DAMAGED`, `DAMAGED_BY_ENTITY`, `KILL_ENTITY`, `SHOOT_TRIDENT`, `ARROW_TICK` etc. allow the user to use the `<target>` internal variable to access the target entity. This also unlocks the `target` entity targeter as well as the `target_location` location targeter for instance.

Trigger types featuring positions like `TRIDENT_LAND` or `ARROW_HIT` unlock the `target_location` location targeter as well as the `<target_location>` internal variable for example.

Some triggers like `TIMER` or `RIGHT_CLICK` don't unlock any internal variable.

`ATTACK` is the only trigger type which unlocks the `<attack>` internal variable as well as special mechanics (`multiply_damage`) or conditions (`has_damage_type`).
