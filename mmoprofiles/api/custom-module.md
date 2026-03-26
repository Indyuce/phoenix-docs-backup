---
order: 3
---

# 📦 Custom Data Modules

A profile data module corresponds to a plugin that owns profile-dependant data. All MMO plugins have their own profile data module. When a player selects a profile, MMOProfiles asks to all profile data modules to load the profile data of the selected player profile, for the given player. MMOProfiles does not let the user play (nor quit the profile selection area) before ALL profile data modules have successfully loaded their profile-dependant data.

If you have a plugin that owns profile-dependant data (quest progress, custom inventories, player leveling, professions, etc...) you will have to implement your own `ProfileDataModule` and register it in MMOProfiles.

## Implement `ProfileDataModule`

The `ProfileDataModule` interface has two methods:

- `#getOwningPlugin()` which should return the main instance of your plugin
- `#getId()` which should return a unique name-spaced key. It will be used by MMOProfiles to parse profile placeholders (see below).

### Events to listen to

MMOProfiles expects EVERY profile data module to listen to the following events. You will find more information about these events in the [following Wiki page](./events.md).

- `ProfileSelectEvent` called when a player selects a profile.
- `ProfileUnloadEvent` called when a player unselects a profile.
- `ProfileCreateEvent` called when a player creates a new profile.
- `ProfileRemoveEvent` called when a player deletes a profile.

These events have a method called `#validate(ProfileDataModule)` which needs to be called (passing your profile data module instance as argument) when your plugin is done loading/unloading profile-specific data.

::: tip
A reference implementation of the `ProfileDataModule` interface can be found in MythicLib, in the `DefaultProfileDataModule` class.
:::

The following code snippet provides a pseudo-code for what is supposed to happen on `ProfileSelectEvent` and `ProfileUnloadEvent`. When a profile is selected, profile data is loaded asynchronously, and the `#validate` method is called afterwards. MMOProfiles only lets the player join the server when all registered profile data modules have called this method. When a profile is unselected, profile data is unloaded and saved asynchronously, after which the `#validate` method is called.

```java
Plugin myPlugin;
ProfileDataModule dataModule; // MMOProfiles API
PlayerDataManager manager; // MMO plugin API

@EventHandler
public void onProfileSelection(ProfileSelectEvent event) {
    PlayerData playerData = manager.get(event.getPlayer());
    manager.loadData(playerData).thenAccept(Tasks.sync(plugin, v -> {
        // ...
        event.validate(dataModule);
    }));
}

@EventHandler
public void onProfileUnload(ProfileUnloadEvent event) {
    manager.unregister(event.getPlayer()).thenAccept(Tasks.sync(plugin, v -> {
        // ...
        event.validate(dataModule);
    }));
}
```

### Why and when to validate player sessions

When the player joins the server and selects a profile, MMOProfiles waits until all plugins have loaded their player data before teleporting the player. In the mean time, they are usually left in a "profile selection black box" in order to avoid unwanted interactions during inconsistent player data states.

You don't actually need to call the `#validate` method right away. In fact, you are encouraged to defer calling it until the player data has been loaded from the database.

::: warning
The `#validate` method must be called from the main server thread, or it will raise an exception.
:::

Failure to call the `#validate` (due to a previously unhandled exception, for instance) will result in the player's session freezing, and the player being stuck in the profile selection limbo. After a few seconds of session inactivity, MythicLib will start raising "ghost session" warnings in the console.

## Register your instance of `ProfileDataModule`

Use the following method in the `#onEnable` of your plugin to register your instance of `ProfileDataModule`. If your module is an instance of `Listener`, MMOProfiles will register its events for you.

```java
ProfileProvider provider = /* profile provider */;
ProfileDataModule yourProfileDataModule = /* TODO */;
provider.registerModule(yourProfileDataModule);
```