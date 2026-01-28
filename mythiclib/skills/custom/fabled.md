---
order: 3
---

# Using Fabled

Fabled, formerly known as ProSkillAPI, or SkillAPI, is a powerful skill creation and management plugin. You can create custom skills inside Fabled and use them inside MythicLib.

::: info
As of MythicLib 1.6.2 snapshots, SkillAPI and ProSkillAPI are no longer supported, as both plugins are no longer being actively maintained. We ask users to move to Fabled instead.
:::

## Custom Skill Registration

Similarly to MythicMobs, you can register custom skills into MythicLib using the Fabled skill editor. The process is the exact same as in [this tutorial](mythic.md#custom-skill-registration) apart from the format of the MythicLib skill configuration file.

First, code your skill using the Fabled skill editor. Let's assume the skill you coded has ID `Firebolt`. Open up a YML config file within the `MythicLib/skill` folder and paste the following:
```yml
FIREBOLT:
  source: 'fabled:<Fabled_skill_identifier>'
  name: 'Firebolt'

  # Parameters/modifiers are not supported.
  #parameters: {}
```

## Skill Modifiers

There is currently no way to retrieve skill modifiers when using Fabled skills, unlike when using MythicMobs. The `parameters` section in the config sample above can therefore be omitted.

## Skill Level

That being said, all skills registered using Fabled have a `level` skill modifier which hooks directly into Fabled skill level system. You can setup skill mechanic numerical parameters to linearly scale on the skill level. Using MythicMobs you'd have been able to setup any type of scaling you want (not limited to linear scaling).

Just like `cooldown` `mana` and `stamina`, the `level` modifier is automatically registered.

::: tip
While Fabled remains an option for custom skill creation, we still recommend using MythicMobs instead
:::
