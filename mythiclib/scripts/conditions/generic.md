---
title: 'Generic'
---

# Generic

## Expression Check

Use this condition to perform arithmetic and boolean calculations. You can use placeholders from PAPI returning `true` or `false` as well as logical operators (negation `!`, or `||`, and `&&`) and MythicLib will parse and compute the result of your boolean formula.

This can be used to multiple compare numbers simultaneously, for instance using `(a < b) && (c >= d)`. The brackets are not mandatory but can help with readability. You can add as many spaces as you want between the different parts of the formula for better clarity.

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| formula | form, f, expression, expr, e      | The boolean formula to evaluate. | - |

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

## Has Variable

Checks if a variable exists. This can also be used against a reserved variable like `target` or `target_location`.

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| variable | var, v, name, n      | Name of the variable to check for. | - |

```yml
condition_has_variable:
  conditions:
  - 'has_variable{var=target_location}'
  mechanics:
  - 'message{format="The variable target_location exists!"}'
```

## String Contain

Use this condition to check if some string contains another string.

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| within | in      | The string to search in. | - |
| search | lookfor, look, lf | The string to search for. | - |
| ignore_case | ic      | Whether to ignore case when comparing the strings. | false |

This example script checks if the target entity is either a Zombie or a Skeleton.

```yml
condition_string_contain:
  conditions:
  - 'string_contains{in="ZOMBIE,SKELETON";look="<target.type>"}'
  mechanics:
  - 'message{format="Target is either a Zombie or a Skeleton!"}'
```

## String Match

Use this condition to check if two strings match exactly.

| Parameter | Alias  | Description | Default |
|-----------|--------|-------------|---------|
| first | one, left, lhs      | The first string. | - |
| second | two, right, rhs | The second string. | - |
| ignore_case | ic      | Whether to ignore case when comparing the strings. | false |

This checks if the player is in a certain world:

```yml
condition_string_eq:
  conditions:
  - 'string_equals{first="<target.location.world.name>";second="spawn"}'
  mechanics:
  - 'message{format="You are in the spawn world!"}'
```
