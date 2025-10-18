---
order: 2
---

# 💸 Economy & Taxes

What would a bounty plugin be without a proper economy and tax system? 🤑

## Taxes

In order to prevent your players from abusing bounties, you may use taxes to make them think twice before creating/removing a bounty. Using the config, you may configure a set percentage of the reward that will be taken whenever a player either creates a bounty, adds money to someone's bounty or takes off the money he had put on someone's head.

::: tip
We recommend using a big tax, say 10%, on bounty claims to stabilize your economy, as that would be the equivalent of VAT.

You can also then use a smaller tax, like 1-3%, on bounty removal to discourage players from creating fake or useless bounties. If you tax bounty removal instead creation, players will be encouraged to create bounties, which is good for your server's activity!
:::

```yaml
bounty-tax:

  # Tax taken when claiming a bounty.
  # Most important tax, basically VAT
  bounty-claim:
    flat: 0
    scale: 5
    #min: 10       # Absolute minimum of tax taken
    #max: 1000     # Absolute maximum of tax taken
    #min-scale: 3  # Minimum % of the bounty amount taken as tax
    #max-scale: 50 # maximum % of the bounty amount taken as tax. Cant be more than half

  # Tax taken when creating a bounty (to fight abuse).
  # By default, no discouragement from creating bounties.
  bounty-creation:
    flat: 0
    scale: 0
    #...

  # Tax taken when a player removes the bounty he set.
  # Discourages players from creating fake or useless bounties.
  bounty-removal:
    flat: 0
    scale: 3
    #...

  # Tax when targeting a player
  # Avoids players spamming the chat with target messages
  # (You can also remove those messages instead of using a tax)
  target-set:
    flat: 100
    scale: 1
    #...
```


## Minimum/maximum reward
Using this config option, you can decide the minimum and maximum amount of money a player can add to a bounty.

```yaml
# Min and max bounty rewards.
# Set max to 0 to remove the max restriction.
min-reward: 0
max-reward: 0
```

