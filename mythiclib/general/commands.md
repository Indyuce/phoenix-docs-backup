# 💾 Commands

| Command | Description |
|---------|-------------|
| `/ml reload` | Reloads the plugin and config files. |
| `/ml damage <source> <target> <value>` | Force source player to deal damage to target entity (name or UUID) |
| `/ml stat [...]` | More information on [this wiki page](../features/stats.md#using-commands) |
| `/ml debug cast <skill_id>` | Debug command to cast skill with given ID. |
| `/ml debug logs` | Dumps latest server logs to `mclo.gs` |
| `/ml debug stats <player>` | Open a GUI to explore stats of target player |
| `/ml debug attributes <player>` | Open a GUI to explore attributes of target player |
| `/ml debug versions` | Dumps plugin versions to chat |
| `/ml debug healthscale set <amount> <player>` | Sets health scale of given player |
| `/ml debug healthscale reset <player>` | Resets health scale of given player |
| `/ml debug test` | Developer command, do not use |
| `/ml debug parse ` | Developer command, do not use |

## Command Config

::: warning
This is only available for MythicLib and MMOCore at the moment.
:::

MMO plugins allow you to edit basic information of native plugin commands, including their name, description, usage, aliases and permission. All of these options are editable in the `commands.yml` file located in the main plugin folder.

Here is the content of the `MMOCore/commands.yml` file as an example:

```yml
mmocore:
  verbose: PLAYER
cast:
  main: cast
  aliases: []
  description: 'Enter casting mode'
  permission: 'mmocore.cast'
  verbose: ALL
player:
  main: player
  aliases: [ p, profile ]
  description: 'Displays player stats'
  permission: 'mmocore.profile'
  verbose: ALL

# [...]
```

The `main` option defines the command name, or label. If set to `player`, players have to type `/player` to execute the command. The `aliases` option allows you to define alternative labels for the same command. In the example above, players can also type `/p` or `/profile` to execute the same command as `/player`.

The `permission` option defines the permission required to execute the command. In the example above, only players with the `mmocore.profile` permission can execute the `/player` command.

## Command Verbose

::: warning
This is only available for MythicLib and MMOCore at the moment.
:::

In the same config file, you can also define a `verbose` level for each command. This option allows you to control where the command execution messages are sent. There are multiple verbose levels available:

| Level | Description |
|-------|-------------|
| `ALL` | Messages are sent to both the player and the console. |
| `PLAYER` | Messages are only sent to the player executing the command. This mode avoids console spam when using commands like `/ml stat add`. |
| `CONSOLE` | Messages are only sent to the console. |
| `REDIRECT_TO_CONSOLE` | All messages are sent to the console instead. This can be useful for logging important command executions. |
| `NONE` | No messages are sent. |

For instance, the following code snippet sets the verbose level of the main `/mythiclib` command, and all its subcommands, to `PLAYER`.
```yml
# MythicLib/commands.yml
mythiclib:
  verbose: PLAYER
```