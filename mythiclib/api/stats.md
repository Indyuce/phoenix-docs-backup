---
order: 1
---

# 📊 Player Stats

MythicLib stats API design is similar to the Spigot attribute modifiers API. Stat data from every numeric MMOItems/MMOCore stat is stored in a `StatMap` accessible using the following method.

```java
MMOPlayerData playerData = MMOPlayerData.get(/* player or UUID */);
StatMap statMap = playerData.getStatMap();
```

Using that class you can access instances of `StatInstance` which correspond to one specific stat.

## Stat Instances

Just like Spigot's attribute instances, stat instances feature a map that **stores stat modifiers**. There are two different types of stat modifiers:

- fixed stat modifiers, which add a fixed/flat amount (+10 Atk Damage)
- % stat modifiers, which multiply the total stat value by a certain constant (+10% Atk Damage)

The advantage of using attributes is that any plugin can add its own attributes, and MythicLib can easily gather all of them and calculate the total stat value based on these attributes. For instance, MMOCore uses attributes to handle experience party buffs:

```java
// Modifier that adds +10% exp gained
StatModifier experienceModifier = new StatModifier("myCustomPluginKey", "ADDITIONAL_EXPERIENCE", 10, ModifierType.FLAT);

// Register the modifier
experienceModifier.register(playerData);

// Access all currently registered modifiers this way
statMap.getInstance("ADDITIONAL_EXPERIENCE").getModifiers().forEach(mod -> /* code */);
```

Notice how any plugin can access all the modifiers created by all the plugins. That means you must make sure your plugin only manipulates the attributes you create which can be done by choosing a very specific **modifier key** like "mmocorePartyBuff" or "mmoitemsItemSetBonus".

## Adding a stat modifier

There are multiple ways of generating a stat modifier. The most exhaustive constructor is the following

```java
StatModifier(UUID, String, String, double, ModifierType, ModifierSource, EquipmentSlot)
```

The first parameter is the UUID. When not provided, a random UUID gets assigned to your new modifier. Every modifier is identified by a UUID. The second parameter, the **modifier key** can also be used to quickly identify the plugin which registered the modifier, but it's **NOT UNIQUE!!** The plugin key should be your plugin name, to make sure that there are no collisions with other systems or plugins. Again, this modifier key is **no longer unique** since MythicLib 1.6.2 builds.

The third parameter is the stat being modified. This can be `ATTACK_DAMAGE` or `SKILL_CRITICAL_STRIKE_CHANCE` for instance.

The **equipment slot** was implemented to keep track of where that modifier is coming from. It's mostly used by MMOItems and MMOInventory to apply the right stats from an item depending on where it's equipped in the player inventory.

The **modifier source** was implemented to differenciate stat modifiers given by melee and ranged weapons. This is also used by MI and MMOInventory to fix similar issues.

::: tip
Use `ModifierSource#OTHER` and `EquipmentSlot#OTHER` for general buffs, or if you're unsure about what to use.
:::

You can also use this simpler constructor if you don't need to specify the UUID, modifier source and equipment slot.

```java
StatModifier modifier = new StatModifier(String, String, double, ModifierType);
```

### Register the stat modifier

In order to register your stat modifier, you can use the following method.

```java
MMOPlayerData playerData = MMOPlayerData.get(/* player UUID */);
modifier.register(playerData);
```

You may also use this method which does exactly the same thing:

```java
StatModifier modifier = /* TODO */;
StatInstance instance = statMap.getInstance(modifier.getStat());
instance.addModifier(modifier);
```

## Temporary stat modifiers

Note that you can also add **temporary stat modifiers** using the following method. The long parameter corresponds to the duration of the modifier in ticks.

```java
new TemporaryStatModifier(String, String, double, ModifierType, EquipmentSlot, ModifierSource).register(MMOPlayerData, long);
```

## Remove a stat modifier

The following code uses the key we were talking about to remove all stat modifiers registered by a specific plugin, or which key starts with a specific prefix, etc.

```java
statInstance.removeIf(key -> key.startsWith("mmoitems"));
statInstance.removeIf("MyAwesomePlugin"::equals);
```

You can also pinpoint a specific modifier and remove it using its UUID.

```java
statInstance.removeModifier(/* modifier UUID */);
```

You can also unregister the stat modifier directly from the modifier instance. This does exactly the same thing as the previous method, and you do not need to provide the modifier UUID.

```java
modifier.unregister(playerData);
```

## Calculating player stats

The following code snippet shows how to calculate the total value of a stat.

```java
// calculate the player's crit strike chance
double critChance = statMap.getStat("CRITICAL_STRIKE_CHANCE");
```

Stat values depend on the player's action hand. Most of the time, they are interacting with their main hand (right hand), but sometimes they might be using their off hand (left hand) like when shooting a bow or throwing a snowball. In that case, MythicLib must ignore some stat modifiers depending on which hand is being used.

By default, MythicLib assumes the action hand is the right hand. If you need to compute a stat value with the left hand as action hand, you can use the following method:

```java
double attackSpeed = statMap.getInstance("ATTACK_SPEED").getTotal(EquipmentSlot.OFF_HAND);
```

MythicLib does fancy calculation to determine which modifiers to ignore, and which to keep, based on the equipment slot and modifier sources of the registered stat modifiers. All of this is already taken care of internally, so you don't have to worry about it!

## _Total_ vs _Final_ Stat Value

Vanilla attribute-based stats like Attack Damage, Max Health, Movement Speed are a little harder to deal with. This is because, as they are handled by Minecraft itself, MythicLib has no guarantee that it is the only plugin modifying these stats. Other plugins may also add their own attribute modifiers, and Minecraft itself applies some default modifiers depending on the player's equipment.

For this reason, the _final_ stat value refers to **the value that Minecraft would return**, that is, taking into account all attribute modifiers from all plugins and Minecraft itself. The _total_ stat value refers to the value that MythicLib computes, taking into account only the stat modifiers registered through MythicLib's API.

For example, if a player with 20 base Max Health is wearing a +10 Max Health armor (MythicLib API), and another plugin adds +5 Max Health through its own Minecraft attribute modifier, then the total Max Health would be 30, while the final Max Health would be 35.

::: info
For non-vanilla stats like _Critical Strike Chance_ or _Skill Damage_, the total and final stat values are always the same, as these stats are not handled by Minecraft itself.
:::

The following methods return the final stat value of a stat
```java
double moveSpeedFinal = statMap.getStat("MOVEMENT_SPEED");
double moveSpeedFinal = statMap.getInstance("MOVEMENT_SPEED").getFinal();
```

The following method returns the total stat value of a stat.
```java
double moveSpeedTotal = statMap.getInstance("MOVEMENT_SPEED").getTotal();
```

