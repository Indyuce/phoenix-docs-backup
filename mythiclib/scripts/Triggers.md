When using custom scripts in MMOItems and MMOCore you might sometimes specify when a specific script should be executed: when damaging an entity, when being damaged, when crouching etc. This is done using trigger types.

You can find the full list of available trigger types [here](Trigger Types).

### When a script is triggered

Some trigger types provide special properties to the script they trigger. For instance, when using the `ATTACK` trigger type, the `<target>` variable can be accessed to work with the attack target. `<attack.damage>` returns the attack damage. More precisely, some internal variables only exist when specific trigger types are used.

Trigger types featuring entities/projectiles like `ATTACK`, `DAMAGED`, `DAMAGED_BY_ENTITY`, `KILL_ENTITY`, `SHOOT_TRIDENT`, `ARROW_TICK` etc. allow the user to use the `<target>` internal variable to access the target entity. This also unlocks the `target` entity targeter as well as the `target_location` location targeter for instance.

Trigger types featuring positions like `TRIDENT_LAND` or `ARROW_HIT` unlock the `target_location` location targeter as well as the `<target_location>` internal variable for example.

Some triggers like `TIMER` or `RIGHT_CLICK` don't unlock any internal variable.

`ATTACK` is the only trigger type which unlocks the `<attack>` internal variable as well as special mechanics (`multiply_damage`) or conditions (`has_damage_type`).