---
order: 5
---

# 🗃️ Configuration

## Class Config

Skills are class-specific, which means you need to choose what skills to give to each [class](../features/classes.md).

In order to choose what skills each class can use, open up the class config file and look for/create the `skills` config section. Each entry of this config section corresponding to a single class skill.

```yaml
skills:

  # First skill
  FIRE_STORM:
    level: 1
    max-level: 30
    unlocked-by-default: true

    # Skill modifeirs
    damage:
      base: 5.0
      per-level: 3.0
    cooldown:
      base: 5.0
      per-level: -0.1
      max: 5.0
      min: 1.0
    #....
  
  # Second skill
  POWER_MARK:
    level: 3
    max-level: 30
    unlocked-by-default: true
    needs-bound: true
    #.....
  
  #..........
```

### Skill Level

`level` indicates the level at which the class naturally unlocks this skill. `max-level` is the maximum level for that class skill. Once reached, the player can no longer [upgrade](intro.md#upgrading-a-skill) this skill.

`unlocked-by-default` indicates if this skill should be unlocked by default. It is set to `true` by default. When toggled off, this skill has to be [unlocked](unlocking.md) through the use of a command, quest trigger, skill book, exp table...

### Needs Binding

Another option is `needs-bound`. This option is only relevant for passive skills, as active skills must all be bound. When set to `false`, the passive skill takes effect even if not bound (and therefore can no longer be bound to any skill slot).

### Skill Parameters

You might also want to change the skill numerical parameters, so that a fireball cast by the _Mage_ class deals more damage than a fireball cast by the _Paladin_ class. Each parameter of each skill can be edited by adding the corresponding entry to the class skill config. For instance (see above), the `damage` parameter for the _Fire Storm_ skill is set to equal 5 Dmg, plus 3 Dmg per skill level. These skill parameters do not scale with the player's level but rather with the skill level. The skill level increases when a skill is [upgraded](intro.md#upgrading-a-skill).

## Skill Folder

The `/skills` folder houses all of the skills that come with the plugin. Most skills are hardcoded into the plugin jar. If you do not want to use a skill, simply do not assign it to any class. Each skill has its **own YAML configuration file**, where you can edit its lore, name, looks... and the default parameter values for that skill.

```yml
name: Fire Storm
material: 'BLAZE_POWDER:1'
lore:
- Casts a flurry of 6 fire projectiles onto
- nearby enemies, proritizing the initial
- target. Each projectile deals &c{damage} &7damage
- and ignite the target for &c{ignite} &7seconds.
- ''
- '&e{cooldown}s Cooldown'
- '&9Costs {mana} Mana'
damage:
  base: 5.0
  per-level: 3.0
  #Optional: The decimal format used for this skill parameter.
  decimal-format: '0.#'
ignite:
  base: 2.0
  per-level: 0.1
mana:
  base: 15.0
  per-level: 2.0
cooldown:
  base: 5.0
  per-level: -0.1
  max: 5.0
  min: 1.0
```

This is an example skill showing the name option, lore, and several skill parameters.

For each skill you can edit the display name, how it looks in the skill GUI, and all of its modifiers. The `base` option is how much damage/value it will have by default, and then per-level is what it will change by each time you level up the skill using skill points. There is a max and minimum for these values as well, that way you can't have a -2sec cooldown. You can also set a specific \`decimal-format \` for each parameter that will be used when parsing the corresponding placeholder, if it is not specified the default mythiclib decimal format will be used.

The `material` option determines what icon will display in the player's skill list. Using `<MATERIAL_NAME>:<integer>` will apply a custom model data to your skill icon, where the integer input is the custom model data being used.

Finally the `unlocked-by-default` option enables to say if a skill is unlocked or not by default. If this option is not filled the skill will be considered as unlocked-by-default.

![PhIpbOr](uploads/c663353b0893fc7e635bac6007069f77/PhIpbOr.png)

## Skill Categories

Each skill can be assigned to a list of categories through the field `categories`. By default, each skill is associated to two categories: its skill ID (`FIREBALL` for instance, not to be mistaken with the skill name), and either `ACTIVE` or `PASSIVE` depending on if it is an active or passive skill. These categories can be used inside [skill slot formulas](binding.md#skill-slots).

For instance, this code snippet can be placed in the `skills/firebolt.yml` config file to provide a few categories to the _Firebolt_ skill:
```yml
categories:
- fire
- projectile
```

## Making a passive skill

If you want to make a passive skill (using MythicMobs or SkillAPI) all you have to do is add `passive-type: TYPE` to your skill YML file in the '/skills' folder. Adding a passive type to your skill will prevent it from being bound and will automatically cast during specific events, depending on the passive type specified. You can see all Trigger Types on [this](../../mythiclib/skills/triggers.md) page.