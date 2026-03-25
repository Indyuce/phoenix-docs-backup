---
order: 1
---

# 🧙‍♂️ Classes

Due to popular demand, one of MMOCores trademark features is its customizable class system! This paragraph goes over the important features of classes as well as how to configure them.

Our class system aims to provide a completely user determined class creation system that looks good and works good. We have picked up where other plugins have been abandoned!

## Choosing a class

In order to bring up the class selection menu, type `/class`.

![Profess Menu](uploads/class_select.gif)

## Class Points

In order to pick a class/change your current class you **will need one class point**. You get these via admin command. With this versatile command, the server administrators can hand out class points however they choose, either when leveling up or using a special item with a command bound onto it..

![Class Points](uploads/class_pts.png)

## Default Class

The **default class for players** is human, and that is what players are initially. They are able to gain experience and level up this class, but it should only be a temporary class as it has no skill and lower stats. As soon as they get their first class point, they should switch to another class! The default classes are Mage, Marksman, Paladin, Rogue and Warrior.

## Class Configuration Overview

Each class is divided into its own class file within the folder for organization and easy modification. You may create as many classes as you want, and you may modify/remove the default classes without worry. Creating new classes is as simple as copying the format from the default folders and giving it your own creative ideas.

**In order to create a new class, copy and paste the mage class config file. This is a simple class template which already has all the features explicitely written in its config file so you know what to start from.**

The following paragraphs will guide through class configuration; pickup a class config file, open it and explore it along with the wiki:

## Display Options

These are the first options you will see when opening class config files. These display options let you determine how your class looks in the class menu.

```yaml
display:
    name: 'Mage'
    lore:
    - 'The Mage has mastered the power of the'
    - 'Arcanes, taking down any enemy on his path'
    - 'using powerful magic & ranged abilities.'
    attribute-lore:
    - '&a+ &7Mana Regeneration'
    - '&a+ &7Health Regeneration'
    - '&a+ &7Max Mana'
    - '&c- &7Max Health'
    - ''
    - '&8&lStrength'
    - '&7  Attack Damage: &c1 &7(+&c0&7)'
    - '&7  Attack Speed: &c4 &7(+&c0&7)'
    - '&7  Max Health: &c18 &7(+&c0&7)'
    - ''
    - '&8&lDexterity'
    - '&7  Knockback Resistance: &a0% &7(+&a0%&7)'
    - '&7  Movement Speed: &a20 &7(+&a0&7)'
    - '&7  Speed Malus Reduction: &a0% &7(+&a0%&7)'
    - ''
    - '&8&lIntellect'
    - '&7  Max Mana: &927 &7(+&91.2&7)'
    - '&7  Health Regen: &90.13 &7(+&90&7)'
    - '&7  Mana Regen: &90.2 &7(+&90.04&7)'
    item: BLAZE_POWDER:10 #10 is the custom model data
```

The `name` option corresponds to the class name, used in placeholders and info GUIs. The `lore` and `attribute-lore` options correspond to the class description displayed when a player selects his class using /class.

**Important note: editing the lore and more specifically things like `Attack Damage` or other attributes does NOT actually edit those attributes, it's purely cosmetic and only affect how they look in the /class menu.**

The `item` option corresponds to the icon displayed in the same GUI. You may use custom model data to change the class icon using the following format:

```yaml
display:
    # Format: <material>:<custom-model-data>
    item: 'BLAZE_POWDER:1'
```

## Experience Curve and Max Level

More information [here](../level/curves.md). This is your main class' experience curve ie it defines how much experience a player with this class needs to reach the next level.

```yaml
# Must match an existing exp curve filename from the 'expcurves' folder
exp-curve: levels
```

You can also setup a maximum level so that players cannot keep scaling and earning stats.

```yaml
# Players cannot go further than Lvl 100
max-level: 100
```

## Experience Tables

Just like professions, player classes have experience tables too. Experience tables are not to be mistaken with experience curves. Experience tables determine what happens when a player levels up his main class.

Learn more about experience tables [here](../level/tables.md).

## Additional Options

These are very diverse yet important class options.

