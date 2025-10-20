# 💖 Buffs & Stats

## Add temporary stats

This adds a stat to the player. You can use all the stats within MMOCore and MMOItems. It will be removed when the server restarts. The `lifetime` option is optional (in ticks), it's used to add temporary buffs. Set `relative` to true and this will grant 10% Atk damage instead of a flat +10 Atk damage.

The `key` option is very necessary. It's the key you need to provide to remove your modifier later on if you need. There can't be two stat modifiers with the same `stat` and `key` option pair.

```yml
script_give_stat:
  mechanics:
  - 'add_stat{amount="10 + <modifier.extra>";time="20 + <modifier.extra_time> * 20";stat=ATTACK_DAMAGE;key=my_custom_skill;relative=false;target=caster}'
```

## Remove temporary stats

The following mechanic removes the stat modifier registered above, whether or not it's temporary.
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

