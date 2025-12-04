# Location Targeters

::: warning
Under Construction
:::

Location targeters are used to specify locations where you want to execute a mechanic or script. Location targeters may return multiple locations, in which case the mechanic/script will be executed multiple times, once for each location.

## Caster

Use this to target the script caster's location. The optional `position` parameter allows you to access a precise location on the player's body, from lowest to highest: `FEET`, `BODY` (half way up), `EYES` (at eyes height), `TOP`. It is set to `BODY` by default.

```yml
location_targeter_caster_1:
  public: true
  mechanics:
  - 'particle{particle=FLAME;target=caster;amount=100;x=0.5;y=1;z=0.5;speed=0.1}'

location_targeter_caster_2:
  public: true
  mechanics:
  - 'particle{particle=FLAME;target={type=caster;position=TOP};amount=100;x=0.1;y=0.1;z=0.1;speed=0.05}'
```

## Circle

Use it to run a script multiple times with a set distance away from a center location. `amount` is the number of points samples on the circle. The higher, the "smoother" the circle will appear if you spawn particles for instance. `radius` is the radius of the circle.

Setting the `source` parameter to `true` will use the script source location as center location. If set to `false`, MythicLib will first try to use the script target location as center location.

```yml
location_targeter_circle:
  public: true
  mechanics:
  - 'particle{particle=FLAME;target={type=circle;radius=3;amount=30;source=false}}'
```

## Custom position

Using this targeter you can input the position X, Y and Z manually. Setting `relative` to `true` will **add** to the location you input the target script location, or caster location if `source` is set to `false`. For instance, the following example returns one block above the script source location.

```yml
location_targeter_custom:
  public: true
  mechanics:
  - 'particle{particle=FLAME;target={type=custom;x=1;y=1;z=1;source=true;relative=true};amount=100;x=0.1;y=0.1;z=0.1;speed=0.05}'
```

## Source location

Use it to target the script source location. It is usually the location of the player who ran the script initially.

```yml
location_targeter_source:
  public: true
  mechanics:
  - 'particle{particle=LAVA;target=source_location;amount=10;x=0.1;y=0.1;z=0.1}'
```

## Target entity location

The location of the script target entity. The optional `position` parameter allows you to access a precise location on the player's body, from lowest to highest: `FEET`, `BODY` (half way up), `EYES` (at eyes height), `TOP`. It is set to `BODY` by default.

```yml
location_targeter_target:
  public: true
  mechanics:
  - 'particle{particle=LAVA;target={type=target;position=BODY};amount=10;x=0.1;y=0.1;z=0.1;speed=0.05}'
```

## Target location

Targets the script target location.

```yml
location_targeter_target_loc:
  public: true
  mechanics:
  - 'particle{particle=LAVA;target=target_location;amount=10;x=0.1;y=0.1;z=0.1}'
```

## Location variable

If a location/position happens to be stored as a variable in a script, you can access it using this targeter. `name` is the name of the variable you want to use as target location.

```yml
location_targeter_variable:
  public: true
  mechanics:
  - 'copy_vector{value="caster.location";variable=l}' # copy caster location to variable "l"
  - 'set_x{variable=l;x=" <l.x> + 5"}' # add 1 to the X of the location stored in variable "l"
  - 'particle{particle=LAVA;target={type=variable;name=l};amount=10;x=0.1;y=0.1;z=0.1}'
```