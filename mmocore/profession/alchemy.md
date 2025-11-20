---
order: 3
---

# 🍹 Alchemy

The default alchemy profession allows players to earn experience when brewing any type of potions: splash, lingering, upgraded vanilla potions. Here is the most important part of the alchemy profession config file.

```yml
exp-sources:
- 'brewpotion{effect=SPEED}'

# When brewing a potion, players earn Alchemy experience.
# Experience earned depends on the effect you give to your
# potion, if you upgrade/extend its duration, etc.
alchemy-experience:

    special:
        
        # When brewing a potion into a splash potion,
        # only 40% of the base EXP is earned.
        splash: 40
        
        # When brewing a potion into a splash potion,
        # only 40% of the base EXP is earned.
        lingering: 40
        
        # When extending a pot duration,
        # only 40% of base EXP is earned.
        extend: 40
        
        # When upgrading a potion level,
        # only 40% of base EXP is earned.
        upgrade: 40

    # Base EXP of potions
    effects:
        
        # Water bottles
        AWKWARD: 5
        MUNDANE: 5
        THICK: 5
        
        # Potion effects
        NIGHT_VISION: 10
        INVISIBILITY: 10
        JUMP: 10
        FIRE_RESISTANCE: 10
        SPEED: 10
        SLOWNESS: 10
    
        #....
```

As you can see, the only alchemy experience source is brewing (brewing stand). You may also specify what type of potions the player must brew in order to get experience in that specific profession using the `brewitem` **experience source**. If you want the player to earn EXP when only brewing speed and regen potions, use `'brewpotion{effect=SPEED,REGEN}'` (separate potion types using a comma).

The `alchemy-experience` config section dictates how much experience the player will get from brewing any potion. The experience a player gets from brewing **directly depends on the potion effect type**: rarer potions i.e potions which require rarer ingredients like ghast tears (over glistering melons) should grant more alchemy experience.\
On the other hand, mundane, thick and awkward potions should give less experience since players must brew them before brewing any other potion.

## Base EXP

Every potion type has a base EXP which the player earns when brewing 1, 2 or 3 potions (at the same time) of this type in a brewing stand, for example the player will earn 15EXP from brewing a fire resistance potion and 20EXP from brewing a jump potion _(with the default setup)_.

## Alchemy EXP Modifiers

When using **redstone to extend the effect duration**, the player will earn X% of the potion effect base experience e.g when extending a jump potion, the player will earn `40% * 20 = 5EXP`. This percentage can be setup with the `special.extend` option. When using **glowstone to upgrade the effect**, the player will also earn X% of the potion effect base experience. This percentage can be setup with the `special.upgrade` option.

When using **gunpowder to brew a splash potion** or **dragon breath to brew a lingering potion**, the player will earn X% of the potion effect base experience (percentages are configurable using `special.splash` and `special.lingering`).