```yaml
options:
    default: false
    display: true
    off-combat-health-regen: false
    off-combat-mana-regen: false
    off-combat-stamina-regen: false
    off-combat-stellium-regen: false
```

| Option | Description | Default |
|--------|-------------|---------|
| default | The class that a new player will spawn in with | false |
| display | Whether or not the class should display in /class | true |
| off-combat--regen | regen only applies when out of combat | false |
| needs-permission | The class needs the permission mmocore.class.\<class_id\> to be unlocked | false |

## Class stats

Class stats are the statistics given to the player when he levels up. It's one of the most essential RPG gameplay feature.

```yaml
stats:
    max-health:
        base: 18
        per-level: 0
    max-mana:
        base: 27
        per-level: 1.2
    mana-regeneration:
        base: .2
        per-level: .04
    health-regeneration:
        base: 0.13
        per-level: 0
    ...
```

The most important part of balancing your classes: every class stat scales on the player level. You can edit the class stats here. The stat formula is the following: `stat = <base> + <player-level> * <per-level>`.

By default, all classes will use the base stats from **stats.yml** so you do not have to specify anything redundant in the attributes section. Changing these will override the formulas specified in stats.yml.

You may also add min/max caps so that classes don't get too overpowered:

```yaml
attributes:
    max-health:
        base: 18
        per-level: 3
        max: 80
```

## Mana Display Options

Every class can have a different mana bar (mana for mages, rage for warriors...). The `char` option corresponds to the character which will be used to display the player's mana bar inside a chat message. The `color` config section corresponds to the color being used to generate that bar. The `icon` option corresponds to the mana icon displayed on the player action bar.

```yaml
mana:
    char: '♦'
    icon: '&c♦'
    color:
        full: DARK_RED
        half: RED
        empty: WHITE
    name: 'Rage'
```

## Subclasses

Subclasses are classes which are available only when players reach a certain level. This is a way to make your class architecture more diverse by adding multiple new paths and playstyles.

```yaml
subclasses:
    ARCANE_MAGE: 10
```

Simply give the class ID and the level at which the subclass should be unlocked. When a player has a subclass available, a slightly different menu will pop up when using `/classes`. Nothing else is different for a subclass. Display, attributes, skills, etc are all setup the same. That obviously means you will need to create a separate config file for your subclass and put its reference in that `subclasses` section.

Since you most likely want your players to access these subclasses only by leveling previous (sub)classes, you will most likely use the `display: false` class option (see above) so that your subclass does not display in the class list when using `/classes`.

## Skills

Each class has its own set of skills. Learn more about class skills on [this wiki page](../skills/config.md).

## Skill Slots

