---
order: 6
---

# ⚙️ Triggers

Recipe triggers are recipe options which do not display in the recipe GUI item. They dictate actions which are performed when the recipe is used by a player.

```yml
recipes:
    steel-sword:
        ....
        triggers:
        - 'vanilla{type=STICK,amount=3}'
```

## Available Triggers

| Trigger    | Description                          | Format/Example                                            |
|------------|--------------------------------------|-----------------------------------------------------------|
| ``message``    | Sends a message to the player.       | `message{format="&aYour message here... "}`               |
| ``command``    | Makes the console perform a command. | `command{format="give dirt",sender=OP}`<br> *- Available senders: PLAYER, CONSOLE, OP* |
| ``sound``      | Broadcasts a sound to the player.    | `sound{sound=<SOUND_NAME>;volume=<VOLUME>;pitch=<PITCH>}` |
| ``vanilla``    | Gives a vanilla item to the player.  | `vanilla{type=DIAMOND;amount=3}`                          |
| ``mmoitem``    | Gives an mmoitem to the player.      | `mmoitem{type=SWORD;id=FALCON_BLADE;amount=1}`            |
| ``mmskill``    | Casts a MythicMobs skill. | `mmskill{id=MythicMobsSkillInternalName}`     |
| ``experience`` | Gives the player MMOCore experience.  | `exp{profession=<PROFESSION>;amount=<AMOUNT>}`|
