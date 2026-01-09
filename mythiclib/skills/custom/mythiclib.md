---
order: 2
---

# Using MythicLib

MythicLib [scripts](../../scripts/intro.md) can easily be turned into custom skills that can be used in MMOItems or MMOCore. We first need to write a MythicLib script, then declare it as a skill. A script basically says "what happens", while a skill provides more metadata including its mana cost, cooldown, damage, GUI lore, icon....

::: info
This page will be subject to changes in the near future
:::

## 1/ Code a MythicLib script

First, navigate to the `MythicLib/script` folder and open an existing/create a new YML config file to start writing your MythicLib script.

For this tutorial, we will use the builtin `staff_attack` script that comes with MythicLib. You can find it inside the `MythicLib/script/example_skills.yml` file. This script shoots a magic projectile dealing 10 damage to the first entity it hits.

```yml
# The script that you cast to peform the staff attack
staff_attack:
  mechanics:
    - 'raytrace{hit_entity=staff_attack_hit_entity;tick=staff_attack_tick;size=1}'
    - 'sound{sound=ENTITY_BLAZE_SHOOT;pitch=1;volume=1}'

# The effect when the attack hits an entity
staff_attack_hit_entity:
  conditions:
    - 'can_target'
  mechanics:
    - 'damage{amount=10;ignore_immunity=true}'
    - 'particle{particle=LAVA;amount=32}'

# The tick effect while the raytrace is ongoing
staff_attack_tick:
  mechanics:
    - 'particle{particle=REDSTONE;amount=4;x=.5;y=.5;z=.5}'
```

## 2/ Declare the script as a skill

Now that we have our MythicLib script called `staff_attack`, we need to declare it as a skill and provide additional metadata. Now, navigate to the `MythicLib/skill` folder and create a new/open an existing YML config. Copy the following code into the file:
```yml

# This will register a skill with ID 'MY_NEW_SKILL'
STAFF_ATTACK:

  # This points to the MythicLib script you want to use
  # located in the MythicLib/scripts folder
  mythiclib-skill-id: staff_attack

  # This is optional. These are the skill parameters/modifiers
  # that will be passed to MMOItems/MMOCore when the skill is executed.
  # You can add as many as you need.
  modifiers:
  - damage
  - slow_duration
```

You can test this skill in-game by using the following command:
```sh
/ml debug cast staff_attack
```