---
order: 1
---

# Using MythicMobs

This page will help you register custom skills in MythicLib/MMOItems/MMOCore using the Mythic/MythicMobs scripting language. Here are the main steps:

1. Code a Mythic script
2. Register that script as a custom MythicLib skill,
3. Configure that same skill (in MMOItems/MMOCore).

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

Go to the `MythicLib/skill` folder and create a YAML configuration file, which name can be whatever your want. Let's say it's `tutorial.yml`. Just like in Mythic, you can:

- have multiple skills within the same config file
- organize your files into folders
- the file and folder names do not matter

```yaml
FIRE_BOLT:
  # Internal name of the MythicMobs script
  mythicmobs-skill-id: FireBolt

  # Choose the ability modifiers
  modifiers:
  - damage
  - duration
  
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

# You can have multiple skills in one config.
ANOTHER_SKILL:
  #...
```

As you can see, you can put Mythic scripts inside of the MythicLib config file. That is what the `extra-skills` config section is all about - any Mythic script that you place inside this configuration section will be passed to Mythic. In order to register MythicLib custom skills, you can either put your Mythic scripts inside of the ML config file, or simply pass a reference (the script name i.e `FireBolt`) to an existing Mythic script. Either way, the Mythic script names must match:
```yaml
FIRE_BOLT:
  mythicmobs-skill-id: FireBolt # These two must match
  #...
  extra-skills:
    FireBolt: # These two must match
      #...
```

Let's go through the `FIRE_BOLT` configuration section. First, nicely format the config section name so that it matches that `UPPERCASE_ID_FORMAT` because it's the one used for skills in MMOItems/MMOCore. Then, input the internal name of your MM skill using the `mythicmobs-skill-id` config option: in our case, it is `FireBolt`.

The second option you need to input is the list of your **skill modifiers**. We will go over this feature later on, just keep in mind that this is the list of all the possible **numeric parameters** of your skill (how much damage it deals, how long slowness lasts...)

At this point, you can use `/ml reload` and test your new skill using the following command:
```sh
/ml debug cast FIRE_BOLT
```

## 3/ Configuring your skill in MMOItems/MMOCore

Your skill is now registered in MythicLib. Since both MMOItems and MMOCore use the MythicLib skill registry, it is now also registered in MMOItems and MMOCore, but it is not fully configured, which is what we're going to do now.

**MMOCORE:** Use `/mmocore reload`. A configuration file named `fire-bolt.yml` should appear inside the `MMOCore/skills` folder. Open and edit it to your liking before using `/mmocore reload` again which will load the edited config file into the MMOCore registry. You now have a fully working skill which you can bind to your player class. Since this part is specific to MMOCore, check the [MMOCore wiki](../../../mmocore/skills/config.md) to learn how to edit a MMOCore skill config file.

**MMOITEMS:** Use `/mi reload skills`. A config file named `fire-bolt.yml` should appear inside the `MMOItems/skills` folder. Open and edit it to your liking before using `/mi reload skills` again which will load the edited config file into the MMOCore registry. You now have a fully working skill which you can add to your MI items. This part is specific to MMOItems, so check the [MI wiki](../../../mmoitems/features/skills.md#editing-an-ability) to learn how to edit a MI skill config file.

---

## Skill Conditions

Custom MM skills also support skill conditions. If any of the skill conditions is not met, the skill won't cast and no mana will be consumed.

## Retrieving MythicLib skill modifiers inside MM custom skills

::: warning
Some of the features described below are not available in the free version of MythicMobs.
:::

Let's consider the `Fire-Bolt` skill again.

As explained before, the skill currently deals 10 damage whatever modifier you might have setup. However, we want that skill to deal the amount of damage dictated by MMOItems or MMOCore.

- In MMOItems, this allows you to have skills with different parameters on your MI items
- In MMOCore, skills can scale up with the player class level.

The following skill deal a static amount of 10 damage.

```yaml
SomeSkill:
  Mechanics:
  - damage{a=10}
```

The following skill deals damage equivalent to the `damage` skill modifier, forwarded from MythicLib to MythicMobs.

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