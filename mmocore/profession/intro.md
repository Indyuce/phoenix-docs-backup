---
order: -1
---

# Introduction

Although MMOCore features at the moment 7 default professions, you can create as many professions as you want to make your leveling system more interesting. Professions can have specific **[experience sources](Experience Sources)** i.e actions players can perform in order to get X exp in a specific profession.

Once players have earned enough experience in their profession, they not only level up their profession but also receive some class EXP which can level up their main level and give them skill points.

![TBz9e5B](uploads/51810e957ab276b52b39fda03789e2d0/TBz9e5B.gif)

## Example: Farming Profession
```
# Display options
name: Farming

# Must match an existing exp curve filename from the 'expcurves' folder
exp-curve: levels

# How to get exp in that profession
exp-sources:
- 'mineblock{type=CARROTS;amount=1-3;crop=true;player-placed:true}'
- 'mineblock{type=POTATOES;amount=1-3;crop=true;player-placed:true}'
- 'mineblock{type=WHEAT;amount=1-3;crop=true;player-placed:true}'

# The maximum profession level
max-level: 10

# See below for full explanation
exp-table: example_exp_table

# Experience given to the main level
# when leveling up this profession
experience:
    base: 10
    per-level: 2
```

All profession config files are saved in the `/MMOCore/profession` plugin folder. You may configure the profession display name, as well as the **main class experience** the player will earn whenever leveling this specific profession.

## Experience Curve
This determines how much EXP the player needs to reach the next profession level. More info on experience curves [over here](Experience Curves).

## Experience Tables
More about experiences tables [here](Experience tables)
## Experience sources
Experience sources define what actions the player have to do in order to earn exp in your profession. More info over that [wiki page](Experience Sources).