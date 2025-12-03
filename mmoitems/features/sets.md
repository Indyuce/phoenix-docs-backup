# 🛡️ Item Sets

Items sets allow you to link multiple items together to make them stronger when worn at the same time. Item sets give extra stats to the player if he wears enough items from the same item set. The config file is pretty self explanatory; here is a config snippet.
```yml
ARCANE:
  name: '&2Arcane Set'
  bonuses:
    '3':
      magic-damage: 20
    '4':
      max-mana: 30
      potion-speed: 1
  lore-tag:
  - '&7Arcane Set Bonus:'
  - '&8[3] +20% Magic Damage'
  - '&8[4] 30 Max Mana'
  - '&8[4] Permanent Speed I'
```

## Set Bonuses

Set bonuses can be displayed in the item lore using the _lore-tag_ option. You can really put anything in that list, but I like to precisely give the amount of additional stats the item gives. The bonuses section defines what bonuses the item set gives. The subsections with numbers correspond to the stats the item set grants for each amount of items the player wears.

Full set can grant stats, abilities, permanent potion effects, permissions as well as particle effects to the player.

## Permanent potion effects
Set bonuses can grant **permanent potion effects** to the player. You need to specify the potion effect name (names can be found [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html)) and the potion level which needs to be an integer. You need to use the following format: `potion-<potion-effect-name>: <permanent-level>`. Using the `potion-` prefix will indicate to MMOItems that you want to setup a permanent potion effect.
```yml
SPEED:
  name: '&2Speed Set'
  bonuses:
    '4':
      potion-speed: 1
      # ......
```

## Abilities
Last but not least, you may also setup **abilities** as full set bonuses. Pretty easy to setup since it's the same format as with item abilities. In the following example, any player who holds at least 2 items from the Hatred Set will be temporarily granted a Life Ender ability which will trigger when hitting any entity. The ability has a 30sec cooldown. Just make sure you are using the `ability-` prefix which indicates to MMOItems that you'd like to setup a permanent ability.
```yml
HATRED:
  name: '&cHatred Set'
  bonuses:
    '2':
      ability-1:
        type: LIFE_ENDER
        cooldown: 30
        mode: ON_HIT
      #......
```

## Particle Effects
The prefix for particle effects is `particle-`. You can put whatever you want after that prefix.
```yml
HATRED:
  name: '&cHatred Set'
  bonuses:
    '2':
        particle-whatever_you_want_here:
          type: GALAXY
          particle: FLAME
          # Modifiers which are specific to the particle type (GALAXY in that case)
          height: 1
          speed: 1
        #......
```
You can find more information on MMOItems particle effects [here](stats/stats.md#item-particles).

## Permissions

You can provide a list of permissions that will be granted to the player once he reaches a specific number of items in the set.

```yml
HATRED:
  name: '&cHatred Set'
  bonuses:
    '2':
      granted-permissions:
        - 'hatred.fullset'
        - 'whatever.permission'
      #......
```