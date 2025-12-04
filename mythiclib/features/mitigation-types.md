---
order: 4
---

# 🛡️ Damage Mitigation

_Damage Mitigation_ refers to the various ways a player can reduce or avoid incoming damage from attacks. While MythicLib provides several built-in mitigation types (_Block_, _Dodge_, and _Parry_), you can also create custom mitigation types to suit your server's needs.

## Built-in Mitigation Types

### Blocking

When blocking a melee or projectile attack, a player reduces damage taken by a significant amount. Both the block chance and block power (percentage of damage you are blocking) can be increased by items. Blocking power has a default value and a cap, meaning that if a player has no item giving him extra block power, he will block at least 20% of the damage taken. Blocking power can't exceed 75%.
The chance of blocking an attack is determined by the _Block Rating_ stat.

```yml
STEEL_BREASTPLATE:
  material: IRON_CHESTPLATE
  block-power: 10
  block-rating: 5
```

### Dodging

When dodging a melee or projectile attack, a player entirely **negates** damage taken and performs a quick dash backwards, allowing him to escape from the fight. The chance of dodging an attack is capped at 80%.

```yml
SWIFT_LEATHER_BOOTS:
  material: LEATHER_BOOTS
  dodge-rating: 10
```

### Parrying

Just like dodging, parrying entirely negates attack damage and knocks the attacker back.\
The knockback force can be edited in the main MythicLib config file.
```yml
DWARVEN_SHIELD:
  material: SHIELD
  parry-rating: 10
```

### Mitigation Cooldown Reduction

Every mitigation stat also features a cooldown reduction stat. By default, a player cannot dodge, parry or block more than one attack every few seconds. These cooldown stats lower that delay, which can be really useful if the player is running low on health.

```yml
ROGUE_AMULET:
  material: RED_DYE
  dodge-cooldown-reduction: 40
```

## Custom Mitigation Types

You can create your own custom mitigation types by adding new sections to the `MythicLib/mitigation_types.yml` file. Each section should follow the same structure as the built-in mitigation types. The following section goes over the different parameters available for mitigation types, using _Blocking_ as an example.

While you can certainly recreate similar _Mitigation Types_ using other plugins or scripting solutions, MythicLib aims to provide an easy-to-use framework finetuned to RPG server use cases.

## An Example

```yml
block:

  # For backwards compatibility only.
  # If none of your plugins use the old MythicLib mitigation
  # events, you can safely remove/comment out this option.
  legacy: block

  # Formula for cooldown between two consecutive blocks (in seconds)
  # To disable cooldown, delete this line, or comment it out
  # Note that, by default, cooldown reduction is capped at 80% (see stats.yml)
  cooldown: '3 * (1 - <stat.block_cooldown_reduction> / 100)'

  # Chance to successfully block an attack
  # This formula should return a value between 0 and 1 (0 being 0% chance, 1 being 100% chance)
  # Note that, by default, block rating is capped at 80% (see stats.yml)
  roll: '<stat.block_rating> / 100'

  # Script/skill ran on damage
  on_damage: mitigation_on_block
```

### Cooldown

The option `cooldown` indicates that such mitigation type has a cooldown. It cannot occur more frequently than once every X seconds, where X is the value returned by the formula. The default formula for _Blocking_ is `3 * (1 - <stat.block_cooldown_reduction> / 100)`, meaning that the base cooldown is 3 seconds, but it can be reduced by the player's _Block Cooldown Reduction_ stat.

### Roll

The option `roll` is a formula that returns the chance of successfully performing the mitigation. The formula should return a value between 0 and 1, where 0 means 0% chance and 1 means 100% chance. In the case of _Blocking_, the default formula is `<stat.block_rating> / 100`, meaning that if the player has 25% _Block Rating_, they have a 25% chance to block each incoming attack.

### Pre-Damage Script

The script `pre_damage` is executed before the mitigation is rolled for. It can be used to set up any necessary variables or conditions for the mitigation. In the case of _Blocking_, there is no pre-damage script by default, but you can add one if needed using the following syntax:

```yml
my_mitigation_type:
  pre_damage: my_custom_pre_damage_script
```

::: info
Note that all built-in scripts used by mitigation types are all located in the `MythicLib/script/mitigation_types` config file. You can view and edit them as you wish.
:::

### On-Damage Script

Last but not least, the script `on_damage` is executed when the mitigation successfully triggers. This script only executes if the following conditions are met:
- the mitigation is not on cooldown,
- the mitigation roll was successful,
- all conditions in the pre-damage script (if any) were met,
- the `DamageMitigationEvent` Bukkit event was not cancelled by another plugin.

For _Blocking_, the default on-damage script is `mitigation_on_block`, which reduces the incoming damage by a percentage based on the player's _Block Power_ stat.

```yml
mitigation_on_block:
  mechanics:

    # First, compute block coefficient and reduce damage
    - 'set_double{variable="block_coef";value="<stat.block_power>/100"}'
    - 'multiply_damage{amount="1 - <block_coef>"}'

    # Send message and play sound effect
    - 'set_double{variable="damaged_blocked";value="<attack.damage> * <block_coef>"}'
    - 'action_bar{m="&cYou blocked <damaged_blocked> damage!";target=caster;priority=31}'
    - 'play_sound{sound=ENTITY_ZOMBIE_ATTACK_IRON_DOOR;volume=1;pitch=2}'
    - 'set_double{variable=max_angle;value=120}'
    - 'script{name=mitigation_block_particle_effect}'

mitigation_block_particle_effect:
  # Sound and particle effect logic
  # [...]
```