# ⚔️ Combat

## Combat Logging
Combat logging is a useful feature which lets players know when they enter or quit combat. Combat log is handled via chat messages. It is a very bare-bones feature in itself, but **it ties in so nicely with other mechanics like skills**: for instance there is a skill that makes players deal significantly increased damage when performing a melee attack that gets him into combat. You may also imagine a skill where the player gets increased damage for each second they spend in combat.

![image](uploads/0d9fba444da20e6dccca654bb16de446/image.png)

## Resource Regeneration
Combat log also dictates when the player should be able to regen their resources i.e health, mana and stamina. For instance, you can setup a Warrior class which has a base flat health regeneration rate, and which additionally regens 10% of his missing health every second **when out of combat**. This can be applied to any class, any resource, the off combat option can be disabled, the % can scale on the player's level, and you can make it so the regenerated amount also scales on the player's **missing** health instead. More information [over this page](Player Resources).

## PvP/PvE Interaction Rules
These rules basically determine in which contexts any given player can "interact" with another player. An "interaction" may refer to a skill or an attack. This obviously depends on the location of the two players (is the PvP flag on?), the relationship between the players (are they in the same party/guild?) as well as the interaction type (is it a damaging skill, or a buff?).

Player interactions include anything from healing/buff skills, to MMOItems staff/whip/musket attacks or even simple melee or projectile vanilla attacks. There are some interactions that we want to disable>: for instance, being able to damage or cast damaging skills onto party/guild members. Interaction rules are mainly designed to disable friendly fire.

Two players can have two different _relationships_ (as defined above) at the same time. They can be in the same party while being in different guilds (although it is quite rare) - in that case, PvP is disabled as long as one of the two relationships prevent PvP.

