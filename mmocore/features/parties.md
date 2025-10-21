# 👯 Parties

Parties are a basic system built into MMOCore where you and up to 7 friends can party up for extra boosts and information! This system is a great groundwork for party integration into other plugins such as DungeonsXL.

## How to use
To begin, you can type the /party command. If you are not already in a party, it will ask you if you want to create one.\
After that, you will be brought into the main party GUI. Inside the GUI is where you will invite your friends, and see the information on the party. By default, parties give a slight regeneration and experience boost. The more players in your party, the greater the buff (see below).

![7Vx1Ld2](uploads/4115203f28cf342ec245efbe6c3b4196/7Vx1Ld2.png)

## Party Chat
Players can talk via party chat using @ at the beginning of their message:

![3zFCOei](uploads/cf8a7b13172530d88f4b4a3ef278e9d5/3zFCOei.png)

## Party Buffs
Party buffs are extra statistics that everyone in a party will get as long as they are more than 2. These buffs are configurable in the main config.yml file. Here is the `party` config section in the config.yml file.
```
party:

    # Edit party buffs here. You may
    # add as many stats as you want.
    buff:
        health-regeneration: 3
        additional-experience: 5
    
    # Prefix you need to put in the chat
    # to talk in the party chat.
    chat-prefix: '@'
```

These buffs are displayed on a cake icon when opening the player stats menu, that you can configure under the `/gui/player-stats.yml` config file:

![CX0lIKA](uploads/1af871d02b5bb9971653ac9d5185515b/CX0lIKA.png)
```
    party:
        slots: [16]
        function: party
        item: CAKE
        name: '&aParty Morale'
        lore:
        - '&7&oPlaying with your friends'
        - '&7&ogreatly encourages you!'
        - ''
        - '&7Party Bonuses ({count}):'
        - '&8- +{buff_additional_experience}% Experience Earned!'
        - '&8- +{buff_health_regeneration}% Health Regeneration'
```

## Exp splitting
Since MMOCore 1.9.3, the experience earned by any player is evenly split over all the party members. If your party has a total of 4 members you will only earn 25% of the exp you'd get with no party. This makes sure all the party members level up at the same time.

This feature creates an issue where low level players can join the party of high level players and get huge amounts of exp. This can be fixed by using the `max-level-difference` in the MMOCore main config file. For instance, setting this option to 5 will prevent level-1's from joining parties of level-7's or more. The level of the party is determined by the initial party owner's level.

That feature stays operational even if you are using another party plugin. It also supports profession experience.

## Using other party plugins
If you'd like to use a more advanced party plugin, you can take advantage of the modularity of MMOCore and use any of the following plugins:
- MMOCore
- [DungeonsXL](https://www.spigotmc.org/resources/dungeonsxl.9488/)
- [mcMMO](https://www.spigotmc.org/resources/official-mcmmo-original-author-returns.64348/)
- PartyAndFriends ([Spigot](https://www.spigotmc.org/resources/party-and-friends-extended-for-spigot-supports-1-7-1-19.11633/) & [Proxy](https://www.spigotmc.org/resources/party-and-friends-for-bungeecord-supports-1-7-x-to-1-19-x.9531/))
- [Parties](https://www.spigotmc.org/resources/parties-an-advanced-parties-manager.3709/)
- [Mythic Dungeons](https://mythiccraft.io/index.php?resources/mythic-dungeons.869/) ([DungeonParties](https://www.spigotmc.org/resources/mythicdungeons.102699/))
- [OBTeam](https://www.spigotmc.org/resources/obteam.108269/) ([DungeonMMO](https://www.spigotmc.org/resources/%E2%AD%90-dungeonmmo-%E2%AD%90-dungeon-world-generator-%E2%9C%85-create-your-dungeons-%E2%AD%95-endless-possibilities.106150/))

Just go in your main MMOCore config file and change this option to whatever plugin you have installed:
```
# Edit the plugin handling parties here.
# Supported values (just copy and paste):
# - mmocore
# - dungeonsxl
# - parties
# - party_and_friends (Use this one if you are using Party and Friends Extended for Spigot)
# - party_and_friends_bungeecord_velocity (Use this one if you are using Party and Friends For Bungeecord, Party and Friends For Velocity or Party and Friends Extended Edition for Bungeecord/Velocity. This one requires https://www.spigotmc.org/resources/spigot-party-api-for-party-and-friends.39751/ to be installed)
# - mcmmo
# - obteam (addon for DungeonMMO)
# - mythicdungeons (only when using default party handler)
party-plugin: mmocore
```
The exp splitting mechanism will work exactly in the same way as described above for all the plugins listed. The party buff system works for all of them except party-and-friends(PAF).
