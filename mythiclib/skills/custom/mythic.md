---
order: 1
---

# Using MythicMobs

This page will help you register custom skills in MythicLib/MMOItems/MMOCore using the Mythic/MythicMobs scripting language. Here are the main steps:

1. Code a Mythic script
2. Register that script as a custom MythicLib skill,
3. Reload the plugins.

## 1/ Code a MythicMobs skill

The first step is to code what your skill does using the MythicMobs scripting language. In this tutorial, we'll consider a skill example that we found in the MythicMobs manual. It is a simple fire projectile that deals 10 damage and slows the first enemy it hits for 2 sec.

```yaml
FireBolt: # The main skill
  Skills:
  - 'projectile{onTick=FireBolt-Tick;onHit=FireBolt-Hit;v=8;i=1;hR=1;vR=1;hnp=true} @targetLocation'
FireBolt-Tick:
  Skills:
  - 'effect:particles{p=flame;amount=20;speed=0;hS=0.2;vS=0.2} @origin'
FireBolt-Hit:
  Skills:
  - 'damage{a=10}'
  - 'potion{type=SLOW;duration=40;lvl=2}'
```

## 2/ Declare it as a MythicLib skill

Go to the `MythicLib/skill` folder and create a YAML configuration file, which name can be whatever you want - let's say you name it `tutorial.yml`. Just like in MythicMobs, you can:

- have multiple skills within the same config file
- organize your files into subfolders
- file and folder names can be whatever you want

```yaml
FIRE_BOLT:
  source: mythicmobs:FireBolt
  # trigger: RIGHT_CLICK # Not needed here as we are making an active skill

  name: Firebolt
  lore:
    - 'You conjure a flaming ball and'
    - 'ball and hurl it at your target.'
    - ''
    - '&e{cooldown}s Cooldown'
    - '&9Costs {mana} {mana_name}'
  icon: BLAZE_POWDER

  # Edit default values of the ability parameters
  parameters:
    damage:
      name: Damage
      player:
        base: 2
        per-level: 1
      item: 5.0
    duration:
      name: Duration
      player: '2 + {level} * 1'
      item: 5.0
  
  extra-skills:
    FireBolt: # The main skill
      Skills:
      - 'projectile{onTick=FireBolt-Tick;onHit=FireBolt-Hit;v=8;i=1;hR=1;vR=1;hnp=true} @targetLocation'
    FireBolt-Tick:
      Skills:
      - 'effect:particles{p=flame;amount=20;speed=0;hS=0.2;vS=0.2} @origin'
    FireBolt-Hit:
      Skills:
      - 'damage{a=10}'
      - 'potion{type=SLOW;duration=40;lvl=2}'

# You can have multiple skills in one config file
#ANOTHER_SKILL:
  #source: ...
  #....
```

### Config Options

#### Skill Identifier

Let's go through the `FIRE_BOLT` configuration section. First, nicely format the config section name so that it matches that `UPPERCASE_ID_FORMAT` because it's the one used for skills in MMOItems/MMOCore.

#### Skill Source

Then, provide the "source" of your skill. Since we are implementing a MythicLib skill using MythicMobs, the source must be `mythicmobs:FireBolt`, where `FireBolt` is the name of the MythicMobs skill that we defined earlier. The table below indicates all skill sources that you can actually use with MythicLib:

