---
order: 2
---

# 🪣 API Usage

The main API class is `ProfileProvider`. You can access the MMOProfiles implementation of this interface using Bukkit's service provider.

```java
ProfileProvider provider = Bukkit.getServicesManager().getRegistration(ProfileProvider.class).getProvider();
```

This service is provided by MMOProfiles when the plugin enables. If you want to access this service from inside your plugin's `onEnable`, you need to declare MMOProfiles as a soft (or hard) dependency in your plugin `plugin.yml`.

```yml
softdepend: [ ..., MMOProfiles ]
```

## Check if Proxy-mode profiles is on

The following code snippet can be used to check if MMOProfiles is currently running proxy-mode profiles.

```java
// possible values: PROXY, LEGACY, NONE
// are proxy-mode profiles enabled?
boolean proxyMode = MythicLib.plugin.getProfileMode() == ProfileMode.PROXY;
```