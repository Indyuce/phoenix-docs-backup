## Using SkillAPI, ProSkillAPI, Fabled

### Custom Skill Registration

Similarly to MythicMobs, you can register custom skills into MythicLib using the Fabled skill editor. The process is the exact same as in [this tutorial](https://gitlab.com/phoenix-dvpmt/mythiclib/-/wikis/Using-MythicMobs#custom-skill-registration) apart from the format of the MythicLib skill configuration file.

First, code your skill using the Fabled skill editor. Then, open up a YML config file within the `MythicLib/skill` folder, and instead of using:
```
mythicmobs-skill-id: <Mythic skill name>
```
use:
```
fabled-skill-id: <Fabled skill identifier>
```

As of MythicLib 1.6.2 snapshots, SkillAPI and ProSkillAPI are no longer maintained ; users are asked to use Fabled instead. Note that for backwards compatibility, `skillapi-skill-id` can still be used instead of `fabled-skill-id`.

### Skill Modifiers

**There is currently no way to retrieve skill modifiers when using Fabled skills, unlike when using MythicMobs.** However all skills registered using Fabled have a `level` skill modifier which hooks directly into Fabled skill level system. Basically you can setup skill mechanic numerical parameters to linearly scale on the skill level. Using MythicMobs you'd have been able to setup any type of scaling you want (not limited to linear scaling).

Just like `cooldown` `mana` and `stamina`, the `level` modifier is already registered so it's useless to have it in the `modifiers` list in the config sample above.

**Due to this specific Fabled limitation, we recommend the use of MythicMobs instead of Fabled for custom skill creation, although it is still an option.** You will see why this is such a limitation when working on complex skills that require non-linear profiles for its numerical parameters.

## Using MythicLib

You can create custom skills using the MythicLib scripting language, learn more about scripts [here](https://gitlab.com/phoenix-dvpmt/mythiclib/-/wikis/Custom%20Scripts). A full tutorial on how to convert MythicLib scripts into skills can also be found on the same page [here](Custom%20Scripts#registering-a-custom-skill-using-mythiclib-scripts).