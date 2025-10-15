---
order: 2
---

# 🔌 Installation Guide

## Installation

MMOProfiles is pretty much usable right of the bat after installation with default configuration. When logging in for the first time, players who have already played on the server before will see a profile with their old data saved inside of it. This is an optional feature and can be disabled in the main plugin configuration file.

## Disable Spigot player data saving

Enable this option in your `spigot.yml` config file for the best MMOProfiles experience possible. This option tells Spigot to **stop saving player data** inside of your world data folder. MMOProfiles already handles all the player data saving stuff, so this basically reduces data duplication. It's still a dangerous option to play with, so bear that in mind!
```yml
players:
  disable-saving: true
```

If you're fine with losing your previous player data, you may also clear the `/world/playerdata` folder right away after enabling this option. If you enable this option and do not clear the `playerdata` folder, MMOProfiles will transfer this data to a new profile the first time the player joins.

## Note for Multiverse-Core users

If you happen to use Multiverse-Core, you have to disable this option as well in `Multiverse/config.yml` as this option inteferes with the MMOProfiles profile selection feature. When toggled on, this option teleports players when joining for the first time, overriding MMOProfiles teleportation.

```yml
firstspawnoverride: 'false'
```