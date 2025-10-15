---
title: 'Conditions: Generic'
---
### Boolean check
Use this condition to perform boolean algebra calculations. You can use placeholders from PAPI returning `true` or `false` as well as operators (negation !,or `||`, and `&&`) and MythicLib will parse and compute the result of your boolean formula. You can also compare numbers into your formulas to make any type of conditions relying on math.

These formulas are parsed using a JavaScript interpreter.

```
example_condition:
    type: boolean
    formula: "%mmocore_in_combat% || %mmocore_in_combat%"

example_condition2:
    type: boolean
    formula: '(<caster.health> <= 10 && <caster.health> > 5) || (!%mmocore_in_combat%)'

```

### String match
Use this condition to check if two strings match exactly.

This checks if the player is in a certain world:
```
example_condition:
    type: string_equals
    first: '<target.location.world.name>'
    second: 'world'
```

### Check if a number if within certain bounds (deprecated)
Use this condition to check, for instance, if a player's X coordinate is between some two numbers.

In the following example, the condition will be met if the caster's X coordinate is within 120 (included) and 140 (excluded).
```
example_condition:
    type: in_between
    first: '120'
    second: '<caster.location.x>'
    third: '140'
```

It is deprecated because it is now easier to do this:
```
example_condition:
    type: boolean
    formula: "<caster.location.x> > 120 && <caster.location.x> < 140"
```

### Compare two numbers (deprecated)
Use this condition to compare two numbers. You can check if the first number is (strictly) greater than/(strictly) lower than/or equal to the second number. Comparator names are `equals`, `lower`, `greater`, `strictly_lower`, `strictly_greater`.

The following condition will be met if the player's health is lower than 10hp.
```
example_condition:
    type: compare
    first: '<caster.health>'
    second: '10'
    comparator: LOWER_THAN
```

It is deprecated because it is now easier to do this:
```
example_condition:
    type: boolean
    formula: "<caster.health> < 10"
```