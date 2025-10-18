# 👨‍🚀 Player Data

## Obtaining player data
Since 2.3, player data is now mapped inside a `PlayerDataManager` instance that you can access using `BountyHunters.getInstance().getPlayerDataManager()`. Using the right method you can retrieve the corresponding `PlayerData` instance.


## Methods
| Getter | Setter | Description |
|---|---|---|
| ``getLevel()`` | ``setLevel(int)`` | The hunter's [[level|Leveling Up]]. |
| ``getClaimedBounties()`` | ``setClaimed..(int)`` | How many bounties the player claimed. |
| ``getSuccessfulBounties()`` | ``setSuccessful(int)`` | How many successful bounties the player created. |
| ``getTitle()`` | ``setTitle(Title)`` | The player's [[current title|Leveling Up]]. |
| ``getAnimation()`` | ``setAnimation(Quote)`` | The player's current [[bounty animation|Leveling Up]]. |
| ``getIllegalKills()`` | ``setIllegalKills(int)`` | Amount of illegal kills he performed. |
| ``getIllegalKillStreak()`` | ``setIllegalKillStreak(int)`` | Amount of illegal kills made since last respawn. |
| ``getRedeemableHeads()`` | ``add/remove...(UUID)`` | UUIDs of players whose heads the player may redeem. |

You can also access the player profile item using `data.getProfileItem()` (be careful, that skull item does **NOT** have any skull texture), the level progress bar using `data.getProgressBar()` and the number of bounties needed to level up using `data.getBountiesNeededToLevelUp()`.

### Extra

| Method | Usage |
|---|---|
| ``addLevels(int)`` | Give extra levels to the player with no level up message |
| ``addClaimedBounties(int)`` | Give extra claimed bounties |
| ``addSuccessfulBounties(int)`` | Increases count of bounties created by the player, and claimed by others. |
| ``addIllegalKills(int)``| Add kills to the illegal kill streak & total counter |
| ``hasUnlocked(LevelUpItem)`` | Checks if a player has unlocked an item |

## Player Hunting

Learn about player hunting on this [wiki page](../features/player-hunting.md).

| Method | Usage |
|---|---|
| `setHunting(Bounty)` | Forces the player to hunt a player |
| `isHunting()` | True if the player is on a hunt |
| `stopHunting()` | Quits player hunting |

## Manipulating the player level

Keep in mind the `PlayerData` instance does **NOT** store what items (quotes/titles) the player unlocked. These are recalculated every time the player is prompted the item list. You may check if a player has unlocked an item using `hasUnlocked(LevelUpItem)` where `LevelUpItem` is an abstract class which `Quote` and `Title` both extend.

## Plugin Inventories

The following code can be used to open the bounty list to a player.
```java
PlayerData playerData = BountyHunters.getInstance().getPlayerDataManager().getPlayerData(/* player UUID */);
PlayerGUI.BOUNTY_LIST.build(playerData).open();
```

Available GUIs are `BOUNTY_LIST`, `HUNTER_LEADERBOARD` and `REDEEMABLE_HEADS`.