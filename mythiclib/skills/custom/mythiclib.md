---
order: 2
---

# Using MythicLib

MythicLib [scripts](../../scripts/intro.md) can be exported into custom skills that can be used in MMOItems or  MMOCore. There are to methods of exporting a MythicLib script into a custom skill.

## First Method

Let's assume you already have an existing MythicLib script somewhere inside the `MythicLib/scripts` folder. You only need to toggle on the `public` flag to indicate you want MythicLib to export this script into a skill.

```yml
my_mythiclib_script:
    
    # This will register a skill with ID 'MY_MYTHICLIB_SCRIPT'
    public: true
    
    # Modifiers of your new skill
    modifiers:
    - damage
    - slow_duration

    conditions:
        # skills conditions....
    mechanics:
        # skills mechanics...
```

## Second Method

Navigate to the `MythicLib/skill` folder and create a new/open an existing YML config. Copy the following code into the file:

```yml

# This will register a skill with ID 'MY_NEW_SKILL'
MY_NEW_SKILL:

    # This points to the MythicLib script you want to use
    # located in the MythicLib/scripts folder
    mythiclib-skill-id: my_mythiclib_script

    # This is optional. These are the skill parameters/modifiers
    # that will be passed to MMOItems/MMOCore when the skill is executed.
    # You can add as many as you need.
    modifiers:
    - damage
    - slow_duration
```
