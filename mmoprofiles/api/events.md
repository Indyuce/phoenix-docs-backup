---
order: 5
---

# 📮 Events

## Profile Creation and Removal

When a profile is created, `ProfileCreateEvent` is called. This event contains the player UUID and the profile UUID of the newly created profile. You can listen to this event to perform actions when a new profile is created. This event stores a `CompletableFuture<Void>` which is completed once all data modules have validated this event.

`ProfileRemoveEvent` is called when a user permanently deletes one of their profile. You can use this event to remove the record corresponding to the deleted profile in your plugin's database. This event stores a `CompletableFuture<Void>` which is completed once all data modules have validated this event.

## Profile Selection and Unselection

When a player selects a profile, `ProfileSelectEvent` is called. When all data modules have validated this event, the profile is applied to the player, that is, the player is teleported to its previous location, its inventory is restored, etc...

When a player unselects a profile by either logging out, quitting their profile or switching to another profile, `ProfileUnloadEvent` is called.

In case of a profile switch, `ProfileUnloadEvent` is guaranteed to be called before the `ProfileSelectEvent` of the new profile. In case of a logout or upon quiting the current profile with no switch, only `ProfileUnloadEvent` is called. On logouts, `ProfileUnloadEvent` is guaranteed to be called after `PlayerQuitEvent`.

## Proxy-Mode Events

When proxy-mode profiles are enabled, `PlayerIdDispatchEvent` is called at least one tick after the player joins (after `PlayerJoinEvent`) when the proxy finally provides the backend server with the player's real UUID and profile UUID.

::: info
When the player joins the server, the player already has its spoofed UUID, as spoofing happens at the proxy-level. Therefore, the player's official UUID (as well as other generic player information) need to be forwarded from the proxy to the backend server, via plugin messages. `PlayerIdDispatchEvent` is called when the backend server receives this information from the proxy.
:::
