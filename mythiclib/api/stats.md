---
order: 1
---

# 📊 Player Stats

MythicLib stats API design is similar to the Spigot attribute modifiers API. Stat data from every numeric MMOItems/MMOCore stat is stored in a `StatMap` accessible using the following method.

```plaintext
MMOPlayerData playerData = MMOPlayerData.get(playerOrUUID);
StatMap statMap = playerData.getStatMap();
```

Using that class you can access instances of `StatInstance` which correspond to one specific stat.

## Stat Instances

Just like Spigot's attribute instances, stat instances feature a map that **stores stat modifiers**. There are two different types of stat modifiers:

- fixed stat modifiers, which add a fixed/flat amount (+10 Atk Damage)
- % stat modifiers, which multiply the final stat value by a certain constant (+10% Atk Damage)

The advantage of using attributes is that any plugin can add its own attributes, and MythicLib can easily gather all of them and calculate the final stat value based on these attributes. For instance, MMOCore uses attributes to handle experience party buffs:

```plaintext
// +10% experience gained modifier
StatModifier experienceModifier = new StatModifier("myCustomPluginKey", "ADDITIONAL_EXPERIENCE", 10, ModifierType.FLAT); // +10% experience

// Register the modifier
experienceModifier.register(playerData);

// Access all currently registered modifiers this way
statMap.getInstance("ADDITIONAL_EXPERIENCE").getModifiers().forEach(mod -> ...);
```

Notice how any plugin can access all the modifiers created by all the plugins. That means you must make sure your plugin only manipulates the attributes you create which can be done by choosing a very specific **modifier key** like "mmocorePartyBuff" or "mmoitemsItemSetBonus".

## Creating a stat modifier

There are multiple ways of generating a stat modifier. The most exhaustive constructor is the following

```plaintext
StatModifier(UUID, String, String, double, ModifierType, ModifierSource, EquipmentSlot)
```

The first parameter is the UUID. When not provided, a random UUID gets assigned to your new modifier. Every modifier is identified by a UUID. The second parameter, the **modifier key** can also be used to quickly identify the plugin which registered the modifier, but it's **NOT UNIQUE!!** The plugin key should be your plugin name, to make sure that there are no collisions with other systems or plugins. Again, this modifier key is **no longer unique** since MythicLib 1.6.2 builds.

Using this key, you can do things like the following code snippet which clears all modifiers which key start with the `mmoitems` keyword.

```plaintext
statInstance.removeIf(key -> key.startsWith("mmoitems"));
statInstance.removeIf("MyAwesomePlugin"::equals);
```

The third parameter is the stat being modified. This can be `ATTACK_DAMAGE` or `SKILL_CRITICAL_STRIKE_CHANCE` for instance.

The **equipment slot** was implemented to keep track of where that modifier is coming from. It's mostly used by MMOItems and MMOInventory to apply the right stats from an item depending on where it's equipped in the player inventory. If the modifier does not from an item, use `EquipmentSlot.OTHER`, otherwise just use the corresponding equipment slot. This has **LITTLE TO NO** influence if you are dealing with custom stats or player buffs.

The **modifier source** was implemented to differenciate stat modifiers given by melee and ranged weapons. This is also used by MI and MMOInventory to fix similar issues. This also has **LITTLE TO NO** influence if you are dealing with custom stats or player buffs.

You most likely don't need to use the `EquipmentSlot`/`ModifierSource` parameters so you might just need to use the following, simpler constructor.

```plaintext
StatModifier(String, String, double, ModifierType)
```

In order to register your stat modifier, you can use the following method. Make sure you use a wisely chosen modifier key as explained above (if there already exists one modifier with the same key, it will be erased).

```plaintext
modifier.register(MMOPlayerdata);
// Where you'd get the player data using MMOPlayerData#get(Player)
```

You may also use this method which does exactly the same thing:

```plaintext
StatModifier modifier = ...;
StatInstance instance = statMap.getInstance(modifier.getStat());
instance.addModifier(modifier);
```

Note that you can also add **temporary stat modifiers** using the following method. The long parameter corresponds to the duration of the modifier in ticks.

```plaintext
new TemporaryStatModifier(String, String, double, ModifierType, EquipmentSlot, ModifierSource).register(MMOPlayerData, long);
```

## Calculating player stats

For most stats, it is quite easy to calculate the final stat value. Just take the base stat value, apply all the currently registered stat modifiers and return the final value, no?

```plaintext
// calculate the player's crit strike chance
double critChance = statMap.getInstance("CRITICAL_STRIKE_CHANCE").getTotal();
```

This does work for **MOST** stats. For _attack speed_ and _attack damage_, things get a little more complicated with 1.9 dual wielding: take a player attack for instance. If the player is using his mainhand weapon, MythicLib must not consider the Atk Damage and Speed from his offhand weapon, and the same applies if the player is, say, shooting an arrow using his offhand bow. Using the `StatInstance#getFilteredTotal(...)` method we can filter out the modifiers that come from the off hand item using

```plaintext
statMap.getInstance("CRITICAL_STRIKE_CHANCE").getFilteredTotal(Predicate<StatModifier>)
```

The default predicate used as parameter is then

```plaintext
Predicate<StatModifier> DEFAULT_MODIFIER_FILTER = mod -> !mod.getSource().isWeapon() || mod.getSlot() != EquipmentSlot.OFF_HAND
```

If you want to apply a modification to some modifiers (while not actually modifying them in the stat map) and then calculate the stat value, you can use

```plaintext
statMap.getInstance("CRITICAL_STRIKE_CHANCE").getTotal(Function<StatModifier, StatModifier>)
```