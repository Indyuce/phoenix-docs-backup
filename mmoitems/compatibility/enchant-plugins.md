---
order: 3
---

# 🔮 Enchant Plugins

MMOItems features native compatibility for [EcoEnchants](https://www.spigotmc.org/resources/ecoenchants-⭕-250-enchantments-✅-create-custom-enchants-✨-essentials-cmi-support.79573), [MythicEnchants](https://mythiccraft.io/index.php?resources/mythicenchantments-early-access.397) and [AdvancedEnchants](https://www.spigotmc.org/resources/43058) partially. Most modern enchant plugins that feature a reasonable implementation of enchants (aka that use the Bukkit enchantment registry) should work fine with MMOItems.

## Implementing compatibility with your custom enchant plugin
Your plugin has to be using the default Bukkit enchantment registry if you want to be compatible with MMOItems. Create and register an instance of `EnchantPlugin` and register it in MMOItems using the following code (run this **BEFORE** MMOItems enables):
```java
MMOItems.plugin.registerEnchantPlugin(...);
```

Here is the interface you must implement:
```java
/**
 * There are three types of enchant plugins.
 * - enchants saved using the Bukkit Enchantment interface (EcoEnchants, MythicEnchants)
 * - enchants saved in the NBT (AdvancedEnchants)
 * - enchants saved in lore only (CrazyEnchants)
 * <p>
 * Interface used to support plugins which use the Bukkit Enchantment
 * interface to register their enchantments. This makes enchant storage
 * so much easier for MMOItems.
 *
 * @param <T> The plugin class implementing Enchantment
 */
public interface EnchantPlugin<T extends Enchantment> {

    /**
     * @param enchant Enchant being checked
     * @return If this enchant plugin handles a given enchant
     */
    boolean isCustomEnchant(Enchantment enchant);

    /**
     * Called when an item is built. This should be used to add the enchantment
     * lines to the item lore or add any item tag required by the enchantment.
     *
     * @param builder Item being built
     * @param enchant Enchantment being applied
     * @param level   Enchant level
     */
    void handleEnchant(ItemStackBuilder builder, T enchant, int level);

    NamespacedKey getNamespacedKey(String key);
}
```

Here is, for instance, the implementation for the MythicEnchants plugin. The `MythicEnchant` class is a class that extends the default `Enchantment` Bukkit class. `getNamespacedKey(String)` should return a namespaced key with your plugin as namespace. `handleEnchant(...)` is ran everytime an item is (re)generated and basically adds one line to the lore to indicate that an enchant is applied onto the item. the `ItemStackBuilder` class can be used to access the `LoreBuilder` class which contains all the methods required to edit the item lore. `LoreBuilder#insert(int, String)` can be used to insert at 1st position any string.
```java
public class MythicEnchantsSupport implements EnchantPlugin<MythicEnchant> {

    @Override
    public boolean isCustomEnchant(Enchantment enchant) {
        return enchant instanceof MythicEnchant;
    }

    @Override
    public NamespacedKey getNamespacedKey(String key) {
        return new NamespacedKey(MythicEnchants.inst(), key);
    }

    public void handleEnchant(ItemStackBuilder builder, MythicEnchant enchant, int level) {
        Validate.isTrue(level > 0, "Level must be strictly positive");

        // Type cannot be changed. Must make sure that item is an enchanted book

        if (!builder.getMeta().hasItemFlag(ItemFlag.HIDE_ENCHANTS))
            builder.getLore().insert(0, LoreParser.formatEnchantment(enchant, level));
    }
}
```

Enchant plugins like EcoEnchants do NOT need you to register that `EnchantPlugin` implementation because the lore display is handled using packets which is another possibility.

## If your enchant plugin doesn't use the Bukkit enchant registry

::: warning
This is getting changed in MI7
:::

It's a little harder because you need to register a new item stat that will recognize the NBT tags that you use to save the enchant data. Plugins like AdvancedEnchants do save enchants using NBT tags like `ae_enchant:thorns` (and the enchant level is the tag value). It really is recommended to use the Bukkit registry.

You can check the `ItemStat` implementation for AdvancedEnchants at `net.Indyuce.mmoitems.comp.enchants.advanced_enchants` (check source code).

Register your stat **BEFORE** MMOItems enables using:
```java
MMOItems.plugin.getStats().register(...);
```