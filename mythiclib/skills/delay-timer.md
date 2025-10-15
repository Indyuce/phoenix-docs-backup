# Delay and Timer

### Skills that run every X ticks (timers)
`TIMER` is a special trigger type that casts a skill every X ticks. To setup timed skills, simply define the timer period in ticks using the `timer` skill modifier. This is a default skill modifier for **ANY** skill, just like `cooldown` or `mana`. If the skill trigger is not set to `TIMER`, this skill modifier becomes 100% useless and you can just ignore it.

### Adding delays to skills
Since MythicLib 1.5, any skill can have a **casting delay**. When casting such skill, the player is temporarily slowed down and must wait a small period of time before the skill is actually cast. This makes for a great RPG feature for skills like teleports or other super powerful skills.

You can configure specific options for the casting delay in the MythicLib config file:
```
# What happens when the player is waiting for his skill to cast
# Does not apply if skill delay (it is a skill modifier) is set to 0
casting-delay:
  slowness: 50 # A % based speed reduction when casting
  cancel-on-move: false # If the casting should cancel if the player moves

  cast-script: # MythicLib script called when the countdown begins
    enabled: true
    script:
      mechanics:
        play_sound:
          type: sound
          sound: BLOCK_END_PORTAL_FRAME_FILL
          volume: 1
          pitch: 2

  cancel-script: # MythicLib script called if the countdown is cancelled
    enabled: true
    # Other format:
    # script: <public_script_name>
    script:
      mechanics:
        play_sound:
          type: sound
          sound: ENTITY_VILLAGER_NO
          volume: 1
          pitch: 2

  bossbar: # Displayed during casting delay
    enabled: true
    format: 'CASTING'
```

The `slowness` option dictates how much the player is slowed down during the skill delay. When enabling `cancel-on-move`, the skill will cancel if the player moves: in that case, adding slowness is pretty useless.

`cast-script` is the MythicLib script ran when the player enters the casting delay. By default, it simply plays a little sound. `cancel-script` is the script ran **if** the player cancels the skill while waiting. It will therefore only be triggered if `cancel-on-move` is enabled.

You can also choose to enable or disable a custom bossbar which will display `CASTING` to the user.