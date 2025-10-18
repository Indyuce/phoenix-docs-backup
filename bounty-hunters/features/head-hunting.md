---
order: 7
---

# 💀 Head Hunting

The _Head Hunting_ feature, when enabled, requires bounty hunters to collect the head of the bounty target in order to claim the bounty. Hunters need to bring the head to the bounty creator by right clicking them with the head in their hand. Doing so will claim the bounty and give the reward to the hunter.

```yml
# When enabled, players have to bring the target's head back to the
# bounty creator and right click it in order to claim the bounty.
# Make sure you both disable 'drop-head.killer' and 'drop-head.creator'
# Reload your server when changing this option.
head-hunting:
  enabled: false
```

Make sure you enable [head drops](#head-drops) when using head hunting so that hunters can actually get the head of their target when killing them.

We also recommend toggling off the following option to avoid bounties to stack. When toggled off, two different players placing a bounty on the same target will result in two different bounties, instead of one larger bounty.

```yml
# When disabled, using /bounty will NOT increase the player's
# current bounty but will rather create one new bounty with the
# very same target.
bounty-stacking: true
```

If this option is toggled off, two heads will drop and the hunter will have to bring both heads to the respective bounty creators in order to claim both bounties, as if it were two different bounties. It's up to you to decide whether you want this option enabled or not!


## Head Drops

When claiming a bounty, the head of the bounty target may drop. You can configure this feature in the main config file. You may also choose the chance for a player head to drop whenever a bounty is claimed.

```yml
# Drops the player head when claming a bounty or give the head to
# the bounty creator. Make sure you disable the 'drop-head.killer'
# option when toggling on.
drop-head:

  # Drops the head on the ground.
  killer:
    enabled: false
    chance: 100

  # Give the head to the bounty creator or saves it in the bounty head
  # GUI that can be opened using /redeembountyheads. This option can also
  # be used with Head Hunting to give the head to the right clicked player.
  creator:
    enabled: false
    chance: 100
```

Notice there are two different options there. The first one is to make one head drop on the floor whenever the bounty target is killed.

The _creator_ option can be used to **give a player head to the bounty creator**. If the bounty creator is offline, or else if his inventory is full the moment the bounty is claimed, the head is saved and can be redeemed for free using _/redeembountyheads_ whenever he wants. He will receive the player head instantly in his inventory if he has one free slot.
