Just like ingredients, conditions must be met in order to use a recipe. Unlike ingredients, conditions do not take anything from the player inventory when using a crafting recipe. There are several types of recipes conditions, the main being **level** conditions and **permission** conditions. Just like ingredients, conditions are stored in a list inside the recipe config section.

```
...
recipes:
    steel-sword:
        output: 'mmoitems{type=SWORD,id=STEEL_SWORD}'
        ...
        conditions:
        - 'level{level=5,consume=true}'
        - 'permission{list="mmoitems.recipe.steel-sword,mmoitems.recipe.station.steel"}'
        - 'placeholder{placeholder="%ac_Stat_Weight%~>~1"}'
```

| Condition | Usage | Description |
|-----------|-------|-------------|
| Min Lvl. | `level{level=<min>,consume=<true/false>}` | Players must be Lvl X or higher. `consume` is whether or not the levels should be consumed. |
| Class | `class{list=<Class Name>,<Class Name 2>...}` | Restricts a recipe to certain classes |
| Permission | `permission{list="<perm1>,<perm2>...";display="...";hide=false}` | Only players with specific perms may use the recipe. `display` is how the condition looks like in the item lore |
| Placeholder | `placeholder{placeholder="<Placeholder>~<Comparator>~<Number>";display="...";hide=false}` | Check the placeholder of a Player, then compare it to a number of your choice. Comparator list: `<`, `<=`, `>`, `>=`, `==`, `!=`. Use `eq` or `neq` when comparing strings |
| Food | `food{amount=<amount>}` | The recipes consumes (and requires) X food. |
| Mana | `mana{amount=<amount>,format="0.#"}` | The recipe consumes (and requires) X mana. |
| Stamina | `stamina{amount=<amount>,format="0.#"}` | The recipe consumes (and requires) X stamina. |
| Money | `money{amount=<amount>,format="0.#"}` | The recipe costs (and requires) X Vault currency. |
| Min Profession Lvl. | `profession{profession=<profession>,level=<min>}` | Players must be Lvl X in a profession or higher (MMOCore). |

The `hide-when-locked` recipe option only triggers when at least one of the conditions is/are not met. The recipe will still display in the GUI if the player does not have all the required ingredients. Recipe conditions display at the beginning of the GUI recipe item lore:\
![](https://i.imgur.com/xPwlm5B.png)