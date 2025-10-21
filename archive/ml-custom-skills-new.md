---
order: 1000
---

::: warning
Don't mind this page, it's for an upcoming feature
:::

# Custom Skill Config

```yml

FIREBOLT:
  hardcoded-id: FIREBOLT
  name: Firebolt
  lore:
  - 'You conjure a ball of flames'
  - 'and hurl it at your target'
  - ''
  - '&e{cooldown}s Cooldown'
  - '&9Costs {mana} {mana_name}'
  material: BOOK

  categories: [ 'fire', 'projectile' ]

  # Damage types dealt
  damage-types: [ MAGIC, FIRE, PROJECTILE ]

  default-item-parameters:
    damage: 4
    ignite: 5

  parameters:
    timer: 0
    delay: 0

    damage: '3 + {skill_level} * 1'
    ignite:
      base: 2
      per-level: 1
    mana:
      base: 2
      per-level: 1
    stamina:
      base: 0
      per-level: 0
      min: 0
      max: 0
    cooldown:
      base: 7
      per-level: 1

```