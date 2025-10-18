---
order: 3
---

# 🗃️ Skill Configs

The `/skills` folder houses all of the skills that come with the plugin. Most skills are hardcoded into the plugin jar. If you do not want to use a skill, simply do not assign it to a class. Each skill has its **own YAML configuration file**, where you can edit its lore, , how it looks in the /skills menu, and the default parameter values for that skill.

MMOCore comes with 90+ default skills which it shares with MythicLib and MMOItems. MMOCore also enables you to create your own skills, either using the MythicMobs, MythicLib/MMOLib or even SkillAPI scripting language. More information below.

## Example Skill

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

This is an example skill showing the name option, lore, and several attribute modifiers.

For each skill you can edit the display name, how it looks in the /skills, and then all of its modifiers. The base option is how much damage/value it will have by default, and then per-level is what it will change by each time you level up the skill using skill points. There is a max and minimum for these values as well, that way you can't have a -2sec cooldown. You can also set a specific \`decimal-format \` for each parameter that will be used when parsing the corresponding placeholder, if it is not specified the default mythiclib decimal format will be used.

The `material` option determines what icon will display in the player's skill list. Using `<MATERIAL_NAME>:<integer>` will apply a custom model data to your skill icon, where the integer input is the custom model data being used.

Finally the `unlocked-by-default` option enables to say if a skill is unlocked or not by default. If this option is not filled the skill will be considered as unlocked-by-default.

![PhIpbOr](uploads/c663353b0893fc7e635bac6007069f77/PhIpbOr.png)

## Binding MythicMobs skills to MMOCore skills

Since MMOCore 1.9 custom skills are handled within MythicLib, please refer to [this wiki page](https://gitlab.com/phoenix-dvpmt/mythiclib/-/wikis/Skills).

### Making a passive skill

If you want to make a passive skill (using MythicMobs or SkillAPI) all you have to do is add `passive-type: TYPE` to your skill YML file in the '/skills' folder. Adding a passive type to your skill will prevent it from being bound and will automatically cast during specific events, depending on the passive type specified. You can see all Trigger Types on [this](https://gitlab.com/phoenix-dvpmt/mythiclib/-/wikis/Trigger%20Types) page.