| Source | Format |
|--------|--------|
| [MythicMobs](https://www.spigotmc.org/resources/5702/) | `mythicmobs:<MythicMobsSkillname>` |
| [MythicLib](https://www.spigotmc.org/resources/90306/) | `mythiclib:<mythiclib_script_name>` |
| [Fabled](https://www.spigotmc.org/resources/91913/) | `fabled:<FabledAbilityName>` |
| [CoreTools](https://www.spigotmc.org/resources/125126/) | `coretools:<CoreToolsScriptName>` |

#### Skill Icon, Name and Lore

The `icon` options lets you modify the item that MMOCore will use inside the skill UI to display that skill. You can use any valid Minecraft material name.

In order to add custom model data, item model... use the following syntax. Note that all of these parameters are optional.
```yml
FIRE_BOLT:
  #...
  icon:
    item: DIAMOND_SWORD
    custom_model_data: 1234
    item_model: 'minecraft:dirt'
    item_flags: [HIDE_ATTRIBUTES, HIDE_ENCHANTS]
  #...
```

The `lore` option lets you customize the skill description that players will see in the MMOCore skill UI. Note the use of placeholders such as `{cooldown}`, `{mana}`, `{mana_name}` that will be dynamically replaced when the skill is displayed.

The `name` option lets you customize the skill name. Note that this is the only field used by MMOItems, as the icon and lore are only being used by MMOCore.

#### Trigger

The `trigger` option defines the default trigger type/casting method for that skill. Unless specified again in a MMOCore skill config, that skill will inherit this trigger. The list of available trigger types is available on [this wiki page](../triggers.md).

::: tip
Recall that skills that have a trigger are considered "passive skills" as they trigger automatically. Skills with no triggers are considered "active skills" as they need to be manually [cast by players](../../../mmocore/skills/casting.md).
:::

#### Skill Categories

Each skill can be assigned to a list of categories through the field `categories`. By default, each skill is associated to two categories: its skill ID (`FIREBALL` for instance, not to be mistaken with the skill name), and either `ACTIVE` or `PASSIVE` depending on if it is an active or passive skill. These categories can be used inside [skill slot formulas](binding.md#skill-slots).

The following code snippet sets the categories of the _Firebolt_ skill:
```yml
FIREBOLT:
  # ...
  categories: [ fire, projectile ]
```

#### Skill Parameters

The `parameters` section lets you define the skill modifiers that your skill will use. In our example, we defined two skill modifiers: `damage` and `duration`. Each modifier has a `name` (displayed in the skill UI), a `player` section (which defines how the modifier scales with player level) and an `item` section (which defines how the modifier scales with item level).

The `player` section dictates the scaling of the skill modifier when the skill is cast through MMOCore classes. The `item` section dictates the default skill parameter value when the skill is placed onto an MMOItems item. The `name` field is used by both MMOCore UIs and MMOItems for the item lore.

Note that you have two possibilities to provide the `player` section. You can either provide a `base` and `per-level` value, which will result in a linear scaling:
```yml
FIRE_BOLT:
  #...
  parameters:
  #...
    damage:
      name: Damage
      player:
        base: 2
        per-level: 1
      item: 5.0
```

You can also provide a fully custom formula using the `{level}` placeholder, which represents the player skill level:
```yml
FIRE_BOLT:
  #...
  parameters:
  #...
    duration:
      name: Duration
      player: '2 + {level} * 1'
      item: 5.0
```

The `item` field, however, is always a flat decimal number.

### `extra-skills`

As you can see, you can put Mythic scripts inside of the MythicLib config file. That is what the `extra-skills` config section is all about - any Mythic script that you place inside this configuration section will be passed to Mythic. In order to register MythicLib custom skills, you can either put your Mythic scripts inside of the ML config file, or simply pass a reference (the script name i.e `FireBolt`) to an existing Mythic script. Either way, the Mythic script names must match:
```yaml
FIRE_BOLT:
  #...

  extra-skills:
    FireBolt: # These two must match
      #...
```

## 3/ Reload the plugins

1) Reload MythicMobs using `/mm reload`. By now, you should be able to use `/mm debug cast FireBolt` to test your MythicMobs skill.
2) Reload MythicLib using `/ml reload`. By now, your skill should be registered in MythicLib, and you should be able to use `/ml debug cast FIRE_BOLT` to test your MMO skill.

That's it! You do not need additional config files for MMOItems or MMOCore, as both of these plugins directly use the MythicLib skill registry.


## Skill Conditions

Custom MM skills also support skill conditions. If any of the skill conditions is not met, the skill won't cast and no mana will be consumed.

## Retrieving MMO skill modifiers inside MythicMobs skills

::: warning
Some of the features described below are not available in the free version of MythicMobs.
:::

Let's consider the `Fire-Bolt` skill again.

As seen before, the following skill currently deals a flat 10 damage. We would like this value to scale with the MMOCore skill level or MMOItems item power.

```yaml
SomeSkill:
  Mechanics:
  - damage{a=10}
```

The following skill deals damage equivalent to the `damage` MythicLib skill modifier. The `<modifier.xxx>` allows to forward MythicLib skill parameter values to MythicMobs math formulas used inside mechanics, conditions...

```yaml
SomeSkill:
  Mechanics:
  - damage{a="<modifier.damage>"}
```

These placeholders can be combined with math formulas. In the following example, the `duration` modifier is multiplied by 20 to convert seconds into ticks.

```yaml
SomeSkill:
  Mechanics:
  - potion{type=SLOW;duration="<modifier.duration> * 20";lvl=2}
```

Here is the full list of placeholders implemented by MythicLib, available inside MythicMobs skills.

| Placeholder                 | Description                                                         |
| --------------------------- | ------------------------------------------------------------------- |
| `<modifier.(mod_name)>`     | Skill modifier, as decimal number                                   |
| `<modifier.int.(mod_name)>` | Skill modifier, as integer                                          |
| `<cooldown.skill_(name)>`   | Remaining cooldown for a skill                                      |
| `<mmostat.(stat_name)>`     | Player stat value, as decimal number. Ex: `<mmostat.attack_damage>` |
| `<mana>`                    | The player's current mana (MMOCore)                                 |
| `<stamina>`                 | The player's current stamina (MMOCore)                              |
| `<stellium>`                | The player's current stellium (MMOCore)                             |

## Dealing Damage

::: info
This is subject to change for better support of the MythicLib damage system in the future.
:::

Use the `mmodamage` mechanic instead of the native `damage` mechanic to deal damage with MMO damage types.

```yaml
SomeSkill:
  Mechanics:
  - mmodamage{amount="<modifier.damage> + 10";types=SKILL,MAGIC,PROJECTILE;element=FIRE}
```

You can specify the ability damage using `amount` or `a` as well as the damage types using `types` or `t`. The list of available damage types can be found [here](../../features/damage.md).

It works just like the default `damage` mechanic, except that it completely supports the MythicLib damage system, which means that it will apply damage buff stats (additional skill damage, etc), damage reduction stats, on-hit effects (on-hit abilities from MMOItems when using the WEAPON damage type), skills from MMOCore that trigger when dealing damage to entities....

The following mob deals 10 Physical-Weapon damage every 2 seconds to all nearby entities.
```yml
ZombieWarrior:
  Type: ZOMBIE
  Damage: 10
  Skills:
    - 'mmodamage{amount=10;type=PHYSICAL,WEAPON} @NearbyEntities{r=5} ~onTimer:40' 
```

## Increase/Decrease Damage Dealt

You may also use the following skill mechanic:

```yaml
SomeSkill:
  Mechanics:
  - multiplydamage{type=SKILL;amount="1 + <modifier.extra> / 100"}
```

This has the effect of multiplying _Skill_ damage by a specific factor. Currently this factor is `1 + <modifier.extra> / 100` so if the `extra` skill modifier is set to 50, _Skill_ damage will be increased by 50%. You can use this mechanic to increase incoming damage dealt by entities or players by a certain factor (e.g increase damage when low on health).

If you want to increase damage from any source (with no damage type), use:

```yaml
SomeSkill:
  Mechanics:
  - multiplydamage{amount="1 + <modifier.extra> / 100"}
```

## Checking if the skill caster can target another entity

Using the `mmoCanTarget{..}` MythicMobs condition, you can check if any player can target another entity. Here is the format:

```yaml
SomeSkill:
  Conditions:
  - mmoCanTarget{interaction=OFFENSE_ACTION}
```

There are two different interaction types: `OFFENSE_ACTION`, `SUPPORT_ACTION`. For instance, a player will be able to target another player when using a buffing skill (like a heal or a speed boost) but the same target won't be valid if that skill becomes offensive (deals damage or inflicts debuffs). It is therefore very important to specify what type of interaction you are talking about. The PvP/PvE Interaction Rules user guide is available [here](../../../mmocore/features/combat.md).

Here are some examples:

```yaml
COMBAT_ONE:
  mythicmobs-skill-id: combat_one_run
  modifiers:
  - damage
  - duration
  extra-skills:
    combat_one_run:
      TargetConditions:
      - mmoCanTarget{interaction=SUPPORT_ACTION} true
      Skills:
      - jsonmessage{m="[{'text':'SUPPORT_ACTION','color':'red'}]"} @self

COMBAT_TWO:
  mythicmobs-skill-id: combat_two_run
  modifiers:
  - damage
  - duration
  extra-skills:
    combat_two_run:
      TargetConditions:
      - mmoCanTarget{interaction=OFFENSE_ACTION} true
      Skills:
      - jsonmessage{m="[{'text':'OFFENSE_ACTION','color':'red'}]"} @self

COMBAT_THREE:
  mythicmobs-skill-id: combat_three_run
  modifiers:
  - damage
  - duration
  extra-skills:
    combat_three_run:
      Skills:
      - mmodamage{amount=10;types=SKILL,MAGIC,PROJECTILE} @Target{conditions=[ - mmoCanTarget{interaction=OFFENSE_ACTION} true ]}
```