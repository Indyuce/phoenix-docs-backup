Using MMOItems API you may register custom stats as complex as abilities or item restrictions. The first thing you will need to do is define a class which extends `ItemStat` which is an abstract class with many functions, we will go over what each does, but first let's deal with the ItemStat constructor you need to call.

## ItemStat constructor
```public ItemStat(String id, Material material, String name, String[] lore, String[] types, Material... materials)```

The `id` String corresponds to your internal stat ID. You may only use upper case letters and _ dashes. This stat is used to calculate player stats in MMOLib, used to saved stat data in MMOItems config files, literally anywhere in the plugin. Do never change it once your stat is setup otherwise you might "lose" previously created item data.

The `material` parameter corresponds to the icon your stat has in the item edition GUI. `name` corresponds to your stat name, it's also used to display your stat in the edition GUI. This piece of string cannot be seen by normal players. `lore` is your stat description (edition GUI).

`types` is the list of the item types which are supported by your item stat.\
`new String[] { "!armor", "!gem_stone", "all" }` would ban armors and gem stones from using your stat. Using `!<type_name>` you can ban a specific item type. Make sure you put type restrictions at the beginning of the string array. Using `all` you can make the stat compatible with any item type. Make sure you use `all` after type restrictions.

`materials` are the item materials supported. This is specific to some stats like `Dye Color` or `Shield Pattern` which depend on the ItemMeta instance and which are type-specific. If the given array is empty, the stat is obviously available for any type by default.

## Methods to override
This is the class for numeric stats.
```
@Override
public StatData whenInitialized(Object object) {
	return new DoubleData(object);
}

@Override
public RandomStatData whenInitializedGeneration(Object object) {
	if (object instanceof Number)
		return new NumericStatFormula(Double.valueOf(object.toString()), 0, 0, 0);
	
	if (object instanceof ConfigurationSection) 
		return new NumericStatFormula((ConfigurationSection) object);
	
	throw new IllegalArgumentException("Must specify a number or a config section");
}

@Override
public void whenApplied(MMOItemBuilder item, StatData data) {
	double value = ((DoubleData) data).generateNewValue();
	item.addItemTag(new ItemTag(getNBTPath(), value));
	item.getLore().insert(getPath(), formatPath(value, "#", new StatFormat("##").format(value)));
}

@Override
public boolean whenClicked(EditionInventory inv, InventoryClickEvent event) {
	if (event.getAction() == InventoryAction.PICKUP_HALF) {
		ConfigFile config = inv.getItemType().getConfigFile();
		config.getConfig().set(inv.getItemId() + "." + getPath(), null);
		inv.registerItemEdition(config);
		inv.open();
		inv.getPlayer().sendMessage(MMOItems.plugin.getPrefix() + "Successfully removed " + getName() + ChatColor.GRAY + ".");
		return true;
	}
	new StatEdition(inv, this).enable("Write in the chat the numeric value you want.",
			"Or write [MIN-VALUE]=[MAX-VALUE] to make the stat random.");
	return true;
}

@Override
public boolean whenInput(EditionInventory inv, ConfigFile config, String message, Object... info) {
	String[] split = message.split("\\=");
	double value = 0;
	double value1 = 0;
	try {
		value = Double.parseDouble(split[0]);
	} catch (Exception e1) {
		inv.getPlayer().sendMessage(MMOItems.plugin.getPrefix() + ChatColor.RED + split[0] + " is not a valid number.");
		return false;
	}

	// second value
	if (split.length > 1)
		try {
			value1 = Double.parseDouble(split[1]);
		} catch (Exception e1) {
			inv.getPlayer().sendMessage(MMOItems.plugin.getPrefix() + ChatColor.RED + split[1] + " is not a valid number.");
			return false;
		}

	// STRING if length == 2
	// DOUBLE if length == 1
	config.getConfig().set(inv.getItemId() + "." + getPath(), split.length > 1 ? value + "=" + value1 : value);
	if (value == 0 && value1 == 0)
		config.getConfig().set(inv.getItemId() + "." + getPath(), null);
	inv.registerItemEdition(config);
	inv.open();
	inv.getPlayer().sendMessage(MMOItems.plugin.getPrefix() + getName() + " successfully changed to "
			+ (value1 != 0 ? "{between " + value + " and " + value1 + "}" : "" + value) + ".");
	return true;
}

@Override
public void whenLoaded(MMOItem mmoitem, NBTItem item) {
	if (item.hasTag(getNBTPath()))
		mmoitem.setData(this, new DoubleData(item.getDouble(getNBTPath())));
}

@Override
public void whenDisplayed(List<String> lore, FileConfiguration config, String id) {
	lore.add("");

	String[] split = config.contains(id + "." + getPath()) ? config.getString(id + "." + getPath()).split("\\=") : new String[] { "0" };
	String format = split.length > 1 ? tryParse(split[0]) + " -> " + tryParse(split[1]) : "" + config.getDouble(id + "." + getPath());

	lore.add(ChatColor.GRAY + "Current Value: " + ChatColor.GREEN + format);
	lore.add("");
	lore.add(ChatColor.YELLOW + AltChar.listDash + " Left click to change this value.");
	lore.add(ChatColor.YELLOW + AltChar.listDash + " Right click to remove this value.");
}
```

