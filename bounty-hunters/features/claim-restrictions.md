---
order: 3
---

# 🛑 Bounty Restrictions

A common problem with bounty systems is players abusing bounties on friends or alts in order to farm stats or rewards. BountyHunters provides several ways to restrict how players can create and claim bounties in order to prevent such abuses.

::: details Config Options

```yml
# Setting any parameter to 'true' means a new restriction applies.
# Make sure you restart your server when changing one of these options.
claim-restrictions:

  # Players may not claim their own bounties.
  # Disabled by default due to the bounty claim tax. If players
  # claim their own bounties, they will lose tax money.
  own-bounties: false

  # Players cannot claim bounties on players who
  # have close bed spawn points (most likely friends).
  bed-spawn-point:
    enabled: false

    # Blocks threshold
    radius: 100

  # Players may not claim bounties if they are in the same team.
  scoreboard-teams: false

  # Players may ONLY claim bounties if
  # they are tracking the bounty target.
  targets-only: false

  # Compatibility with PartyAndFriends and BungeeFriends
  # Players may not kill their friends to claim bounties.
  friends: true

  # Compatibility with Towny
  # Players may not kill members of the same town to claim bounties.
  town-members: true

  # Compatibility with Lands
  # A player cannot interact with a target bounty
  # if the player's land trusts the target
  lands: true

  # Compatibility with SimpleClans
  simple-clans: true

  # Compatibility with UltimateClans
  ultimate-clans: true

  # Compatibility with FactionsUUID/SaberFactions etc.
  factions: true

  # Compatibility with Guilds
  guilds: true

  # Compatibility with KingdomsX
  kingdoms: true
```
:::

For instance, you can prevent players from claiming bounties on their friends, guild members, faction members... All supported plugins are listed in the config file above.

You can also prevent players from claiming their own bounties, which may be useful if you disable the bounty claim/creation tax.

BountyHunters can also detect if players have their bed spawn point close to the bounty target player's bed spawn point. If so, they won't be able to claim the bounty. You can configure the detection radius in blocks.