---
order: 3
---

# Using CoreTools

[CoreTools](https://www.spigotmc.org/resources/coretools.125126/) can be used to create skills that you can run in all MMO plugins.

## Custom Skill Registration

First, code your skill in CoreTools. For this tutorial, we will be using a very simple script; it is the built-in script which ID `script3`.
```yml
script3:
  Conditions: []
  Mechanics:
    - command{c="say Hello I'm Script 3"} @Self
```

Then, open up any YML config file inside the `MythicLib/skill` folder and paste the following:
```yml
MY_SKILL_3:
  coretools-skill-id: script3
```

After reloading both plugins, you can now use the skill `MY_SKILL_3` in MMOItems and MMOCore. You can try to cast it using `/ml debug cast MY_SKILL_3`, and you should see the message appear in the player chat.

## Skill Modifiers

There is currently no way to retrieve skill modifiers when using CoreTools skills, unlike when using MythicMobs.

## Specifications

### Support for conditions

Just like MythicMobs, skills registered in MythicLib using CoreTools can have conditions. If any of the CoreTools conditions is not met, the skill will not be cast, no mana will be consumed, no cooldown will be applied, etc.