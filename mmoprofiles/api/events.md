---
order: 5
---

# 📮 Events

::: warning
This page is subject to change with the addition of live profile switching in recent dev builds
:::

`ProfileRemoveEvent` is not being used yet. It will be used in the future to notify plugins that an user has permanently deleted one of their profiles. External plugins can listen to it to empty their player database.

When proxy-mode profiles are enabled, `PlayerIdDispatchEvent` is called when the player logs in (in order, `PlayerLoginEvent` -\> `PlayerIdDispatchEvent` -\> `PlayerJoinEvent`). It contains the real player's UUID (from Mojang servers, if online mode is set to true) as well as the fake/spoofed/profile UUID.

## Check if Proxy-mode profiles is on

The following code snippet can be used to check if MMOProfiles is currently running proxy-mode profiles.

```java
// possible values: PROXY, LEGACY, NONE
// are proxy-mode profiles enabled?
boolean proxyMode = MythicLib.plugin.getProfileMode() == ProfileMode.PROXY;
```