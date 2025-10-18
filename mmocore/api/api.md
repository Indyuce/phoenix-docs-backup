# 🔧 Plugin API

## Player data
Player data is stored inside `PlayerData` instances which can be manipulated and accessed using the static ``get`` methods from that class:
```java
PlayerData playerData = PlayerData.get(/* player UUID or Player instance */);
playerData.setLevel(10); // Sets player level to 10
playerData.giveExperience(500); // Gives 500 experience to the player
```
You can modify the player class, level, party, skill data, quest data and anything else. Player data is loaded sync when the player joins, on event priority NORMAL.

## Adding extra quest conditions/triggers/drop table items/conditions
In order to improve compatibility with other drop table or quest plugins, you may need to register extra options like drop table items, conditions, or quest conditions/triggers.

Loading these options are made using instances of ``MMOLoader``. The more loaders MMOCore has, the more of these options it can recognize (just like skill mecanics or drop table items in MythicMobs). First, you need to setup your `MMOLoader` so it loads any extra option. For example, here is the default ``MMOLoader``:
```java
    @Override
    public Trigger loadTrigger(MMOLineConfig config) {
        if (config.getKey().equals("message"))
            return new MessageTrigger(config);

        if (config.getKey().equals("sound"))
            return new SoundTrigger(config);

        if (config.getKey().equals("command"))
            return new CommandTrigger(config);

        if (config.getKey().equals("item"))
            return new ItemTrigger(config);

        if (config.getKey().equals("exp"))
            return new ExperienceTrigger(config);

        return null;
    }

    @Override
    public DropItem loadDropItem(MMOLineConfig config, DropTableManager tables) {
        if (config.getKey().equals("droptable"))
            return new DropTableDropItem(tables, config);

        if (config.getKey().equals("vanilla"))
            return new VanillaDropItem(config);

        if (config.getKey().equals("note"))
            return new NoteDropItem(config);

        if (config.getKey().equals("gold"))
            return new GoldDropItem(config);

        return null;
    }

    @Override
    public Objective loadObjective(MMOLineConfig config, ConfigurationSection section) {
        if (config.getKey().equals("goto"))
            return new GoToObjective(section, config);

        if (config.getKey().equals("mine"))
            return new MineBlockObjective(section, config);

        if (config.getKey().equals("kill"))
            return new KillMobObjective(section, config);

        if (config.getKey().equals("getitem"))
            return new GetItemObjective(section, config);

        if (config.getKey().equals("clickon"))
            return new ClickonObjective(section, config);

        return null;
    }

    @Override
    public Condition loadCondition(MMOLineConfig config) {
        // TODO Auto-generated method stub
        return null;
    }
```
As you can see, you must override one method from the MMOLoader superclass for each option type (trigger/condition/drop item...). `config` returns an object which lets you get info about line configs like `vanilla{type=DIAMOND} 0.5 1-3` (similar to MythicMobs API).

Once your MMOLoader is setup, you must register it in MMOCore using `MMOCore.plugin.loadManager.registerLoader(yourMMOLoader)`. Make sure you register it before **MMOCore is enabled**. Either make your plugin load before MMOCore and register it when it enables, or don't risk any loading order issue and register it when your plugin is **loading** after MMOCore has been loaded.

::: info
In the future, drop tables and items will be moved to MythicLib in order to unify MMOItems and MMOCore drop tables. Quest triggers/conditions from MMOCore will be merged into the MythicLib scripting system as well.
:::