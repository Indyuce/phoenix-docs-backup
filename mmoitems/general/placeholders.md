---
order: 3
---

# 🏷️ Placeholders

All placeholders automatically register upon plugin load, and require
**PlaceholderAPI** to work. You do not need to run any commands to
initialize the placeholders. Keep in mind you can access PAPI
placeholders from MVdWPlaceholderAPI using
`{placeholderapi_mmoitems_...}`.

If you're looking for a placeholder and you can't see it here, do check [**MYTHICLIB PLACEHOLDERS**](https://gitlab.com/phoenix-dvpmt/mythiclib/-/wikis/Placeholders) as well!

### Stats

| **Placeholder**                   | **Description**                                |
|-------------------------------------------------|----------------------------------------------------------|
| `%mmoitems_stat_<stat name>%` | Returns the formatted player [stat](Item-Stats-and-Options) value |
| `%mmoitems_stat_<element name>_<damage/damage_percent/weakness/defense/defense-percent>%` | Returns the elemental stats |

### Types
| **Placeholder**                   | **Description**                                |
|--------------------------------------------|--------------------------------------|
| `%mmoitems_type_<item type>_name%`        | Returns the name of the specified [item type](Item-Types).      |
| `%mmoitems_type_<item type>_total%`       | Returns the total amount of items in the specified [item type](Item-Types).     |

### Durability

| **Placeholder**                   | **Description**                                |
|--------------------------------------------|--------------------------------------|
| `%mmoitems_durability%`      | Returns the durability left of the current item  |
| `%mmoitems_durability_max%`      | Returns the max durability of the current item  |
| `%mmoitems_durability_ratio%`      | Returns the durability of the current item as a percentage  |
| `%mmoitems_durability_bar_square%`      | Returns the durability of the current item as a bar (Squares) |
| `%mmoitems_durability_bar_diamond%`      | Returns the durability of the current item as a bar (Diamonds) |
| `%mmoitems_durability_bar_thin%`      | Returns the durability of the current item as a bar (Thin) |

([More information on Durability](Custom Durability))

### Misc

| **Placeholder**                   | **Description**                                |
|-----------------------------------|------------------------------------------------|
| `%mmoitems_tier_<item tier>%`            | Returns the name of the given tier     |
| `%mmoitems_ability_cd_<ability name>%`            | Returns the current cooldown of the given ability     |