---
order: 2
---

# 🫅 Player Data

Once you have retrieved an instance of `ProfileProvider`, you can access data of online players using the following method. The player data class is `ProfileList`.


```java
UUID playerId = /* TODO */;
ProfileProvider provider = /* see previous page */;

// get player data
ProfileList playerData = provider.getPlayerData(playerId);
```

You can also access the profile list and current profile of a player using the following methods. The profile class is `PlayerProfile`.

```java
// get all profiles from player
List<PlayerProfile> profiles = playerData.getProfiles();

// get current profile
@Nullable PlayerProfile currentProfile = playerData.getCurrent();
```

Once you have an instance of `PlayerProfile`, you can retrieve information about that profile, including its health, attribute data, inventories... Most methods are pretty straight-forward and close to their Bukkit equivalent.

## Location maps

::: info
Using MMOProfiles on proxied servers comes with a few challenges, including correctly handling player locations. Players can log out in a server with a specific map, and log back in a server where this map does not exist. In other words, there is no one-to-one correspondance between maps across backend servers.
:::

Where you'd need to store a Bukkit `Location`, MMOProfiles now stores a `LocationMap` instead. Location maps simply bind locations to _servers groups_ (see [below](#server-groups)). If two servers are in the same group, MMOProfiles will use the same locations for these two servers. It is the responsiblity of the admin to correctly setup server groups.

- `PlayerProfile#getLocation()` returns the last location of the profile, in the server group of the running server. Note that if server groups have not been setup correctly, and MMOProfiles finds a non existing world, this method will fallback to the profile selection location.
- `PlayerProfile#getLocationMap()` returns an instance of `LocationMap`. Location maps are also used for the player's last location, bed spawn point and compass target location.

Note that MMOProfiles uses a custom object `WrappedLocation` to store players' locations inside location maps. The only difference with the Bukkit counterpart `Location` is that the `World` object is not parsed (world name is saved as a string), to avoid MMOProfiles running into an exception.

### Server Groups

By "server group" we refer to all servers on a proxy which share the same **server identifier**. The server identifier is a small piece of text that you can configure inside your MMOProfiles `config.yml`. Since this config file is server-specific, multiple servers may have different server identifiers.

```yml
server-identifier: 'default'
```

Two servers with the same identifier are in the same group. By default, all servers are within the same group with identifier `default`.

