---
order: 10
---


# 🎒 Inventory

## Close Inventory

Use this mechanic to close the current player's inventory. This can be used inside any MMO plugin UI: MMOItems crafting stations, MMOProfiles profile selection, MMOCore skill tree UIs, etc...

```yml
script_close_inventory:
  mechanics:
    - 'close_inventory{}'
```

## Go Gack

Use this to have the player navigate to the last page visited. For instance, this can be used to go back from the _Class Confirmation UI_ to the _Class Selection UI_ in MMOCore for instance.

```yml
script_ui_go_back:
  mechanics:
    - 'go_back{}'
```