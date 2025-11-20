**Please first learn about variables** [**here**](../variables.md). Since variables have scopes, everytime you are editing or initializing a variable, you must provide the variable scope using the `scope` option. By default it's always set to `SKILL`.

## Other variables

There is always one mechanic for both initializing and editing the current value of a variable.

### Initialize/edit a number with decimals (a double)

```
example_mechanic:
    type: set_double
    variable: variable_name
    scope: SKILL
    value: '<target.attribute.max_health> - <caster.attribute.max_health>'
```

### Initialize/edit an integer

The formula provided in the `value` option can return a double, tho since it is an integer variable, ML will round the returned number to the closest lower integer.

```
example_mechanic:
    type: set_integer
    variable: variable_name
    scope: SKILL
    value: '<target.attribute.max_health> - <caster.attribute.max_health>'
```

### Initialize/edit a string variable

This saves the script caster world name in a variable.

```
example_mechanic:
    type: set_string
    variable: variable_name
    scope: SKILL
    value: '<caster.location.world.name>'
```

### Initialize/edit a vector

```
example_mechanic:
    type: set_vector
    variable: variable_name
    scope: SKILL
    x: '10 + <caster.location.x>'
    y: '10 + <caster.location.y>'
    z: '10 + <caster.location.z>'
```

## Vector calculation mechanics

Locations, positions, vectors are treated the same way in MythicLib. The following mechanics have been implemented to make script creation a little easier: ML provides a small bundle of basic/more complex mechanics for vector calculation.

### Vector addition

Use this to add a vector (stored in a variable) to another vector (stored in another variable).

```
example_mechanic:
    type: add_vector
    variable: variable_name
    scope: SKILL
    added: added_vector_variable_name
```

You can also use this to add x,y,z coordinates separately to the existing vector variable:

```
example_mechanic:
    type: add_vector
    variable: variable_name
    scope: SKILL
    x: '10'
    y: '4'
    z: '-7'
```

### Copy/duplicate vector

Copies an existing vector (with name given by the `copied` option) into another variable (with name given by the `variable` option). The `scope` option corresponds to the scope of the new variable created.

```
example_mechanic:
    type: copy_vector
    variable: vector_variable_name
    scope: SKILL
    copied: copied_var_name
```

### Vector dot product

Computes the dot product of vectors `vec1` and `vec2` and saves it in a variable. The result is a decimal number (double).

```
example_mechanic:
    type: dot_product
    variable: saved_variable_name
    scope: SKILL
    vec1: first_vector_variable_name
    vec2: second_vector_variable_name
```

This is completely equivalent:
```
example_mechanic:
    type: set_double
    variable: variable_name
    scope: SKILL
    value: '<var.vec1.x> * <var.vec2.x> + <var.vec1.y> * <var.vec2.y> + <var.vec1.z> * <var.vec2.z>'
```

### Multiply vector by a constant

Multiplies the X, Y and Z coordinates of a vector by the same constant.

```
example_mechanic:
    type: multiply_vector
    variable: vector_variable_name
    scope: SKILL
    coef: '3.14159'
```

### Normalize a vector

This takes a vector and makes it of length 1 (essentially divide it by its own length) which is useful when working with vectors describing directions.

```
example_mechanic:
    type: normalize_vector
    variable: vector_variable_name
    scope: SKILL
```

### Set X/Y/Z coordinate of a vector

The mechanic names are `set_x`, `set_y` and `set_y`. The following mechanic sets the Y coordinate of vector in variable `knockback` to 0.

```
example_mechanic:
    type: set_y
    variable: knockback
    scope: SKILL
    z: 0
```

### Vector subtraction

Subtracts a vector from another. Use this to subtract a vector stored in a variable:

```
example_mechanic:
    type: subtract_vector
    variable: edited_var_name
    scope: SKILL
    subtracted: other_var_name
```

You can also subtract individually X, Y and Z coordinates, which has the same effect of adding the opposite coordinates.

```
example_mechanic:
    type: subtract_vector
    variable: edited_var_name
    scope: SKILL
    x: -4
    y: 0
    z: 10
```

## Complex vector mechanics

### Vector cross product

Computes the cross product of vectors `vec1` and `vec2` and saves it in a variable. The result is another vector.

```
example_mechanic:
    type: cross_product
    variable: saved_variable_name
    scope: SKILL
    vec1: first_vector_variable_name
    vec2: second_vector_variable_name
```

### Vector hadamard product

This multiplies the X, Y and Z coordinates of the two vectors separately and saves the result in a variable. The result is another vector.

```
example_mechanic:
    type: hadamard_product
    variable: saved_variable_name
    scope: SKILL
    vec1: first_vector_variable_name
    vec2: second_vector_variable_name
```