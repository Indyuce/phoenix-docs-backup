---
order: 2
---

# 💥 Triggers

When using MMOItems or MMOCore, you will need to specify when a specific skill should be executed: when damaging an entity, when being damaged, when crouching etc. This is done using triggers. MMOItems used to call them _casting modes_.

## Available Triggers

These are the trigger types that you can use in MMO plugins to define when some skill is supposed to run.

### Combat & Damage

| Skill Trigger | Description | Target Entity | Target Block |
|---------------|-------------|----------------|----------------------|
| KILL_ENTITY | Activates the skill when a player kills an entity | The killed entity | - |
| KILL_PLAYER | Activates the skill when a player kills an player | The killed player | - |
| ATTACK | Activates the skill when the player attacks something | The entity the player attacked | - |
| DAMAGED | Activates the skill when the player takes damage | - | - |
| DAMAGED_BY_ENTITY | Activates the skill when the player takes damage from an entity | The entity that damaged the player | - |
| DEATH | Activates the skill when the player dies | - | - |

### Projectiles

| Skill Trigger | Description | Target Entity | Target Block |
|---------------|-------------|----------------|----------------------|
| SHOOT_TRIDENT | When the player shoots a trident | The projectile | - |
| TRIDENT_TICK | Activates every tick when a trident is still midair | The projectile | - |
| TRIDENT_LAND | When a trident lands on the ground | The projectile | - |
| TRIDENT_HIT | When a thrown trident hits an entity | The hit entity | - |
| SHOOT_BOW | When the player fires an arrow | The projectile | - |
| ARROW_TICK | Activates every tick when an arrow is still midair | The projectile | - |
| ARROW_LAND | When an arrow lands on the ground | The projectile | - |
| ARROW_HIT | When a fired arrow hits an entity | The hit entity | - |

### Player Clicks

| Skill Trigger | Description | Target Entity | Target Block |
|---------------|-------------|----------------|----------------------|
| RIGHT_CLICK | On player right click | - | - |
| LEFT_CLICK | On player left click | - | - |
| SHIFT_RIGHT_CLICK | On player right click while sneaking | - | - |
| SHIFT_LEFT_CLICK | On player left click while sneaking | - | - |

### Blocks

| Skill Trigger | Description | Target Entity | Target Block |
|---------------|-------------|----------------|----------------------|
| BREAK_BLOCK | When a player breaks a block | - | Location of mined block |
| PLACE_BLOCK | When a player places a block | - | Located of placed block |

### MMOCore Triggers

These triggers are only available when MMOCore is installed. If you try to use them without MMOCore installed, you will run into errors.

| Skill Trigger | Description | Target Entity | Target Block |
|---------------|-------------|-|-|
| ENTER_COMBAT | Activates skills when a player enters [combat](../../mmocore/features/combat.md). | - | - |
| QUIT_COMBAT | Activates skills when a player quits [combat](../../mmocore/features/combat.md). |  - | - |

### Items

| Skill Trigger | Description | Target Entity | Target Block |
|---------------|-------------|----------------|----------------------|
| DROP_ITEM | Activates the skill when a player press Q | The dropped item | - |
| SHIFT_DROP_ITEM | Activates the skill when a player press Shift + Q | The dropped item | - |
| SWAP_ITEMS | Activates the skill when a player press F | - | - |
| SHIFT_SWAP_ITEMS | Activates the skill when a player press Shift + F | - | - |
| ~~EQUIP_ARMOR~~ | Activates the skill when a player enquip armor | The player | - |
| ~~UNEQUIP_ARMOR~~ | Activates the skill when a player unenquip armor | The player | - |

### Miscellaneous

| Skill Trigger | Description | Target Entity | Target Block |
|---------------|-------------|----------------|----------------------|
| LOGIN | Activates the skill when a player logins | - | - |
| SNEAK | Activates the skill when a player sneaks | - | - |
| TELEPORT | Activates the skill when a player teleport | - | The target teleport location |
| TIMER | Casts the skill every X ticks | - | - |


