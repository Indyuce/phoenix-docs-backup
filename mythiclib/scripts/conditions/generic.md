---
title: 'Conditions: Generic'
---

# Generic

## Expression check

Use this condition to perform arithmetic and boolean calculations. You can use placeholders from PAPI returning `true` or `false` as well as operators (negation !,or `||`, and `&&`) and MythicLib will parse and compute the result of your boolean formula. You can also compare numbers into your formulas to make any type of conditions relying on math.

These formulas are parsed using a JavaScript interpreter.

```yml
condition_generic_1:
  conditions:
  - 'boolean{formula=" (%mmocore_in_combat% || %mmocore_in_combat%) && true"}'
  mechanics:
  - 'message{format="You are in combat!"}'

condition_generic_2:
  conditions:
  - 'boolean{formula="(<caster.health> <= 10 && <caster.health> > 5) || (!%mmocore_in_combat%)"}'
  mechanics:
  - 'message{format="Condition met!"}'

```

## String match
Use this condition to check if two strings match exactly.

This checks if the player is in a certain world:
```yml
condition_string:
  conditions:
  - 'string_equals{first="<target.location.world.name>";second="spawn"}'
  mechanics:
  - 'message{format="You are in the spawn world!"}'
```
