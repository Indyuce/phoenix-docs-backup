---
order: 2
---

# 🫅 Player Data

The `ProfileProvider` class is the main class of the Profile API. You can access it using the following code snippet:

```java
ProfileProvider provider = Bukkit.getServicesManager().getRegistration(ProfileProvider.class).getProvider();
```

You can then access the profile data of any online player using the following method. You can also access any player's current profile as well as any player's profile list. A profile is an instance of the `PlayerProfile` class.

```java
UUID playerId = /* TODO */;

// get player data
ProfileList playerData = provider.getPlayerData(playerId);

// get all profiles from player
List<PlayerProfile> profiles = playerData.getProfiles();

// get current profile
@Nullable PlayerProfile currentProfile = playerData.getCurrent();
```

Once you have an instance of `PlayerProfile`, you can retrieve important information about that profile, including its health, attribute data, inventories... Most methods are pretty straight-forward and close to their Bukkit equivalent.

## Player locations accross a proxy

Using MMOProfiles on proxied servers comes with a few challenges, including correctly handling player locations. Players can log out in a server with a specific map, and log back in a server where this map does not exist. In other words, there is no one-to-one correspondance between maps across backend servers.

Where you'd need to store a Location in the Bukkit `Player` instance, MMOProfiles now stores a `LocationMap` instead. Location maps simply bind locations to _servers groups_. If two servers are in the same group, MMOProfiles will use the same locations for these two. It is the responsiblity of the admin to correctly setup server groups (see below).

For instance, `PlayerProfile#getLocation()` will return the last location of the profile, in the server group of the server running the plugin. `PlayerProfile#getLocationMap()` will return the entire `LocationMap` object which has a few extra options. Location maps are used for the player's last location, bed spawn point and compass target location.

### Server Groups

By "server group" we refer to all servers on a proxy which share the same **server identifier**. The server identifier is a small piece of text that you can configure inside your `MMOProfiles/config.yml`. Since this config file is server-specific, multiple servers may have different server identifiers.

```yml
server-identifier: 'default'
```

Two servers with the same identifier are in the same group.

::: warning

:::