## When a skill/script is triggered

Some trigger types pass on special properties to the script/skill they trigger. For instance; when using the `ATTACK` trigger type:
- The `<target>` internal variable can be used to access the entity being damaged,
- The `<attack>` internal variable returns metadata about the current attack,
- `<attack.damage>` returns the attack damage.

Trigger types featuring entities/projectiles like `ATTACK`, `DAMAGED`, `DAMAGED_BY_ENTITY`, `KILL_ENTITY`, `SHOOT_TRIDENT`, `ARROW_TICK` etc. allow the user to use the `<target>` internal variable to access the shot projectile. These triggers also unlock the use of [entity and location targeters](../scripts/targeters/intro.md) such as `target` and `target_location`.

Trigger types featuring world locations like `TRIDENT_LAND` or `ARROW_HIT` unlock the `target_location` location targeter as well as the `<target_location>` internal variable.

Some triggers like `TIMER` or `RIGHT_CLICK` do not unlock any additional internal variable.

`ATTACK` is the only trigger type which unlocks the `<attack>` internal variable as well as special mechanics (`multiply_damage`) or conditions (`has_damage_type`).

## Custom Triggers

MythicLib allows users to define their own triggers and manually call them. This is a complex - yet super powerful - functionality that adds another layer of configurability on top of existing skills.

### Defining custom triggers

You can define custom triggers inside the `MythicLib/triggers.yml` configuration file. Note that this file only contains user-defined triggers, as the triggers presented above are hard-coded and cannot be edited.

```yml
# Triggered on weapon crits
# Corresponding on-hit effect: on_hit_effects/weapon_crits
# Call in script:              script/on_hit_effects.yml>weapon_crit_script
CRIT:

  # When set to false, send messages to the player
  # when skills cannot cast due to them being on cooldown,
  # missing mana/stamina....
  silent: true

# Triggered on special mage abilities
MAGE_BURN:
  silent: true


```

### Calling custom triggers

You can call custom triggers from inside a MMOLib script using the `call_trigger` mechanic. "Calling a trigger" refers to casting all the skills of a given player with matching trigger. For instance, on all player/mob attacks, MMOLib calls the `ATTACK` trigger under the hood.

Let's take the built-in weapon crits as an example. We would like to create a skill trigger, that gets called whenever a player performs a weapon critical strike while attacking.

The following code snippet is taken from the default `MythicLib/script/on_hit_effects.yml` file, which defines the behavior of weapon crits.

```yml
# Called to check if weapon crits may apply
weapon_crit_script_check:
  conditions:
    - 'has_damage_type{types="weapon,unarmed"}'

# Called when a weapon crit occurs
weapon_crit_script:
  mechanics:
    - 'set_double{var=crit_coef;val="<stat.critical_strike_power> / 100"}'
    - 'multiply_damage{scalar="<crit_coef>";dtype=WEAPON}'
    - 'multiply_damage{scalar="<crit_coef>";dtype=UNARMED}'
    - 'mark_crit{dtype="WEAPON,UNARMED"}'
    - 'call_trigger{trigger=crit}'
    # [...]
```

As you can see, when the `weapon_crit_script` script is called (i.e when a weapon crit occurs), the script eventually uses the `call_trigger` mechanic to call the `CRIT` user-defined skill trigger, that we defined earlier. This has the effect of casting all the caster's skills with trigger set to `CRIT`.

::: warning
You can use the `call_trigger` mechanic to call ANY trigger, not only user-defined triggers. This can be used to create more complex behaviors like on-hit skill triggers, though it is the user's responsibility to make sure the proper skill metadata arguments are provided when calling built-in skill triggers.
:::

### Disabling user-defined triggers

This feature is quite hard to comprehend - if you wish to disable this feature altogether, simply comment out/delete the content of the `triggers.yml` file. Do not delete the config file itself, otherwise it will regenerate with its default content.