Each class has its own set of skill slots. Learn more about skill slots on [this wiki page](../skills/binding.md#skill-slots).

## Linking a skill tree to a class

Skill trees are class based which means that the [skill trees](skill-trees.md) you can see and your progress for them depends on your current class. Each player can only progress in the skill trees linked to its current class. You can link skill trees to a class like this:

```yaml
#For the mage class
skill-trees:
    - 'general'
    - 'mage-arcane-mage'
```

## Casting Mode Particles

This option determines the particles displayed when the player is in [casting mode](../skills/casting.md). At the moment, the particle effect pattern cannot be edited (elegant particle helix rotating around the player): you may only change the particle used to draw that helix.

```yaml
cast-particle:
    particle: SPELL_INSTANT
```

Some particles require a color to be displayed, like the Redstone particle which is named `DUST` in Minecraft 1.21. The following format will let you modify the particle color.

```yaml
cast-particle:
    particle: REDSTONE
    color:
        red: 255
        green: 100
        blue: 0
```

Some particle require you to provide a block, which you can do using the following format. Some examples include `BLOCK`, `FALLING_DUST` and `DUST_PILLAR` in 1.21.

```yaml
cast-particle:
    particle: BLOCK_BREAK
    material: DIRT
```

In order to disable casting particles you will need to delete the cast-particle section from your class config file.

## Class Scripts

Class scripts are a replacement for event triggers (see below). You can define scripts which will apply to players with the corresponding class. These scripts can be used to code complex custom skill behaviours, class passive skills, or literally anything.

Like most skills and scripts, class scripts have a trigger type associated to them, determining when this script will activate. You can find the list of all available trigger types on [this MythicLib wiki page](../../mythiclib/skills/triggers.md). You can also learn how to write MMOLib custom scripts on [this MythicLib wiki page](../../mythiclib/scripts/intro.md).

Here is an example of a script for the _Warrior_ class, that converts 10% of physical damage dealt into Rage points, up to a maximum of 10 Rage pts simultaneously.

```yaml
scripts:
    ATTACK:
        conditions:
        - 'has_damage_type{types=PHYSICAL}'
        mechanics:
        - 'mana{amount="min(10, 0.1 * <attack.damage>)"}'
    #DAMAGED: ....
```

The following format also works, as long as the script named `some_script_id` has already been defined somewhere else.

```yaml
scripts:
    ATTACK: some_script_id
```

## Event Triggers (deprecated)

Event triggers let you perform specific actions when a specific event happens (player leveling up, dealing physical damage, choosing his class). **It's the feature that you should be using to give your players attribute and class points as they level up.**

```
triggers:
    weapon-damage:
    - 'mana{operation=GIVE,amount=2-3}' # Rage charges when dealing weapon damage
    physical-damage
    - 'mana{operation=GIVE,amount=2-3}' # Rage charges when dealing phys damage
    
    # Give a class point when leveling up
    level-up:
    - 'command{format="mmocore admin skill-points give %player_name% 1"}'
    # Run a message when you reach the Farming Profession Level 2
    level-up-Farming-2:
    - 'message{format="&eYou leveled up &a&lFarming &eto: &aLevel %mmocore_profession_farming%&e!"}' 
```

**Important note (can be confusing): events differ from the triggers. An event is what takes place, like a player leveling up or choosing his class, while the trigger is the action performed in response to that event. When setting up your class event triggers, you need to specify what action is performed (trigger), and when it is performed (event).**

| Option | Usage | Description | Replaced by |
|--------|-------|-------------|-------------|
| Main Class Level-Up | `level-up` | Triggers on every single main class level-up | Class exp tables |
| Specific Main Class Level-Up | `level-up-{#}` | Triggers on a specific main class level-up | Class exp tables |
| Multiple Main Class Level-Up | `level-up-multiple-{#}` | Triggers on every {#} main class level-ups | Class exp tables |
| Profession Level-Up | `level-up-{profession}` | Triggers on a profession level-up | Profession exp tables |
| Specific Profession Level-Up | `level-up-{profession}-{#}` | Triggers on a specific profession level-up | Profession exp tables |
| Multiple Profession Level-Ups | `level-up-multiple-{profession}-{#}` | Triggers on every {#} profession level-ups | Profession exp tables |
| Melee Damage | `melee-damage` | Triggers when the player takes melee damage | Class scripts |
| Physical Damage | `physical-damage` | Triggers when the player takes physical damage | Class scripts |
| Magic Damage | `magic-damage` | Triggers when the player takes magical damage | Class scripts |
| Class Chosen | `class-chosen` | Triggers when the player chooses a class from the /class menu | Nothing yet |

Triggerable events, for the most part, should be self-explanatory; For the `multiple` level up triggers, if you were to specify a `2` for the trigger, that would fire the trigger at every interval of the number 2 - `2, 4, 6, 8` and so on.

A full list of available triggers that can be used in conjunction with these events can be found [here](../misc/triggers.md).

## Disabling MMOCore classes

In some cases you might want to fully disable classes and/or leveling within MMOCore. This is rather simple to do:

- Delete the content of the `/class` folder (do not delete the whole folder, as it will regenerate). This has the effect of disabling classes and leveling all together.
- Inside the `commands.yml` config file, remove the `/class` and `/skills` command.
- Edit the `/gui/player-stats.yml` UI so that it does not display class information anymore.

If you would like to keep classes but disable leveling, remove all references to exp tables from within the `/class` and/or `/profession` folders. Classes and/or professions will be stuck to level 1. Don't forget to also edit the `/gui/player-stats.yml` UI so that it does not display information about leveling anymore.