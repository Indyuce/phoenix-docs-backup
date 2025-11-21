---
order: 2
---

# 🔌 Installation Guide

### Installing MMOItems Premium on 1.14+
Drag and drop the latest builds of MythicLib and MMOItems on your server and restart it.

<details>
<summary>Installing MMOItems Premium on Legacy (<1.13) </summary>

Since 4.7.6, MMOItems Premium features 1.12 support however 1.14+ remains the plugin native version. You will need to download the [1.12 default config files](https://www.dropbox.com/s/7j9gowyd32wy9cv/legacy-configs-UPDATED.zip?dl=1) and install them manually after you have started your server once with the MI build installed.

If you're running WorldGuard on a Legacy server, you **MUST** install **MMOItems LegacyWG ([Download](https://github.com/mmopluginteam/mmoitems-legacywg/releases))** otherwise MMOItems will spit out an error when loading and it will not enable.

**Recent versions of MMOItems Premium (6.0.0+) no longer support 1.12, make sure you keep your server up to date to benefit from all the features of MMOItems!**

</details>

### 


### Addon: MMOMana ([Download](https://github.com/mmopluginteam/mmoitems-mana/releases))
MMOMana is the up-to-date, open-source and maintained version of the old MMOItems Mana&Stamina addon. It adds mana & stamina resources to players which can be used in different MMOItems mechanics.
**MMOMana is NOT compatible with other RPG core plugins which already handle mana and stamina.**
*Note:* The placeholders provided by MMOMana are the same as the old Mana&Stamina addon!
* %mana_mana%
* %mana_stamina%
* %mana_mana_regen%
* %mana_stamina_regen%
* %mana_mana_bar%
* %mana_stamina_bar%
* %mana_max_mana%
* %mana_max_stamina%

### Addon: MI PerWorldDrops ([Download](https://github.com/mmopluginteam/mmoitems-perworlddrops/releases))
MMOItems PerWorldDrops allows you to have **drop tables restricted to certain worlds** for blocks and monsters. You can drag & drop this addon in your plugins folder just like with MMOItems. A /drops folder should appear in the MMOItems plugin folder after rebooting your server. In that folder, each .yml you create corresponds to a specific world (the file name has to match **EXACTLY** the world name). In order to know how to setup these YAML configs, please refer to this [wiki page](Item Drop Tables).

This addon is kept up to date and comes handy if you don't need huge/complex drop table plugins like MMOCore or MythicMobs.