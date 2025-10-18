---
order: 3
---

# Alchemy

Enchanting is a specific type of profession in MMOCore. It allows players to get experience and level up their enchant profession by enchanting items at the vanilla enchantment tables. The experience gained when enchanting an items depends directly on the new enchants your item obtains, and on the levels of the new enchants.

## Enchanting Experience
Some enchants are harder to obtain that others and therefore should give more exp than others. Every enchant has a set amount of EXP **per enchant level** that will be given to the player whenever he rolls that enchant. Therefore, the experience earned is the weighted sum of all the exp earned by every single enchant, weighted by the enchant level.

## enchanting.yml
```
base-enchant-exp:
    fire_protection: 10
    sharpness: 10
    flame: 10
    aqua_affinity: 10
    punch: 10
    loyalty: 10
    depth_strider: 10
    vanishing_curse: 10
    unbreaking: 10
    knockback: 10
    luck_of_the_sea: 10
    binding_curse: 10
    fortune: 30
    protection: 10
    efficiency: 40
    mending: 10
    frost_walker: 10
    lure: 10
    looting: 10
    piercing: 10
    blast_protection: 10
    smite: 10
    multishot: 10
    fire_aspect: 10
    channeling: 10
    sweeping: 10
    thorns: 10
    bane_of_arthropods: 10
    respiration: 10
    riptide: 10
    silk_touch: 50
    quick_charge: 10
    projectile_protection: 10
    impaling: 10
    feather_falling: 10
    power: 10
    infinity: 10
```

## Example
A player enchants a diamond sword with _Efficiency IV_, _Unbreaking III_ and _Silk Touch_. Therefore the experience given to the player is: `total = sum of all (<enchant exp> * <enchant level>)` i.e
`total = 4 * 40 + 3 * 10 + 1 * 50 = 160 + 30 + 50 = 240 Enchanting EXP`