### Supported Group plugins
_By groups we are refering to factions, guilds, clans, kindgoms, etc. MMOCore handles these groups in the same way._
- [UltimateClans V6](https://polymart.org/resource/ultimate-clans-v6.1162)
- [Guilds](https://www.spigotmc.org/resources/guilds-30-sale.66176/)
- [KingdomsX](https://www.spigotmc.org/resources/kingdomsx.77670/)
- **MMOCore (not recommended)**
- Any Factions plugin (make sure you install [FactionsBridge](https://www.spigotmc.org/resources/factionsbridge.89716/)!)

### Supported Party plugins
- MMOCore
- [DungeonsXL](https://www.spigotmc.org/resources/dungeonsxl.9488/)
- [mcMMO](https://www.spigotmc.org/resources/official-mcmmo-original-author-returns.64348/)
- PartyAndFriends ([Spigot](https://www.spigotmc.org/resources/party-and-friends-extended-for-spigot-supports-1-7-1-19.11633/) & [Proxy](https://www.spigotmc.org/resources/party-and-friends-for-bungeecord-supports-1-7-x-to-1-19-x.9531/))
- [Parties](https://www.spigotmc.org/resources/parties-an-advanced-parties-manager.3709/)
- [Mythic Dungeons](https://mythiccraft.io/index.php?resources/mythic-dungeons.869/) ([DungeonParties](https://www.spigotmc.org/resources/mythicdungeons.102699/))
- [OBTeam](https://www.spigotmc.org/resources/obteam.108269/) ([DungeonMMO](https://www.spigotmc.org/resources/%E2%AD%90-dungeonmmo-%E2%AD%90-dungeon-world-generator-%E2%9C%85-create-your-dungeons-%E2%AD%95-endless-possibilities.106150/))

### What you can configure
MythicLib lets you configure a sort of three-dimensional array where you can choose to enable OR disable any combination of these three parameters:
- if PvP is enabled (`on` or `off`)
- the type of interaction (`support` or `offense`)
- the players relationship (`party_member`, `guild_enemy` etc.)

**This is located in the main MythicLib config file!**
```yaml
interaction_rules:

  # When enabled, apply PvP interaction rules for skills, melee and projectile hits.
  # This option is toggled off by default to reduce confusion for new users.
  enabled: true

  # When disabled, support-based skills (buffs or heals)
  # may only be applied onto players.
  support_skills_on_mobs: true

  # When PvP is turned off
  pvp_off:

    # Ability to heal other players when PvP is off
    support:
      party_member: true
      party_other: true
      guild_ally: true
      guild_neutral: true
      guild_enemy: true

  ## When PvP is turned on
  pvp_on:

    # Ability to heal other players when PvP is on
    support:
      party_member: true
      party_other: false
      guild_ally: true
      guild_neutral: true
      guild_enemy: false

    # Friendly fire for guilds/parties
    offense:
      party_member: false
      guild_ally: false
      guild_neutral: true
```

The `support_skills_on_mobs` determines if you can cast support skills/heals/buffs onto monsters. Only for default skills.

## Custom skills from MythicMobs
Interaction rules can be used in custom skills added from MythicMobs. The user manual is available [here](https://gitlab.com/phoenix-dvpmt/mythiclib/-/wikis/Using%20MythicMobs#checking-if-the-skill-caster-can-target-another-entity).

## PvP Mode
This feature is specially designed for PvE servers which still want to leave some options for players to fight. In specific WorldGuard regions where PvP is disabled by default, players can use `/pvpmode` to toggle on PvP back and fight other players! **Only players with PvP enabled can fight and attack each other.** Furthermore, this feature is fully compatible with the PvP interaction rules defined above.

This suits well RPG or even profession/job-oriented survival servers and is a quite unique RPG feature!

_PvP Mode only works with WorldGuard! It won't work with other flag plugins like Residence._

How to setup PvP Mode:
- first setup PvP interaction rules as explained above.
- select an existing/create a new WorldGuard region
- toggle **ON** server PvP, world PvP as well as the PvP flag
- toggle on the `pvp-mode` flag (toggled off by default)

You are now good to go! When the `pvp-mode` flag is on, players have access to the `/pvpmode` command and MMOCore will take care of the rest.

### Configuration
In order to prevent abuse, you can configure Pvp Mode so that players can't exit it while they are still in combat. Moreover, you can setup cooldowns for that command.

**This is located in the main MMOCore config file.**
```yaml
pvp_mode:

  # Requires /reload when changed
  enabled: false

  # Minimum level in order to fight other players.
  # Set to 0 to fully disable
  min_level: 0

  # Maximum level difference in order to fight other players.
  # Set to 0 to fully disable
  max_level_difference: 10

  # Delay after any attack during which the player will stay in PvP Mode (seconds)
  # Has to be lower than 'cooldown.combat'
  combat_timeout: 30

  # Invulnerability triggered when:
  # - entering a PvP region with PvP mode turned on.
  # - using the /pvpmode command inside of a PvP region.
  invulnerability:
    time:
      region_change: 60
      command: 30

    # When enabled, players can damage other players
    # to end this invulnerable time period.
    can_damage: false

    # When enabled, leaving a no-PVP zone and entering a
    # PVP zone will apply the SAME invulnerability time.
    # Requires /reload when changed
    apply_to_pvp_flag: true

  cooldown:

    # Cooldown before being able to use the /pvpmode
    # command when entering a PvP mode region.
    region_enter: 20

    # Cooldown before being able to use the /pvpmode
    # command when entering a PvP mode region.
    region_leave: 20

    # Delay before being able to use /pvpmode after being in combat (seconds).
    # Has to be greater than the 'combat_timeout'
    combat: 45

    # Cooldown when toggling on PvP mode, before being able to toggle it off (seconds)
    toggle_on: 5

    # Cooldown when toggling off PvP mode (seconds)
    toggle_off: 3
```

If you want to disable PvP mode, remove the `pvp-mode` config section from `commands.yml` and set `pvp_mode.enabled` to `false` in `MMOCore/plugin.yml`. This will fully disable the functionnality.