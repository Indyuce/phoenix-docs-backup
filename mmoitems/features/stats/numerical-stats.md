---
order: 2
---

# Numerical Stats

By _numerical stat_ we refer to 80% item stats:

## Overview

Most numerical stats (Attack Damage/Crit Chance/PvE Damage/...) or even more specific item options (ability modifiers, potion effect duration/level, enchant level) all feature formulas for numerical inputs. These formulas are adapted to easily provide realistic stat values in a RPG server scenario, though you also have options to make numerical inputs much much easier to configure.

Numerical inputs (numerical stats, ability modifiers...) can scale with the item level. The item level is a constant picked "randomly\_"\_ when generating an item. As a general rule, the higher the item level, the better the stats.

The formula used is the following:

```yaml
attack-damage: # Could be any stat
    base: 10
    scale: 2
```

`base` is the stat value that corresponds to a lvl 0 item. `scale` is the extra value the stat gets for every additional extra level. Using the formula given above, if the item level is 6, the stat value will be `10 + (2 * 6) = 22`. The general formula is therefore `stat_value = base + item_level * scale`_._

If you don't want your stat to scale on the item level, either set the scale parameter to 0, or use the following format :

```yaml
attack-damage: 10
```

## Adding randomness & realism to numerical stats

In RPG games, items you drop never have flat statistics that only depend on level: they have an extra randomness factor, which makes some items good, because of their overall slightly higher stats, and others bad because of their overall lower stats. MMOItems has a similar feature for numeric item stats.

### Specify a range for numerical stats

By using the following format, the stat value will be picked randomly within given lower and upper bounds.

```yaml
attack-damage:
    min: 10
    max: 20
```

This is the easy way of doing random stat values. If you don't want to mess too much with your stat values, just go for that. If you wanna add a deeper RPG touch to your server though, you can go for an option that is more realistic (same formulas as those used in RPG games) yet a little more difficult to setup.

### Use a normal distribution

A normal distribution is a distribution of variables that you can find literally everywhere in maths, physics, nature etc... This is the one we'll be using for the stat values. Let's check out the format first, then fully break it down.

```yaml
attack-damage:   # Unchanged
    base: 10     # Unchanged
    scale: 2     # Unchanged
    spread: .1
    max-spread: .3
```

First, remember that we want the stat value to be on average `base + item_level * scale` because that would be the stat value if there were no randomness. When "applying" a normal distribution to the stat values, the `spread` parameter is the average difference between a randomly generated stat value and the average value. The higher the spread, the more spread out the stat values will be. A lower spread will result in stat values that are more packed up around the average value.

You should use a spread of about 0.1, resulting in 70% values ranging from -10% to +10%, and 95% values ranging from -20% to +20%.

The `max-spread` is the maximum difference to the average value. You should set this parameter to around 30% to 50%, this way the normal distribution doesn't generate stat values that are over-powered. With such distribution remains a small risk of generating a stat value that is 10x the average value, which we don't want to happen for gameplay fairness.

You can also add constant lower/upper bounds to this gaussian-distribution-based numerical formula, using the following format (although this has limited utility when paired with stat scaling):

```yaml
attack-damage:     # Unchanged
    base: 10       # Unchanged
    scale: 2       # Unchanged
    spread: .1     # Unchanged
    max-spread: .3 # Unchanged
    min: 10
    max: 20
```