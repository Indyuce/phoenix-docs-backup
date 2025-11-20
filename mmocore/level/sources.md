# 🪴 Experience Sources

An experience source gives you experience for certain professions when certain events occur. Each experience source has its own specific parameters that you can specify in the config with `exp_source_name{param1=P1;param2=p2..}`. You must specify the parameter `amount=min-max` corresponding to the bounds between which the amount of experience will be randomly chosen each time.

You can also use experience sources for your main classes.

## Examples

Let's have a look at an example. These are the default experience sources for the _Woodcutting_ profession. It basically gives the player anywhere from 1 to 3 experience points whenever he cuts a log.

```yml
exp-sources:
- 'mineblock{type=OAK_LOG;amount=1-3}'
- 'mineblock{type=SPRUCE_LOG;amount=1-3}'
- 'mineblock{type=BIRCH_LOG;amount=1-3}'
- 'mineblock{type=JUNGLE_LOG;amount=1-3}'
- 'mineblock{type=ACACIA_LOG;amount=1-3}'
- 'mineblock{type=BIRCH_LOG;amount=1-3}'
- 'mineblock{type=DARK_OAK_LOG;amount=1-3}' 
```

These are the default experience sources for the farming profession, which grants some experience points whenever the player harvest any type of crops.

```yml
exp-sources:
- 'mineblock{type=CARROTS;amount=1-3;crop=true;player-placed=true}'
- 'mineblock{type=POTATOES;amount=1-3;crop=true;player-placed=true}'
- 'mineblock{type=WHEAT;amount=1-3;crop=true;player-placed=true}' 
```

`crop=true` means that it'll only grant EXP once it's at it's full growth stage. `player-placed=true` means that it'll grant EXP even if the player placed the block

### Experience Sources Tables (Since 1.9.5)

You can create experiences-sources tables in `exp-sources.yml`. It links an id to a list of experiences sources that you will all be to reference at once.

```yml
#Example
test-exp-source: 
  - 'damagedealt{type=physical;amount=250}'
  - 'move{type=WALK;amount=300}'
  - 'from{source=test2}'

test2:
  - 'eat{type=CARROT;amount="50"}'
```

## Every experience source

| Source | Usage | Description |
|--------|-------|-------------|
| From | `from{source=exp-source-id}` | Loads all the experience source in `exp-sources.yml` matching  to `exp-source-id`. |
| Mine Block | `mineblock{type=BLOCK_MATERIAL}` | More info on [Mining](../features/mining.md). |
| Kill Mob | `killmob{type=MOB_ENTITY_TYPE;amount=1-3}` | Killing a mob grants exp |
| Kill Mythic Mob | `killmythicmob{type=MobInternalName;amount=1-3}` | Killing a MythicMob grants exp |
| Fish Item | `fishitem{type=ITEM_MATERIAL}` | Fishing an item of the specified type grants exp. |
| Smelt Item | `smeltitem{type=ITEM_MATERIAL}` | When an item is smelted (furnaces) |
| Craft Item | `craftitem{type=ITEM_MATERIAL}` | When an item is crafted |
| Brew potion | `brewpotion{effect=SPEED,REGEN,...}` | [More info on Alchemy](../profession/alchemy.md) |
| Place Block | `placeblock{type=BLOCK_MATERIAL}` | Placing a block of the specified type grants xp. |
| Repair Item | `repairitem{type=ITEM_MATERIAL}` | You can define on sithing.yml the amount of xp for each material. Check [here](../profession/smithing.md) the info about smithing.. |
| Enchant Item | `enchantitem{type=...}` | [More info on Enchanting](../profession/enchanting.md) |
| Climb | `climb{type=CLIMB_TYPE}` | When you climb one block. The type can be ladder, vines, weeping-vines, twisting-vines. If you don't specify any type it will trigger for all types. |
| Eat | `eat{type=ITEM_MATERIAL}` | Give experience when some specific food is eaten. If you don't specify a material for the type it will give exp disregarding what you eat. |
| Move | `move{type=MOVING_TYPE}` | Give experience for each block travelled the type can be sneak, fly, swim, sprint or walk.If it is not specified will trigger all the time. |
| Resource | `resource{type=RESOURCE_TYPE}` | Gives exp for each resource of type "RESOURCE_TYPE" consumed. Resource type can be mana, stamina or stellium. |
| Ride | `ride{type=ENTITY_TYPE}` | When you move riding a certain entity. Check the [EntityType](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html) enum to specify the type. |
| Tame | `tame{}` | Exp given for each damage your wolves make. |
| Damage Taken | `damagetaken{type=DAMAGE_CAUSE}` or all damage cause `damagetaken{amount=1}` | Exp given for each damage a player takes damage from a certain cause. You can do for instance DROWNING, FALL, FIRE or BLOCK_EXPLOSION, Check [here ](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)the documentation of DamageCause. |
| Damage Dealt | `damagedealt{type=DAMAGE_TYPE}` or all damage types `damagedealt{amount=1}` | Exp given per damage dealt of a certain mmo damage type.The damage type can be magic, physical, weapon, skill, projectile,unarmed, on-hit, minion or dot. |

