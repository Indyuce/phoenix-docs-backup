---
order: 24
---

# 🪽 Elytra Slot

This is a special type of slot. Players can only equip elytras inside such slots. When elytras are equipped in this slot, players can the ability to switch to elytras when falling from high enough.

## How to use

Equip an Elytra in one of these slots. If the player is falling for more than 4 blocks, and if they do not have the _Slow Falling_ potion effect, elytras will automatically be equipped to the player's chestplate slot. The player can then use their elytra for the remaining of the flight. When the player finally touches the ground, elytras are placed back in the custom inventory and the previous chestplate item is restored.

## Slot Example

You will find the following syntax snippet in the default `inventory/default_mmoinventory.yml` config file.
```yml
slots:
  #.....
  ELYTRA:
  type: elytra
  material: GOLD_NUGGET
  custom_model_data_string: "elytra"
  name: "&6Elytra Slot"
  restrictions:
    - 'material{materials="ELYTRA"}'
  slot: 14
  lore:
    - 'Only &bElytras&7 are allowed here.'
    - '&bDeploy automatically&7 when falling.'
    - 'Drag & drop an item to equip it.'
```

## How to disable

Remove or uncomment any slot which uses the slot type `elytra` in all inventories.

## Main Config

Inside `config.yml`, you can change the minimum fall distance required to automatically equip elytras.

```yml
elytra_deployment:

  # If "Slow falling" is detected on the player, fall time
  # is reset, temporarily preventing elytras from deploying
  # until the player hits the ground, or the effect wears off.
  skip_if_slow_falling: true

  # Fall distance threshold (in blocks) after which
  # elytras automatically deploy.
  fall_distance_threshold: 4
```