---
order: 3
---

# ⚙️ Config Options

## Different map servers

This is a useful option when connecting multiple servers which do not share the same maps. Imagine a player quits a server and joins another one: should they be teleported to their last location with no direct correspondence in the server they just joined, as the maps are not the same?

This is only an issue with survival servers as most full-RPG server proxies use a shared ungriefable map.

This issue applies to the following location-based data types:
- last location
- bed spawn point
- compass target

This issue can be fixed by giving servers a different server identifier. Servers with the same identifier will share saved locations, but servers with two different IDs will NOT share location-based player data.
```yml
server-identifier: 'default'
```

## Synced data 
This field enables you to enable or disable sync for all the vanilla features. If a field is set to false then changing profile won't change the corresponding data.

```yml
# Customization of the data that is synced or not between profiles.
synced-data:
  health: true
  health-scale: true
  food-level: true
  saturation: true
  walk-speed: true
  fly-speed: true
  allow-flight: true
  flying: true
  exp: true
  level: true
  air-level: true
  location: true
  respawn-location: true
  compass-target: true
  game-mode: true
  inventory: true
  ender-chest: true
  potion-effects: true
  attributes: true
  invulnerable: false
  balance: true
```

## Spawn Locations

`profile-selection-location` is where the players are teleported when joining the server, in order to choose their profile. It should be a closed or confined area where they can't see much as they might be able to move while the profile selection UI is closed.

```yml
# Location where players spawn to select their profile
profile-selection-location:
  world: 'world'
  x: 110
  y: 63
  z: -149
```

`new-profile-spawn-point` is where players are teleported when starting playing with a profile they just created. It could be some location telling command blocks/another plugin to just random-teleport them somewhere else.

```yml
new-profile-spawn-point:
  world: 'world'
  x: 110
  y: 63
  z: -149
```

## Profile Names
When enabled, profiles have names and users are asked to provide a name when creating a new profile. When disabled, MMOProfiles will just use "Profile nX" where X is the profile number.
```yml
use-profile-names: false
```

## Default Profile

::: warning
Risk of data loss! Toggling off this option will make existing players lose data if it is not associated to any profile! This is why it is toggled ON by default.
:::

When enabled, players who are not joining the server for the first time will have a default profile containing their previous player data. This is a mandatory option for existing production servers willing to install MMOProfiles while a player base has already built.

```yml
default-profile: true

# The default name of player's main profile
default-main-profile-name: 'Main'
```

## How to handle deleted worlds

This option fixes players respawning in deleted worlds.

Profile plugins have issues with Dungeons plugins as players sometimes respawn in a temporary dungeon world which no longer exist. To fix this, MMOProfiles stores the last player's location outside of these temporary worlds, in case a player logs out while still being in one of them.

Permanent worlds are not temporary, which means MMOProfiles is allowed to have players respawn in these worlds instead. If MMOProfiles find no recent permanent world in which the player was, it will simply bring the player back to the profile spawn point which is sometimes unwanted behaviour.
If the world still exists however, the player will respawn normally.

```yml
permanent-worlds:
  - 'world'
  - 'world_nether'
  - 'world_the_end'
  - 'another_world'
```

## Blacklist for inventory slot

This option can be used to prevent MMOProfiles to interact with specific slots used as buttons for other plugins like MMOInventory or ItemJoin. Leave to [] to disable. Example: [ 9, 10, 11, 12 ]
```yml
inventory-slot-blacklist: [ ]
```

## Reopen GUI

Amount of ticks MMOProfiles will wait before opening the profile selection GUI again, in case the player hasn't chosen a profile yet.
```yml
gui-close-timeout: 40
```
## Force stats

When enabled, sets the player's game mode on profile selection.
```yml
force-game-mode:
  enabled: false
  game-mode: SURVIVAL
```
When enabled, sets the player's invulnerability state on profile selection.
```yml
force-invulnerability:
  enabled: true
  state: false
```

## Unique Profile

This plugin can also be used in a totally different way to synchronize all the player data between multiple proxy-connected (BungeeCord/Velocity) servers. This can be achieved by setting the field `unique-profile` to true. 

```yml
unique-profile: false
```


In this mode, the profile selection UI never shows up, and the plugin is totally invisible for the players. It only synchronizes all the vanilla & plugin data of a player between multiple servers.


## How to handle resource packs

If you have a server resource pack, toggle on this option. MMOProfiles will wait for your resource pack to fully load before opening the profile selection UI for the first time.

```yml
resource-pack-options:
  wait-for-resource-pack: false
  resource-pack-load-delay: 40
```


## Disable opening profile select GUI

This option is compatible with proxy-based profile selection. When enabled, MMOProfiles will NOT automatically open the profile selection GUI on login. You can then manually open it using `/mmoprofiles open <player_name>`. There are no safeguards when using this option!

```yml
no-gui-on-login: false
```

This option can be used for login cinematics and events. This option is not compatible with the `wait-for-resource-pack` option.

::: warning
Risk of player data loss! If no plugin/command opens up the profile selection UI, any progress made before choosing a profile will be lost. 
:::

## Amount of profile/character slots available
```yml
default-slots: 5
```
This option dictates how many profile slots any player has by default. However, if you want your server to have ranks, you can use the following option.

```yml
ranks:
  vip:
    permission: 'rank.vip' # You can change this permission to anything you'd like.
    slots: 7 # Amount of profiles the player has access to
    name: 'VIP' # Purely visual, used in the profile section UI
  vip_plus:
    permission: 'rank.vip_plus'
    slots: 10
    name: 'VIP+'
  mvp:
    permission: 'rank.mvp'
    slots: 12
    name: 'MVP'
  mvp_plus:
    permission: 'rank.mvp_plus'
    slots: 15
    name: 'MVP+'
```
You can specify as many ranks as you'd like (the `vip` or `vip_plus` keys do not matter, they are only used internally but have to differ). You need to provide a rank name, that will display in the profile UI on locked profile slots using the placeholder `{rank}`. You also need to provide the amount of profile slots every rank has. Ranks don't have to be ordered in the config, MMOProfiles will do it for you.

## Scripts

You can specify certain scripts that are ran when specific actions get done. These scripts have to be in the [MythicLib format](https://gitlab.com/phoenix-dvpmt/mythiclib/-/wikis/Custom%20Scripts). The `login` script is performed right after player login, when his MMOProfiles player data is successfully loaded (it might take a few ticks). The `profile-select` script is ran after the player chooses a profile, when all of the data from supported plugins is loaded (it might take a few ticks as well).

```myl
script:

  # MythicLib script ran when the player creates a new profile.
  profile-create:
    mechanics:
      send_message:
        type: tell
        format: 'Welcome to your new profile!'

  # MythicLib script ran when the player logs in (before profile selection).
  login:
    mechanics:
      send_message:
        type: tell
        format: 'Welcome! Please choose the profile you''d like to play on.'

  # MythicLib script ran when the player chooses a profile (after login).
  profile-select:
    mechanics:
      play_sound:
        type: sound
        sound: ENTITY_PLAYER_LEVELUP
      send_message:
        type: tell
        format: 'Have fun!'
```


## Proxy-Based Profiles

When enabled, MMOProfiles switches to a proxy-based behaviour, enabling players to switch/spoof UUIDs. This tricks other plugins into thinking another player is joining the server, enabling profile-specific progress with literally ANY plugin. Prox-basedy profiles have their own dedicated [wiki page](proxy-based).