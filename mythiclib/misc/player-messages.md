---
order: 90
---

# 💬 Player Messages

MythicLib provides unified syntax for messages sent to players by all MMO plugins.

Most MMO plugins have a `messages.yml` config file where you can edit messages sent by the plugin. Below is part of the `MMOCore/messages.yml` config file.

```yml
level-up:
  sound: ENTITY_PLAYER_LEVELUP,1,2
  # Runs a script on level up. This script is implemented
  # inside file MythicLib/scripts/mmocore_scripts.yml
  script: mmocore_level_up_effect
  message:
    - ''
    - '&eCongratulations, you reached level &6{level}&e!'
    - '&eUse &6/p &eto see your new statistics!'
    - ''
#......
exp-notification:
  message: '&f{profession} &e{progress} &e{ratio}%'
  action-bar: true
  #sound: ENTITY_EXPERIENCE_ORB_PICKUP # Not recommended, can be spammy
death-exp-loss:
  - ''
  - '&4You died and lost {loss} experience.'
  - ''
#......
already-on-class: '&cYou are already a {class}.'
```

In the next sections, we will take the example of the MMOCore message sent when a player levels up their main class (`level-up`) but this is applicable to any message from any MMO plugin.

## Basic Syntax

This sends one line of text to the player chat.

```yml
level-up:
  format: '&eCongratulations, you reached level &6{level}&e!'
```

This sends multiple lines of text to the player chat. As you can see, `format` can either be text or a list of texts.

```yml
level-up:
  format: 
    - '&eCongratulations, you reached level &6{level}&e!'
    - '&eUse &6/p &eto see your new statistics!'
```

## Disable a message

If you want to disable a message, say `level-up`, so that nothing is sent to the player when they level up, use the following syntax:

```yml
level-up: ''
#level-up: [] # This works too
#level-up: {} # This works too
```

## Send to action bar

If you want to send the message to the player's action bar instead, set `action-bar` to `true`.

```yml
level-up:
  format:
    - '&eCongratulations, you reached level &6{level}&e!'
    - '&eUse &6/p &eto see your new statistics!'
  action-bar: true
```

### Extra options

In MythicLib, the action bar is shared by all MMO plugins. To avoid action bar messages colliding with each other, we implemented a basic _message priority & timeout_ system.

Every message has a priority and a duration, which are both positive integers. One-time messages (such as level-up or waypoint use messages) usually have high priority, and passive messages like MMOCore player info and action bars usually have low priorities.

When multiple messages are sent simultaneously to the same player, only the message with highest priority will show on the player's action bar. The high-priority message will temporarily "hide" the message with low priority, for a set period of time (the message duration).

The message priority and duration can be edited using the following syntax

```yml
level-up:
  format: 'My message'
  action-bar: true # Has to be on
  priority: 30     # Message priority
  duration: 50     # In ticks, 2.5 seconds 
```

The MMOCore player information action bar runs on priority `LOW`, set to `20`. The MMOCore skill casting action bars run on priority `NORMAL` set to `30`.

## Play a sound

Sounds can be played when the message is sent to the player. The basic syntax is `<sound_name>,<pitch>,<volume>`. The sound name can be one of the following:
- a [Bukkit sound](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Sound.html),
- a custom sound provided by a resource pack, like `itemsadder:sound_id`,
- a Minecraft [vanilla sound](https://minecraft.fandom.com/wiki/Sounds.json/Java_Edition_values) like `minecraft:entity.zombie.ambient`.

If you want to set the pitch and volume to 1, you can simply use `<sound_name>`. Pitch ranges from 0.5 (low pitch) to 2 (high pitch) and defaults to 1. Volume defaults to 1.

```yml
level-up:
  format: #......
  sound: 'ENTITY_PLAYER_LEVELUP,1,1' # Or simply 'ENTITY_PLAYER_LEVELUP'
```

If you prefer YML syntax over comma-separated values, you can also use the following syntax:

```yml
level-up:
  format: #.....
  sound:
    sound: ENTITY_PLAYER_LEVELUP
    vol: 1
    pitch: 1
```

You can even remove the `format` field and only send a sound to the player, with no text sent to the player chat or action bar.

## Call a MythicLib script

You can run a MythicLib script when a message is sent to a player. For instance, MythicLib comes with a script named `mmocore_level_up_effect` which displays a small particle effect around the player. By default, it is called when the player levels up either their main class or a profession.

```yml
level-up:
  format: #......
  sound: #......
  script: 'mmocore_level_up_effect'
```

This is the code of the `mmocore_level_up_effect` script, which can be found in the `MythicLib/script/mmocore_scripts.yml` file.
```yml
# Script ran when leveling up
# Displays a helix of particles around the player
# This is configured in MMOCore/messages.yml > level-up.script
mmocore_level_up_effect:
  mechanics:
    - "helix{tick=mmocore_level_up_effect_tick;radius=1;height=2}"

mmocore_level_up_effect_tick:
  mechanics:
    - "spawn_particle{particle=TOTEM}"
```