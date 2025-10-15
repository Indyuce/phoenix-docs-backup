---
order: 3
---

# 📦 Custom Data Modules

A profile data module corresponds to a plugin that owns profile-dependant data. MMOCore, MMOInventory have their own profile data module. When a player selects a profile, MMOProfiles asks to all profile data modules to load into server RAM the profile data of the selected player profile, for the given player. MMOProfiles does not let the user play (nor quit the profile selection area) before ALL profile data modules have successfully loaded their profile-dependant data.

If you have a plugin that owns profile-dependant data (quest progress, custom inventories, player leveling, professions, etc...) you will have to implement your own `ProfileDataModule` and register it in MMOProfiles.

## Implement `ProfileDataModule`

The `ProfileDataModule` interface has two methods:

- `#getOwningPlugin()` which should return the main instance of your plugin
- `#getIdentifier()` which should return a unique string following this `lower_case_format`. It will be used by MMOProfiles to parse profile placeholders (see below).

MMOProfiles expects EVERY profile data module to listen to the following events:

* `ProfileCreateEvent` called when a player creates a profile.
* `ProfileSelectEvent` called when a player selects a profile.
* `ProfileUnloadEvent` called when a player logs off and needs their profile data saved.

These two events have one method called `#validate(ProfileDataModule)` which needs to be called (passing your profile data module instance as argument) when your plugin is done loading profile-specific data.

For information purposes, here is what the MMO plugins do. When a profile is selected, profile data is loaded asynchronously, and the `#validate(ProfileDataModule)` method is called afterwards. MMOProfiles only lets the player join the server when all registered profile data modules have called this method. When a profile is unselected, profile data is unloaded and saved asynchronously, after which the validate method is called.

```java
Plugin plugin;
ProfileDataModule module;
PlayerDataManager manager; // Not part of Profile API

@EventHandler
public void onProfileSelection(ProfileSelectEvent event) {
    final PlayerData data = manager.get(event.getPlayer());
    manager.loadData(data).thenAccept(Tasks.sync(plugin, v -> {
        // ...
        event.validate(module);
    }));
}

@EventHandler
public void onProfileUnload(ProfileUnloadEvent event) {
    manager.unregister(event.getPlayer()).thenAccept(Tasks.sync(plugin, v -> {
        // ...
        event.validate(module);
    }));
}
```

## Register your instance of `ProfileDataModule`

Run this code **in the #onEnable() of your plugin** to register your instance of `ProfileDataModule`. If your module is an instance of `Listener`, MMOProfiles will register its events for you.

```java
ProfileProvider provider = /* TODO */;
ProfileDataModule yourProfileDataModule = /* TODO */;
provider.registerModule(yourProfileDataModule);
```