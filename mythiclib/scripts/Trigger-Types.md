These are the trigger types (also used to be called casting modes in MMOItems) that you will be able to use in MMOCore and MMOItems to define when some skill is supposed to run.

Some triggers are only available when MMOCore is installed, but this doesn't mean they are limited to MMOCore, you can use them inside of MMOItems item abilities as well.

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