### whenInitialized(Object)
`whenInitialized(Object)` is called when MMOItems is requesting to read stat data from the config file. `obj` could be anything, it's the object obtained using `ConfigurationSection#get(#yourStatPath#)`. Here, users can either use a double to have a set stat value, or a config section and in that case MMOItems reads a numeric stat formula from that config section.

This method must return a class which extends the `StatData` interface. It's a **purely cosmetic** interface because it has no function to override but I might need to add some functions to it in a later update. **You can see a StatData class example under the _Mergeable Stats_ section**.

### whenInitializedGeneration(Object)
`whenInitializedGeneration(Object)` is almost the same thing, except that should return a `RandomStatData` instance. The `RandomStatData` interface is used to store data about stat data from an item generation template. For further info, see the RandomStatData paragraph below.

### whenApplied(MMOItemBuilder, StatData)
This function is used by MMOItems when generating an `ItemStack` instance based on a list of `StatData` instances. You can access the item meta, item lore using the `MMOItemBuilder` instance. You will need to cast the `StatData` instance given as input to whatever your stat is compatible with. MMOItems only gives you as input what you gave it as output in the `whenInitialized(Generation)` methods.

### whenClicked(EditionInventory, InventoryClickEvent)
This is the function used to do stuff when a player just clicked the stat icon in the item edition GUI.

### whenInput(EditionInventory, ConfigFile config, String message, Object...)
Used to do stuff when a player just inputs some message in the chat. You can request for a player chat input using the following method:
```new StatEdition(inv, this, objectArray).enable("Write in the chat the numeric value you want.", "Or write [MIN-VALUE]=[MAX-VALUE] to make the stat random.");```
That function would typically be called when the player clicks the stat icon in the edition GUI. The `objectArray` parameter in the `StatEdition` class constructor can be replaced by **any object at all**, it's a way for more complex stats like elements or abilities what the player is editing (is it the ability casting mode, what ability, etc??). That array is kept intact and given as input in the `whenInput` method.

### whenLoaded(MMOItem, NBTItem)
Used to load stat data from a random ItemStack.

### whenDisplayed(List<String>, ConfigurationSection, String)
It's a really old method which will be updated soon. It's the function used to display the current item stat data in the edition GUI. It is still using config sections as input, it will be soon replaced by StatDatas for cleaner functionality.

## RandomStatDatas
They are the equivalent of StatData's but with a random factor needed for random item generation. A good example is the NumericStatFormula which is used for any numeric stats.
```
public class NumericStatFormula implements RandomStatData {
	private final double base, scale, spread, maxSpread;

	private static final Random random = new Random();

	public static final NumericStatFormula ZERO = new NumericStatFormula(0, 0, 0, 0);

	public NumericStatFormula(Object object) {
		Validate.notNull(object, "Config must not be null");

		if (object instanceof Number) {
			base = Double.valueOf(object.toString());
			scale = 0;
			spread = 0;
			maxSpread = 0;
			return;
		}

		if (object instanceof ConfigurationSection) {
			ConfigurationSection config = (ConfigurationSection) object;
			base = config.getDouble("base");
			scale = config.getDouble("scale");
			spread = config.getDouble("spread");
			maxSpread = config.getDouble("max-spread");

			Validate.isTrue(spread >= 0, "Spread must be positive");
			Validate.isTrue(maxSpread >= 0, "Max spread must be positive");
			return;
		}

		throw new IllegalArgumentException("Must specify a config section or a number");
	}

	/*
	 * used as a StatData class to generate a DoubleData instance!
	 */
	public NumericStatFormula(double base, double scale, double spread, double maxSpread) {
		this.base = base;
		this.scale = scale;
		this.spread = spread;
		this.maxSpread = maxSpread;
	}

	public double getBase() {
		return base;
	}

	public double getScale() {
		return scale;
	}

	public double calculate(double x) {

		// calculate linear value
		double linear = base + scale * x;

		// apply gaussian distribution to add +- maxSpread%
		// spread represents the standard deviation in % of the calculated
		// linear value
		double gaussian = linear * (1 + Math.min(Math.max(random.nextGaussian() * spread, -maxSpread), maxSpread));

		return gaussian;
	}

	@Override
	public StatData randomize(GeneratedItemBuilder builder) {
		return new DoubleData(calculate(builder.getLevel()));
	}
}
```
The `randomize` function is the key here. This takes as input a GeneratedItemBuilder which contains info about the item level, tier etc. and outputs a randomized `RandomStatData`, i.e a `StatData` instance which will be later used to build the item!

