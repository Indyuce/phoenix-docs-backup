---
order: 1
---

# 🔥 Skills

Skills are amazing and unique abilities that players can use to defeat their enemies or buff their party mates fighting and surviving. Skills are either passive or active. Active skills are delibetarely cast by the player, and all require to be bound to a skill slot beforehand. Passive skills do not necessarily need to be bound to a skill slot, they are passively triggered by the player based on their interactions (attacks, other skills), movements...

Skills are class-specific. When changing class, a player will _lose_ their previous skills and gain new ones. Old skills from previous classes can still be covered when switching classes again.

## Binding active skills

Active skills all require to be bound to a skill slot before being cast.

Every player has multiple skill slots which they can use to bind active skills to certain keybinds. You cannot cast any active skill unless it is bound. The number of skill slots a player has is determined by the player's class, and is configurable : for example, magic-oriented classes like Mages and Wizards can have more skill slots (and therefore skill casting opportunities) than physical-oriented classes like Warriors or Brutes. You may find more information about skill slots under the [player classes](../features/classes.md) wiki page.

You may bind skills using the skill GUI (type `/skills` to open it up). You may see your current bound skills on the right side of the GUI. After selecting a skill by clicking on it, you can click any of the books on the right side to bind the selected skill. The book item will then update and show the bound skill. Some skill slots (see [Player Classes](../features/classes.md#skill-slots-since-1120) can have the `can-manually-bind` field toggled off, in which case the only way to bind a skill to this slot is to use the `/mmocore admin skill bind <skill> <player>` command.

![skillgui](uploads/ee836a64bbb6db9ab9e2f7d1f4208ca7/skillgui.gif)

**Once your skills are upgraded and bound, you may** [**cast**](Skill%20Casting) **them.**

## Binding passive skills

Since MMOCore 1.11, you can now choose whether or not some passive skills require binding. In your class skill configuration, set the `needs-bound` field to `false` to make your skill **permanent**. Permanent skills always take effect as soon as they are unlocked by the player. Only passive skills can be permanent.

In the following example, the passive skill _Power Mark_ for the _Mage_ class does not require to be bound to a skill slot in order to take effect. In other words, if the player has not bound this skill, they will still benefit from its effects. The following code snippet is taken from the `classes/mage/mage.yml` config file.

```yml
# classes/mage/mage.yml

# Other class options......

skills:
  # Other skills.....
  POWER_MARK:
    level: 5
    max-level: 30
    # .......
    needs-bound: false # Does not need to be bound to apply its effects
```

In the main MMOCore configuration file, you can also toggle off the option `passive-skill-need-bound`. By default, this option is set to true; this means that, unless specified otherwise, passive skills need to be bound to a skill slot in order to take effect.

## Upgrading a skill

Upgrading a skill **increases its power**. Players can choose the skill they would like to upgrade based on their play style and skill path they decided to follow. Upgrading a skill takes **one skill point** which are earned when leveling up. You can upgrade your skills in the skill GUI (`/skills`).

Select the skill you'd like to upgrade by clicking on it, once it's selected it will change the GUI name. You can then upgrade the selected skill by clicking on the corresponding item. On the upgrade item column, you can see how powerful the spell would be with a higher level.

![upgrade1](uploads/c4ab699df0b716956084647484ae40de/upgrade1.gif)

![upgrade2](uploads/402ce7c38f6b934b02783e69f5eab004/upgrade2.gif)

## Unlocking Skills

Each skill can be locked, unlocked but not usable, or usable. Locking a skill means that it cannot be seen in the player's skills UI, and the player is unaware of its existence. When a skill is unlocked, it becomes visible to the player UI but can only be bound to a slot if the player meets the level requirements associated with the skill. A skill can be unlocked or locked through [triggers](https://gitlab.com/phoenix-dvpmt/mmocore/-/wikis/Triggers)(recommended) or [commands](https://gitlab.com/phoenix-dvpmt/mmocore/-/wikis/Commands).

If you unlock a skill for which information is not filled in the class folder, it will be considered directly usable(at level 1) and won't be upgradable.

## Skill categories & formula

Each skill can be assigned to a list of categories through the field `categories`. By default, each skill is associated to two categories:

* its skill ID which name is the skill ID and to the categorie PASSIVE/ACTIVE depending on if it is an passive/active skill. These categories can be used to parse formulas and target a specific subset of skills.\
  \
  Formulas enable the user to check if a condition on the skill categories is met. You can use all the classic operators for the such as !(negation), ||(or) and &&(and). They can be used to filter which skills can be bound to a specific [skill slot](/phoenix-dvpmt/mmocore/-/wikis/20Classes#skill-slots-since-1120) or to apply [skill buffs ](https://gitlab.com/phoenix-dvpmt/mmocore/-/wikis/Player%20Skills#skill-buffs)to a subset of skills.



**Examples slot config for class file.** For more details check [Skill Slots](https://gitlab.com/phoenix-dvpmt/mmocore/-/wikis/Player%20Classes#skill-slots-since-1120)

```
# The valid format for 
formula: "<FIRE_STORM>" #Will only target fire storm
formula: "!<PASSIVE>&&<FIRE>" #Will target active skills with the fire category
#This is the same as <ACTIVE>&&<FIRE> 
```

**Example categories add to the skill file in the skills folder**

```
categories:
- "CATEGORY_1" #Referened with <CATEGORY_1> in a formula
- "CATEGORY_2"
```

## Skill Buffs

A skill buff modifies the value of a certain skill modifier. It can target one or multiple skills using [category formulas]() and can only target 1 modifier. Skill Buffs can only be created through [skill slots](https://gitlab.com/phoenix-dvpmt/mmocore/-/wikis/Player%20Classes#skill-slots-since-1120) and [triggers](https://gitlab.com/phoenix-dvpmt/mmocore/-/wikis/Triggers#available-trigger-types).

```
#Example

triggers: 
- 'skill_buff{formula="true";modifier="cooldown";amount=-10;type="RELATIVE"}' #-10% cooldown to all skills.
- 'skill_buff{formula="<FIRE_STORM>";modifier="damage";amount=20;type="FLAT"}'#+20 dmg to fire storm.
- 'skill_buff{formula="<MY_OWN_CATEGORY>";modifier="damage";amount=20;type="FLAT"}'
#Will target all the skills who have MY_OWN_CATEGORY in their categories list.
```

## Skill Folder


## Editing the skill menu

```
# GUI display name
name: 'Selected Skill: &6{skill}'

# Number of slots in your inventory. Must be
# between 9 and 54 and must be a multiple of 9.
slots: 54

items:
  skill:
    slots: [ 10,11,12,19,20,21,28,29,30,37,38,39]

    function: skill
    name: '&a{skill} &6[{level}]'
    lore:
      - ''
      - '{unlocked}&a✔ Requires Level {unlock}'
      - '{locked}&c✖ Requires Level {unlock}'
      - '{max_level}&e✔ Maximum Level Hit!'
      - ''
      - '{lore}'
  next:
    slots: [ 47 ]
    function: next
    item: PLAYER_HEAD
    texture: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTliZjMyOTJlMTI2YTEwNWI1NGViYTcxM2FhMWIxNTJkNTQxYTFkODkzODgyOWM1NjM2NGQxNzhlZDIyYmYifX19
    name: '&aNext'
    lore: { }
  previous:
    slots: [ 2 ]
    function: previous
    item: PLAYER_HEAD
    texture: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmQ2OWUwNmU1ZGFkZmQ4NGU1ZjNkMWMyMTA2M2YyNTUzYjJmYTk0NWVlMWQ0ZDcxNTJmZGM1NDI1YmMxMmE5In19fQ==
    name: '&aPrevious'
    lore: { }

  reallocate:
    slots: [45]
    function: reallocation
    item: CAULDRON
    name: '&aReallocate Skill Points'
    lore:
      - ''
      - 'You have spent a total of &6{total}&7 skill points.'
      - '&7Right click to reallocate them.'
      - ''
      - '&eCosts 1 skill reallocation point.'
      - '&e◆ Skill Reallocation Points: &6{points}'

  slot:
    slots: [ 8,17,26,35,44,53 ]
    function: slot
    item: GRAY_DYE

    name: '&aSkill Slot {slot}'
    no-skill: '&cNone'
    lore:
      - '&7Current Skill: &6{skill}'
      - ''
      - '{slot-lore}'
      - ''
      - '&7&oCast this spell by pressing [F] followed'
      - '&7&oby the keybind displayed on the action bar.'
      - ''
      - '&e► Left click to bind {selected}.'
      - '&e► Right click to unbind.'
      - '&e► Shift left click to select.'
  skill-level:
    slots: [ 6,15,24,33,42,51 ]
    function: level

    # Skill level offset, should be changed
    # according to the amount of inventory
    # slots the skill-level item occupies.
    offset: 2

    # Item displayed if the skill level is
    # too low to display a level item in the GUI
    too-low:
      item: AIR

    item: LIME_DYE
    name: '&a{skill} Level {roman}'
    lore:
      - ''
      - '{lore}'
  upgrade:
    slots: [ 15 ]
    function: upgrade
    item: GREEN_STAINED_GLASS_PANE
    name: '&a&lUPGRADE {skill_caps}'
    lore:
      - '&7Costs 1 skill point.'
      - ''
      - '&eCurrent Skill Points: {skill_points}'
```

First of all you can edit the general GUI settings like its name and slots.

```
name: Your Skills
slots: 45
```

Notice how the config sections that fall under the `items` section share very similar properties: `name` (the item display name), `lore` (the item description/lore), `item` (the item material), `slots` (where the item is placed in the inventory, it can be a list) and `function` (what the item does). These can (and should) all be edited to your needs.

### Editing Item Slots

If you want to have your item displayed on multiple slots, use something like

```
slots: [1, 2, 3, 4]
```

The following formats won't work

```
slots: 1
```

```
slot: 1
```

### Item Functions

`function` is the most confusing option when editing MMOCore custom GUIs. This option dictates how the item behaves when clicked, and what placeholders to parse in the item lore. Let's go over all the items in the GUI specifically.

`next` and `previous` are the easiest ones, these are the items used for pagination.

`skill` is the item displayed for every skill available to the player. Its lore is a bit complicated

- The line starting with {unlocked} only displays if the player has unlocked the skill
- The line starting with {locked} only displays if the player has NOT unlocked the skill yet
- The line starting with {max_level} displays when the player has reached the max skill level
- {lore} pastes the entire skill description (see [this](Player%20Skills#example-skill))



![image](uploads/2bfb6008eff5bb8e0f4d9222a18fd22d/image.png)

`switch` is the item that you'd click when switching from binding to upgrading mode\
![image](uploads/aa179808ecdfa336ecb45d1b55112b7a/image.png)

`skill-slot` is the item used in the binding mode\
![image](uploads/be06c771527a08258052ddfe00175cc1/image.png)

`skill-level` are the items used to tell the player how the selected skill would behave if it had a higher level\
![image](uploads/67597295b40adbcabb65c83386178082/image.png)

`upgrade` is the item clicked when you want to upgrade the selected skill\
![image](uploads/83bf45b898f68a89e5f9fa4a3d47ac49/image.png)\*\*\*\*