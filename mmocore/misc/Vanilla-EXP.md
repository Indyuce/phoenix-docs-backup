# 🌟 Vanilla Exp

This simple RPG option lets you display the player's current main class level on the vanilla experience bar. Players can also see how close/far they are from reaching the next level by looking at the actual EXP bar progression. This option can be enabled in `config.yml`:

```yml
# Enable this open to override vanilla EXP and display
# level progress on the vanilla experience bar.
# Requires a SERVER reload when changed.
override-vanilla-exp: true
```
![SbErxxz](uploads/09288c4a1e92ee2aaf65b475599bc312/SbErxxz.png)

It matches the experience and level displayed in the ``/p`` menu.

![5f1IZ9F](uploads/6cb344e5b9dcd3fcccae489f9e1edc4d/5f1IZ9F.png)

## Vanilla EXP redirection

When enabled, a set portion of the EXP you earn via experience orbs is redirected to your main MMOCore class exp. You can change this option in `config.yml`.

```yml
# Redirects vanilla experience obtained to MMOCore
# class experience. You can define the % of the vanilla
# experience that is being transfered as MMOCore exp.
# Requires a SERVER reload when changed.
vanilla-exp-redirection:
  enabled: false
  ratio: 0.8
```

This feature can be useful for survival or simple RPG servers which do not want to spend time on setting up setting up [experiences sources](../level/sources.md) and are okay with relying on vanilla exp dropped by mobs and blocks.