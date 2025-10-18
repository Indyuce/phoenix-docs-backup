---
order: 2
---

# 💸 Economy & Taxes

## Taxes

In order to prevent your players from abusing bounties, you may use taxes to make them think twice before creating/removing a bounty. Using the config, you may configure a set percentage of the reward that will be taken whenever a player either creates a bounty, adds money to someone's bounty or takes off the money he had put on someone's head.

```yaml
bounty-tax:
    # Tax taken when creating a bounty (to fight abuse).
    # In % of the money reward. Must be between 0 and 100.
    bounty-creation: 15
    
    # Tax taken when a player removes the bounty he set.
    # Default is 17.8% because it corresponds to 30% of the
    # initial amount when taking into account bounty creation tax
    bounty-removal: 17.8
```

## Minimum/maximum reward
Using this config option, you can decide the minimum and maximum amount of money a player can add to a bounty.

```yaml
# Min and max bounty rewards.
# Set max to 0 to remove the max restriction.
min-reward: 0
max-reward: 0
```

