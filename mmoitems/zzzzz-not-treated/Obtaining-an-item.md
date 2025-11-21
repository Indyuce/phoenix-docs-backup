**Make sure you read [this paragraph](Item Creation#how-items-work-very-important) first. The MMOItems item generation system is pretty complex and needs some time to be fully understood.**

Using /mi generate
------------------

*/mi generate* lets you generate a random item based on specific
criterias that you give as command arguments. The command format is the
following: **/mi generate &lt;player&gt; (extra-args)**.

*&lt;player&gt;* indicates the player you will be giving the item to, as
well as the RPG player data the item will be built onto. For instance,
if the player who's running the command is level 20, and if the command
target is level 10, then the item won't scale on level 20 but rather on
level 10.

The available command arguments are listed below:

| Argument                  | Use                                                                                        |
|---------------------------|--------------------------------------------------------------------------------------------|
| -matchlevel               | The item level will match the target player's level.                                       |
| -matchclass               | The item is guaranteed to be usable (class requirements) by the target player.             |
| -gimme                    | Adds the item to your inventory instead, hence the previous remark about *&lt;player&gt;*. |
| -class:&lt;class-name&gt; | The item is guaranteed to be usable by the given class.                                    |
| -level:&lt;integer&gt;    | The item is guaranteed to have level X.                                                    |
| -tier:&lt;tier-name&gt;   | The item is guaranteed to have specified [tier](Item Tiers).                                           |
| -type:&lt;item-type&gt;   | Choose the [item type](Item-Types).                                                                 |
| -id:&lt;id&gt;            | Use that if you want a specific [Item Generator Templates](Item Generator Templates) to be selected.               |

Keep in mind these arguments are all optional (which is what makes the
item gen so powerful) and act as "filters" when MMOItems determines what
item template, tier and item level it will use. Example use: we're
giving to a player a high tier weapon that matches their level and
class:

**/mi generate PlayerName -matchlevel -matchclass -tier:rare**

This would typically be used when opening a lootable chest for example;
it's not specific loot like when finishing a temporary
christmas/halloween event or killing a boss/special monster, but rather
rare, random yet usable stuff (so he does not feel frustrated).

If you were to add loot to a special monster, you would most likely
specify what item you want looted and not give any tier, so that the
player needs to grind the mob to eventually find a higher tier version
of the same weapon.

Using MythicMobs drop tables
----------------------------

[MM Drops](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/drops/Drops)

Using MMOCore drop tables
-------------------------

Use this MMOCore table item if you want to add a specific item generator
template to one of your MMOCore drop tables: 
```
gentemplate{id=TEMPLATE_ID;tier=TIER_NAME;level=<int>;match-level=<true/false>} <chance> <min-max>
```

| Argument                   | Use                                           |
|----------------------------|-----------------------------------------------|
| `id=TEMPLATE_ID`           | Choose what item gen template you are using.  |
| `level=<item-level>`       | Forces the item level to be around level Y.   |
| `tier=ITEM_TIER_ID`        | Forces the item to be tier X.                 |
| `match-level=<true/false>` | The item level will match the player's level. |

Use this MMOCore table item if you do not want to use a specific gen
template, but rather choose one randomly from all registered templates
based on specific criterias. All the previous parameters (except for
`id`) can be used on that format as well: 
```
miloot{type=ITEM_TYPE_ID;class=PLAYER_CLASS;match-class=<true/false>;tier=TIER_NAME;level=<int>;match-level=<true/false>} <chance> <min-max>
```

| Argument                   | Use                                                           |
|----------------------------|---------------------------------------------------------------|
| `type=ITEM_TYPE_ID`        | Forces the item to be of a specific type.                     |
| `class="Class Name"`       | The item is guaranteed to be usable by a certain class.       |
| `match-class=<true/false>` | The player is guaranteed to meet the item class requirements. |