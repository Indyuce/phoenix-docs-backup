**Make sure you read [this paragraph](Item Creation#how-items-work-very-important) first. The MMOItems item generation system is pretty complex and needs some time to be fully understood.**

Randomly generated items can have **numeric stats**, like attack damage, attack speed, crit strike chance, but you can also add more **complex stats** to it, like abilities, or permanent potion effects, which power do also scale with the item level. These statistics are more complex and therefore a little harder to setup.

Remember any code snippet found in that page would go either in the `base` config section of an item gen template (which corresponds to the template base item data), or in the `stats` config section of an item gen modifier:
```
ITEM_TEMPLATE_EXAMPLE:
    base:
        material: IRON_SWORD
        # <======== either here
    modifiers:
        first-modifier:
            prefix: 'Modifier Prefix'
            stats:
                attack-damage: 3
                # <======= or here
```

## Abilities
Using the item generator, you can create items with special abilities which get stronger the higher the item level. Precisely, abilities have modifiers (how much damage it deals, how long a potion effect lasts..) which can scale on the item level. Use this format to add an ability to an item gen template/item gen modifier:
```
ability:
    first-ability-id:
        type: burn
        mode: on_hit

        # First ability modifier
        cooldown:
            base: 6
            spread: .1
            max-spread: .3

        # Second ability modifier
        duration:
            base: 3
            scale: .2
    second-ability:
        type: life-ender
        mode: right-click
        damage:
            base: 10
            scale: 3
    third-ability:
        type: blizzard
        mode: left-click
        damage:
            base: 5
        cooldown:
            base: 7
            scale: 2
 
```
You may notice that the format is the exact same as if you wanted to add an ability to a normal (not randomly generated) mmoitem. The only thing that changes is how you define the ability modifiers, because they are the only values which can really scale on the item level. The formulas used to define an ability modifier are the same as the formulas used with
[numeric stats](Item-Stats-and-Options#numeric-stats).

In this example, the on-hit burn ability has a 6s cooldown however that values fluctuates +/-10% in average with a maximum relative offset of 10%. The burn lasts for 6 seconds but that duration is increased by 0.2 second for every item level.

Note that if you want to specify an ability modifier but do not want it to scale, you must still specify a base, and set the scale and/or max-spread to 0 or remove them completely. See the above example titled `third-ability`. In this example, damage will be 5 on every item generated using the blizzard ability. However, cooldown will still scale as specified.


## Potion effects obtained when eating a consumable
Remember a potion effect is defined by three options: the potion effect type, a duration and a potion level.
```
effects:
    speed:
        level:
            base: 1
            scale: 1
        duration:
            base: 10
            scale: 3
```
Notice how you start to see a repeating pattern with the `base/scale/spread/maxspread` based config sections which seem to be literally everywhere when dealing with randomly generated items. Like any other numeric values, the potion duration and level can scale on the item level.

Since these are numeric stats, you can also use this format if you want for instance the level to be the same everytime:
```
effects:
    speed:
        level: 1
        duration: ...
```
This is the exact same as the following
```
effects:
    speed:
        level:
            base: 1
            scale: 0
            spread: 0
            max-spread: 0
        duration: ...
```
You can view the Minecraft effect list [here](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html).

## Permanent Potion Effects
It's literally the same as with consumable potion effects (see above), but since these potion effects are supposed to be permanently given to the player when a specific item is held, you **do not have to specify the effect duration**. The `level` config section is also gone because it's cleaner without it.
```
perm-effect:
    speed:
        base: 1
        scale: 1
    # That format works too
    haste: 3
```

## Enchantments
An enchantment is defined by an enchant type and a level. Use this format:
```
enchants:
    efficiency:
        base: 1
        # There is no Efficiency 1.3, but that means that every
        # 10 levels, the item will have an extra efficiency
        # enchant level! This can also be used with potion effect levels.
        scale: .1
    # That format still works because an enchant level is a numeric value
    sharpness: 10
```

## Item Elemental Stats
```
element:
    fire:
        defense: 
            base: 10
            scale: 3
        # That format still works!
        damage: 10
    water:
        defense: 50
```

## Consumable Restore Power
Restore power defines how much health, food and saturation a consumable restores when used.
```
restore:
    health:
        base: 3
        scale: 2
        spread: .3
        max-spread: .5
    # You could use a complex formula for food, or just use this format
    food: 5
    saturation: 3
```