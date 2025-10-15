# 🗒️ Config Options

## Removing damage particles
Some servers use very high damage values which can summon way too many damage particles on the client side. This can cause FPS drops and deeply lower user experience. In order to fix that we've integrated a damage particle cap in MythicLib which lets you control the amount of damage particles displayed. Head to the MythicLib `config.yml` file:
```yml
damage-particles-cap:
  max-per-tick: 10
  enabled: false
```
Enable this option by toggling on the `enabled` option and input the value you want for the `max-per-tick` option. This corresponds to the **maximum amount of particles emitted by one entity in ONE tick**.

## Health Scale
Health scaling is a small sized RPG feature which makes the player health bar always display the same amount of hearts (while still having extra max. health). When scaling your health to 40 (default value), the player health bar will always display 2 rows (`2 * 20`) of hearts.

![](https://i.imgur.com/2wl2fpg.png)

![](https://i.imgur.com/BNrYOoG.png)

You can configurate the health scale feature in the **MythicLib** main config file. It is pretty self explanatory:
```yml
# Allows to scale health up/down to a specific amount
# so extra max health does not fill up the screen.
health-scale:
    enabled: true
    scale: 40
```