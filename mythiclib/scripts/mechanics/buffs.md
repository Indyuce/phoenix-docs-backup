# 💖 Buffs & Stats

## Add Temporary Stats

This adds a stat to the player. You can use all the stats within MMOCore and MMOItems. It will be removed when the server restarts.

For temporary stat buffs/debuffs, you can add a duration using the `lifetime` parameter (in ticks). Set `relative` to ``true`` and the buff will grant 10% Atk Damage instead of a flat +10 Atk Damage.

The `key` parameter is optional. It's the key you need to provide to remove your modifier later on if you need. There can be multiple stats using the same key, and using the `remove_stat` mechanic with that key will remove all of them.

Set `unique` to `true` if you want only one modifier with the same key to be active at a time. **If a new modifier is added with the same key, it will replace the previous one.** This is useful for buffs that you want to refresh periodically.

```yml
script_give_stat:
  mechanics:
  - 'add_stat{amount="10 + <modifier.extra>";time="20 *  (1 + <modifier.extra_time> )";stat=ATTACK_DAMAGE;key=my_custom_skill;relative=false;target=caster;unique=false}'
```

## Remove Temporary Stats

The following mechanic removes all stat modifiers with the associated `key`. It does not matter if the stat modifiers are temporary or permanent.
```yml
script_rem_stat:
  mechanics:
  - 'remove_stat{stat=ATTACK_DAMAGE;key=my_custom_skill;target=caster}'
```

## Heal target

`reason` (why the target is being healed) is optional (`CUSTOM` by default). It's better to indicate it so that other plugins know the healing source. Available sources [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/event/entity/EntityRegainHealthEvent.RegainReason.html).
```yml
script_health_target:
  mechanics:
  - 'heal{amount="10 + <caster.health> / 50";reason=CUSTOM;target=caster}'
```

## Give food to target

Highest food level is 20. A player's food level is always an integer (unlike health). This mechanic **SETS** the player's food level.
```yml
give_food_script:
  mechanics:
  - 'feed{amount="10 + 8 / 2";target=caster}'
```

## Restore saturation of target

This mechanic **SETS** the target's saturation level.

```yml
set_sat_level:
  mechanics:
  - 'saturate{amount="10 + 1";target=caster}'
```

