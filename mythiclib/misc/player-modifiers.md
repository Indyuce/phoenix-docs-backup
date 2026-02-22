---
order: 7
---

# 📌 Player Modifiers

::: warning
This feature is not available yet.
:::

## Overview
A player modifier can be any type of passive behaviour that modifies your player to make it stronger or weaker. Stat modifiers, skills, permanent potion effects are all considered player modifiers and can granted to players using items, full item set bonuses, MMOCore parties, MMOCore player classes...

| Player Modifier      | Description                               | Identifier      |
|----------------------|-------------------------------------------|-----------------|
| Stat modifier        | Modifies a player stat value              | `stat`          |
| Attribute modifier   | Modifies the value of a MMOCore attribute | `attribute`     |
| Skill                | Gives the player some triggerable skill   | `skill`         |
| Potion Effect        | A permanent potion effect like Speed II   | `potion`        |
| Particle Effect      | A permanent particle effect               | `particle`      |

When configurating MMOItems or MMOCore you will sometimes be asked to define player modifiers in specific scenarii, like when creating item sets in MMOItems and defining what modifiers to give the player when wearing 3 items from the same set.

## Stat Modifiers

When applied onto a player, a stat modifier increases the value of a player stat by a certain amount. It can be either a flat stat modifier (+10 Atk Dmg) or a multiplicative modifier (+10% Atk Dmg) which scales on the initial player's stat value.

```yml
modifierId:
    type: stat # This indicates the modifier is a stat modifier
    stat: ATTACK_DAMAGE
    value: 10
    multiplicative: false
    key: mmocoreParty
```

## Skills

Skills are a special type of player modifiers. Check [this page](Custom Skills) out for more info about MythicLib skills.

```yml
modifierId:
    type: item_skill # This indicates the modifier is an item skill
    skill: FIREBOLT
    trigger: RIGHT_CLICK    
    modifiers:
        damage: 10
        mana: 3
```