The `GeneratedItemBuilder` class can be seen as the equivalent of the `MMOItemBuilder` for random stat generation. When a random item is being generated from an item template, MMOItems first creates a `GeneratedItemBuilder`, rolls the item modifiers and gather the randomized `StatData` when generates the item using a `MMOItemBuilder`.

## Mergeable stats
Mergeable stats are stats which can be stacked with each others, for instance when a player tries to apply a gem stone onto another item, where MMOItems needs to "merge" the two stat datas together. A good example is the `DoubleData` class.
```
public class DoubleData implements StatData, Mergeable {
	private static final Random random = new Random();

	private double min, max;

	public DoubleData(Object object) {
		if (object instanceof Number) {
			min = Double.valueOf(object.toString());
			return;
		}

		if (object instanceof String) {
			String[] split = ((String) object).split("\\=");
			Validate.isTrue(split.length == 2, "Must specify a valid range");
			min = Double.parseDouble(split[0]);
			max = Double.parseDouble(split[1]);
			return;
		}

		throw new IllegalArgumentException("Must specify a range or a number");
	}

	public DoubleData(double min, double max) {
		this.min = min;
		this.max = max;
	}

	public boolean hasMax() {
		return max > min && max != 0;
	}

	public double getMin() {
		return min;
	}

	public double getMax() {
		return max;
	}

	public void setMax(double value) {
		max = value;
	}

	public void setMin(double value) {
		min = value;
	}

	public void add(double value) {
		min = min + value;
	}

	public void addRelative(double value) {
		min *= 1 + value;
	}

	public double generateNewValue() {
		return hasMax() ? min + random.nextDouble() * (max - min) : min;
	}

	@Override
	public void merge(StatData data) {
		Validate.isTrue(data instanceof DoubleData, "Cannot merge two different stat data types");
		min += ((DoubleData) data).min;
		// TODO if hasMax()
	}
}
```
Simple enough: MMOItems just adds the two values together. A little specification here: the `min` and `max` options are used to have a stat range but whenever that `StatData` is loaded from an NBTItem using `whenLoading(MMOItem mmoitem, NBTItem)`, only the `min` variable is used because a generated item does not have stat ranges anymore, they have already been rolled on item generation.

## Registering a stat
You now need to register your stat by running
```MMOItems.plugin.getStats().register(ItemStat);```
Make sure you register your stat before MMOItems enables, either right after MMOItems loads if it's a depend, or when your plugin enables if it's a loadbefore. MMOItems does handle `Listener` stats, no need to register them later on.

This registers the stat in MMOItems, so by default your stat will appear in the item edition GUI. The following two steps will make your stat display in the item lore on any generated item:

1) Add your stat to your current lore format. You can do this by opening `language/lore-format.yml` and adding one line there; for example, `- '#attack-damage#'` is the line for the Attack Damage stat.

2) Edit your `stats.yml` configuration section and add the required translations here; for instance you'd add `attack-damage: '&3 &7➸ Attack Damage: &f{value}'` for the Attack Damage stat.

## Item Restrictions
```
public class RequiredLevel extends DoubleStat implements ItemRestriction {

	/*
	 * stat that uses a custom DoubleStatData because the merge algorithm is
	 * slightly different. when merging two "required level", MMOItems should
	 * only keep the highest levels of the two and not sum the two values
	 */
	public RequiredLevel() {
		super("REQUIRED_LEVEL", new ItemStack(VersionMaterial.EXPERIENCE_BOTTLE.toMaterial()), "Required Level",
				new String[] { "The level your item needs", "in order to be used." }, new String[] { "all" });
	}

..........

	@Override
	public boolean canUse(RPGPlayer player, NBTItem item, boolean message) {
		int level = item.getInteger("MMOITEMS_REQUIRED_LEVEL");
		if (player.getLevel() < level && !player.getPlayer().hasPermission("mmoitems.bypass.level")) {
			if (message) {
				Message.NOT_ENOUGH_LEVELS.format(ChatColor.RED).send(player.getPlayer(), "cant-use-item");
				player.getPlayer().playSound(player.getPlayer().getLocation(), Sound.ENTITY_VILLAGER_NO, 1, 1.5f);
			}
			return false;
		}
		return true;
	}
}
```
Simply let your class implement `ItemRestriction` and override the `canUse(RPGPlayer, NBTItem, boolean)` method.

## Proper Stats
"Proper" stats are a very specific type of stats. These are stats which are supported by gem stones but which **must not** be applied onto the target item when a gem stone is being attached onto another item.\
Examples: custom model data, shield patterns, custom sounds...

Let your stat class implement the `ProperStat` interface if you don't want gems to apply the potential gem stone stat data onto the target item.

## Upgradable
More on this later when API is reworked. It's used to make stats upgradable using item upgrade templates.