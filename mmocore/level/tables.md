# 📋 Experience Tables

This feature was introduced in MMOCore 1.8.3 and was designed to let players claim more complex rewards when leveling up their professions. Its primary function is to give players leveling rewards every N profession levels. You can also configure a claim chance for every "experience drop" to have extra randomness. Here is the default `exp-tables.yml` config file

```plaintext
example_exp_table:
  first_table_item:

    # This item will drop every 3 levels
    period: 3

    # This item has a 80% chance in fact to drop
    chance: 80

    # The level at which the item will be claimed for the first time
    first-trigger: 5

    # Every successive fail in claiming the item will reduce
    # the risk of failing future claims by X%. With a 80%
    # fail reduction rate, chances become:
    # - 80%
    # - 96%
    # - 99.2%
    # - 99.84%
    # so on forever..
    #
    # This is better than just increasing the claim chance by a
    # certain amount each time because otherwise the claim chance
    # just becomes/surpasses 100% at some point.
    fail-reduction: 80

    # What happens when that item is claimed
    triggers:
      - 'exp{amount=20}'
      - 'command{format="broadcast That''s three levels"}'

  # Will be used at level 7,9,11,13
  second_table_item:
    period: 2
    first-trigger: 7
    last-trigger: 13
    triggers:
      - 'exp{amount=80}'
      - 'command{format="broadcast Boy, %player_name% level up twice in one of his(her) professions!"}'

second_exp_table:

  # Base exp every level up, sweet.
  some_item:
    period: 1
    triggers:
      - 'exp{amount=100}'

  # Extra exp every 3 levels
  some_other_item:
    period: 3
    triggers:
      - 'exp{amount=100}'

last_example:

  # Only triggers when getting lvl2
  # Perfect for meticulous exp tables
  level_two:
    level: 2
    triggers:
      - 'exp{amount=100}'

  # Only triggers at lvl 3
  # Perfect for meticulous exp tables
  level_three:
    level: 3
    triggers:
      - 'exp{amount=120}'
  
  # Etc.
  # Add as many items as you want
```

### General

An experience table is broken down into multiple _items_ (there is one config section for every item inside an exp. table). An _item_ is a set of rewards that has a X% chance of being claimed every Y profession levels. The `period` option (in levelups) indicates how frequently the item should be given to the player. The `chance` option determines the chance for the player to be given that item.

You can edit the rewards of an item by adding or removing triggers to the list identified by `triggers`. You can find [here](../misc/triggers.md) the list of all of the available triggers that you can use inside of exp tables.

### First & Last Trigger

Using the `first-trigger` option, you can select a level that the player has to reach before claiming an item. If the first trigger level is set to 5 and the period is set to 10, the item will be claimed by level 5, 10, 15 etc. If you don't specify anything for that setting, it's set to the item period by default.

The `last-trigger` option allows you to limit the level at which the item can be dropped. If the last-trigger is set to 8 with a period of 2, the item will be claimed at level 2,4,6 and 8. If nothing is specified the last-trigger will be set to infinity (no-limitation).

If you want an item to be only claimable ONCE, set the period to 0.

### Fixed Level

By using the option `level: <some_integer>`, you can create an item that triggers at one specific level only. This can be used for more meticulous exp tables, or simply for unique rewards like unlocking a skill, a waypoint, etc.

### Fail Reduction

If the player is unlucky and doesn't claim one of the items, the last option (`fail-reduction`) comes handy as it reduces the risk of further bad luck. Let's see how it works with an example: let's say an item claim chance is set to 60% and the fail reduction percentage is set to 50%. Setting it to 50% means that every levelup that fails at claiming the item will halve the remaining chance of not claiming it again. The successive claiming chances are then 60%, 80%, 90%, 95%, 97.5% (every time the distance to 100% gets halved).

_For those of you familiar with mathematics the successive chances of failing describe a geometrical sequence_

The `triggers` option is where you define what happens when that item is claimed. For maximum configurability, this is a list of [triggers](Triggers)... The triggers you will most often use are the `experience` and `command` triggers, exp to give experience to your main class, and commands to give rewards from other plugins (if required).