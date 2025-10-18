Skill trees are a combination of nodes which can be unlocked/levelled-up using skill tree points. Levelling up a skill tree node can give stats or can run some triggers for the player. You can also reset the progress for a skill tree and gain the skill tree points spent for it by using a skill tree reallocation point.

<details>
<summary>Skill Tree Basic Config Example</summary>

```yaml
id: 'custom_combat'    # Unique Identifier for the Skill Tree
name: 'Combat'         # Name of the skill tree that will be displayed in the GUI
type: custom           # See below for explanations
item: GOLDEN_AXE       # The item representing the skill tree in the GUI.
custom-model-data: 0
max-points-spent: 20   # Maximum amount of points spent in that skill tree
lore:
   - '&6This skill tree is used for combat abilities!'

nodes:
  a1:
    name: 'Mana Regeneration'
    coordinates: -3,-2
    paths:
      a2: 
        path1: -2,-2
        path2: -1,-2

    max-level: 2
    is-root: true
    point-consumed: 1
    experience-table:
      first_table_item:
        level: 1
        triggers:
          - 'stat{stat="MANA_REGENERATION";amount=1;type="FLAT"}'
      second_table_item:
        level: 2
        triggers:
          - 'stat{stat="MANA_REGENERATION";amount=1;type="FLAT"}'
    lores:
      0:
        - "&eMana regen in pts/sec +1"
      1:
        - "&eMana regen in pts/sec +1"
      2:
        - "&eMana regen in pts/sec +1"

```
</details>

## Linking a skill tree to a class

Skill trees are class based which means that the skill trees you can see and your progress for them depends on your current [class](Player%20Classes). Each player can only progress in the skill trees linked to its current class. You can link skill trees to a class like this:

```yaml
# In the class config
skill-trees:
   - 'skill-tree-id1'
   - 'skill-tree-id2'
```

## Skill Tree Points

You can use the following command to give skill tree points to players. The `id` represents the identifier of the skill tree you want to give points to. These points will only be usable for the corresponding skill tree. If you want to give skill tree points usable for any skill tree, use the id `global`.
```
/mmocore admin skill-tree-points give <player> <number> <id>
```

One of the main ways you will be giving players skill tree points is through command triggers in experience tables. In the following example, a player will receive 1 skill tree point useable for the skill tree with ID `archerSkillTree` every time they level up.
```yaml
Archer_Exp_Table:
  Skill_trees:
    period: 1
    triggers:
    - 'command{format="mmocore admin skill-tree-points give %player% archerSkillTree"}'
```

You can also use the following command to give skill tree reallocation points to players.
```
/mmocore admin skill-tree-realloc-points give <player> <number>
```

## Max Points spent

This field corresponds to the maximum amount of points that you can spend in a skill tree. If you reach this amount, you won't be able to unlock / upgrade any node within that skill tree even if you still have some skill tree points left. If it isn't filled it will be set to infinity.

# Skill Tree Nodes

Skill tree nodes are what players unlock/level up with their skill tree points. A skill tree is comprised of multiple nodes that can be linked together or completely independent. The skill tree nodes are all listed in `nodes` in the yml.

### Node states

At any instant in time, any node in a skill tree is in one of the four following states:
- Unlocked (The node is at least at level 1 and is already unlocked)
- Locked (The node is not accessible to the player yet, but might be in the future)
- Fully Locked (The player made a branching choice, rendering this node inaccessible until a full skill tree reset)
- Unlockable (The node can be unlocked for X skill tree points)

You can modifiy the display name of each state in the `node-status` section in the `gui/skill-tree.yml` config file.

### Strong Parents

You can make it so that players cannot unlock a node unless they have unlocked/levelled-up other nodes that you have specified.

You need to have the required level for all the strong parents of a node to be able to unlock it. You can define all the strong parents of a node with the level required to unlock them in the skill tree yml.

```yaml
nodes:
  a1:
    name: 'Mana Regeneration'
    ...
    parents:
      strong:
        force: 2
        agility: 1
        wisdom: 3
```

In this example, in order to unlock this node, the player needs to have 2 levels in the `force` node, 1 level in the `agility` node and 3 levels in the `wisdom` node

### Soft Parents

Soft parents are like strong parents except you only need to unlock and level up one of the requirements rather than all of them to unlock the node.

```yaml
nodes:
  a1:
    name: 'Mana Regeneration'
    ...
    parents:
      soft:
        force: 3
        agility: 2   
```

In this example, the player can either have 3 levels in `force` or 2 levels in `agility` to unlock the node.

### Incompatible Parents

If one of the incompatible parents matches its level requirement, the node will be instantly marked as fully-locked and you won't be able to unlock it anymore.

```yaml
nodes:
  a1:
    name: '&6Extra Atk Damage'
    ...
    parents:
      # If wisdom is unlocked//agility goes to level 2, the node will be unreachable
      incompatible:
        wisdom: 1
        agility: 2   
```

### Coordinates

To be represented in the GUI, each skill tree node has unique coordinates defining where it will be displayed. The coordinates can be as big as you want (e.g x:15 y:0). You might have to move around in the GUI using the arrows to see the corresponding node.

```yaml
nodes:
  a1:
    name: '&6Extra Atk Damage'
    ...
    coordinates: 0,0
```

![Coordinates](uploads/d142d83dc3237858959ea87b2262b633/GGlEXK2.jpeg)
### Lore

The `lore` is displayed in the skill-tree GUI through the `{node-lore}` placeholder in `gui/skill-tree.yml`. If you want to fully customize the lore each node has, you can include in it all the placeholders that are used for the node item lore in `gui/skill-tree.yml` (`{current-level}`, `{current-state}`, `{max-level}`...).

### Root Nodes

Root nodes are the first nodes to be unlocked in a skill tree. To configure a root node, use the following syntax:
```yaml
nodes:
  a1:
    name: '&6Some Node'
    ...
    root: true # Here
```

A skill tree with no root node is - almost - useless as new players cannot unlock any node. However, you can have players unlock a specific non-root node using a command, giving them access to the rest of the tree. This can be a cool way to have some quest/event unlock a whole skill tree for players.

### Permission Required

The option `permission-required` mandates that the corresponding permission is required to unlock the skill tree node. If this option is left unfilled, there will be no restrictions on permission to advance and unlock the skill tree node.

### Maximum Children

Nodes work under a parent/children system. If the player has the proper parent nodes, then the children nodes will be unlocked. The `max-children` option allows you to limit the number of unlocked children a parent node can have. If the amount of unlocked children a parent node has exceeds `max-children` then the other children nodes will become locked from the parent nodes. For instance with :

```yaml
nodes:
  a1:
    name: '&6Resistance'
    ...
    max-children: 1
    parents:
      strong:
        wisdom: 1
        archery: 1
```

If you choose to unlock archery then wisdom will be fully locked because it will be locked from one of its strong parents.

With soft parent instead of strong parent the wisdom node could be unlockable if it has one of its other parent unlocked with a valid amount of children regarding its max-children parameter.

### Experience Tables

Each node has an experience table associated with it. More about Experience Tables [here](Experience%20Tables)

### Paths

The purpose of displaying paths and nodes in the GUI is solely for visual representation, allowing for the connection of two nodes. To connect the current node to a child node using a path, you must specify the ID of the node you wish to connect to and list all of the necessary paths to reach it.

A path can exist in three different states, which will modify its appearance. More information about these icons can be found [here](https://gitlab.com/phoenix-dvpmt/mmocore/-/wikis/Skill%20Trees#icons). A path is considered "unlocked" if both of the nodes it connects are also unlocked. If one of the two nodes is fully locked, the path is considered "fully-locked." Otherwise, the path is simply "locked."

```yaml
#Example
paths:
  # Node being linked
  a1:
    path1: '2,2' # Coordinates of the path
    path2: 2,1
  a2: {...}
```

### Display

The optional field `display` enables you to have a specific icon for the node depending on its state.

```yaml
#Example config
display:
    unlocked: 'WHITE_CONCRETE:0'
    unlockable: 'BLUE_CONCRETE:0'
    locked: 'GRAY_CONCRETE:0'
    fully-locked: 'BLACK_CONCRETE:0'
```

### Max Level

This is the maximum level you can reach for this skill tree node.

### Points Consumed

The optional field `point-consumed` lets you set the number of skill tree points required to upgrade this skill tree node. If not filled, leveling up the node will cost 1 skill tree point.

## Icons

You have the ability to fully customize the appearance of the skill tree graphical user interface (GUI) by creating different displays for each possible node or path configuration. To make these changes, you can modify the file located in `gui/skill-tree.yml`, which will automatically select the appropriate display for each node or path. This configuration can also be done in each skill-tree config in order to have different GUI display for each skill-tree. As stated above each node can have its own look by filling the display section for it.

Here is how the display will be chosen for a node / path:

- If it is a node and has a specific display corresponding to its state then this will be its display.
- Else if there is a display in the skill tree config it will take it.
- Else it will take the display specified in `gui/skill-tree.yml`.

Let's now dive in how the display section works in the skill-tree config and `gui/skill-tree.yml`:

The display of a node/ path depends on both its neighborhood and its state. You can for example define a display for each node in the unlocked state and with 2 path at its left and right by being in nodes.unlocked.right-left.

The process is exactly the same for paths with 4 possible state for each path:

- Unlocked if the 2 node it links are unlocked.
- Unlockable if one node is unlocked while the other is unlockable.
- Locked if one of the 2 nodes is locked.
- Fully locked if one of the 2 nodes is fully locked.

The neighborhood also impacts the display of a path. For instance, if a path has a branch that goes up and ones that goes right, it will take the item associated with "up," followed by "down-right," and finally "right." This is a symmetrical process, so if a path goes left and then down, it will look identical.

<!-- For example this path has 1 skill tree node at its left and one that is below him so it is a down-left path. -->

The same rule applies for nodes. For example, if a node is surrounded by four paths, it will display the "up-right-down-left" configuration. Alternatively, if a node has only three paths (up, left, and right), it will automatically select the "up-right-left" display.

Here is a full example to show what the display enables you to do:

<div>

![Skilltree](uploads/87cc7edc2f5af55cf0a3d642c8c82869/Skilltree_display-01.png)

</div>Here the nodes 1,3,5,7,9 are unlocked. This makes the display for paths 2,4,6,8 be unlocked as the 2 nodes each path is linking are unlocked. The node 11 is unlockable making the path 10 unlockable also. Finally 22,24,25 are fully locked making the corresponding path have the fully locked display. The rest corresponds to the locked state. Now regarding the direction, here is an extensive list of the directions and state of each node/path:

| No | Display Icon | No | Display Icon | No | Display Icon | No | Display Icon |
|----|--------------|----|--------------|----|--------------|----|--------------|
| 1 | unlocked:down | 8 | unlocked:right | 15 | locked:up | 22 | fully-locked:down-right |
| 2 | unlocked:up<br>(same as down as this is symetric) | 9 | unlocked:right-left | 16 | locked:down-left | 23 | fully-locked:right |
| 3 | unlocked:up-down | 10 | unlockable:right | 17 | locked:right-left | 24 | fully-locked:right-left |
| 4 | unlocked:up | 11 | unlockable: right-left | 18 | locked:right | 25 | fully-locked:left |
| 5 | unlocked:up-right | 12 | locked:up-left | 19 | locked:right-left | 26 | fully-locked:up |
| 6 | unlocked:right | 13 | locked:up | 20 | locked:right |  |  |
| 7 | unlocked:up-right-left | 14 | locked:up-down | 21 | locked:right |  |  |

```yaml
# Example config in skill-tree.yml or in skill-tree configs.
display:
  paths:
    unlocked:
      up: 'WHITE_DYE:0'
      up-right: 'WHITE_DYE:0'
      up-left: 'WHITE_DYE:0'
      down-right: 'WHITE_DYE:0'
      down-left: 'WHITE_DYE:0'
      right: 'WHITE_DYE:0'
      default: 'WHITE_DYE:0'
    locked: {...}
    unlockable: {...}
    fully-locked: {...}
  nodes:
    unlocked:
      up-right-down-left: 'WHITE_CONCRETE:0'
      up-right-down: 'WHITE_CONCRETE:0'
      up-right-left: 'WHITE_CONCRETE:0'
      up-down-left: 'WHITE_CONCRETE:0'
      down-right-left: 'WHITE_CONCRETE:0'
      up-right: 'WHITE_CONCRETE:0'
      up-down: 'WHITE_CONCRETE:0'
      up-left: 'WHITE_CONCRETE:0'
      down-right: 'WHITE_CONCRETE:0'
      down-left: 'WHITE_CONCRETE:0'
      right-left: 'WHITE_CONCRETE:0'
      right: 'WHITE_CONCRETE:0'
      left: 'WHITE_CONCRETE:0'
      up: 'WHITE_CONCRETE:0'
      down: 'WHITE_CONCRETE:0'
      no-path: 'WHITE_CONCRETE:0'
    locked: {...}
    unlockable: {...}
    fully-locked: {...}
```

## Skill Tree GUI

There is 2 possibilities to open a skill tree:

The first option is to use "/skilltrees," which will open the GUI using the `gui/skill-tree.yml` configuration file. It allows you to browse through each skill tree within the GUI. You can enable or disable this feature by modifying the `enable-global-skill-tree-gui` field in the `config.yml` file.

The second option is to use "/skilltrees " to open a specific skill tree without the ability to browse between skill trees. This will utilize the GUI configuration file from `gui/specific-skill-tree/specific-skill-tree-<skill-tree-id>.yml`. Make sure that your skill tree IDs follow the YAML format to avoid any issues. If no configuration is found, it will load the GUI from `gui/specific-skill-tree/specific-skill-tree-default.yml`. You can also toggle this feature on or off by modifying the `enable-specific-skill-tree-gui` field in the `config.yml` file.

## Skill Tree Types (MMOCore 1.21.1+)
There are currently two types of skill trees. Using some type or another does not add, nor remove any feature from your skill tree, it only makes it easier to setup skill trees in certains scenarios, since skill tree config files can quickly get big.

### Custom Skill Trees
If you don't specify the `type` option for a skill tree, it will be set to `CUSTOM` by default. When using 
a custom skill tree, you need to manually provide all relations between skill tree nodes, as well as the location of all the paths between the nodes. In order to create a custom skill tree, simply use the following syntax:
```yaml
id: 'sample_skill_ree'
name: '&6My Skill Tree'
type: CUSTOM # Here
...
```

MMOCore will automatically infer that skill tree nodes with NO parents whatsoever are root nodes.

### Proximity Skill trees
Proximity skill trees are a simplified version of custom skill trees where you sometimes don't need to provide parenting relations between the nodes. In order to create a proximity skill tree, change the `type` config option to `PROXIMITY` inside your skill tree config file.
```yaml
id: 'sample_skill_ree'
name: '&6My Skill Tree'
type: PROXIMITY # Here
...
```

Any two neighboring nodes are automatically marked as soft parents. In other words, leveling up any node automatically unlocks the neighboring nodes. Every skill tree node has four direct neighbors (up, down, left and right neighbor). Here are some examples (click to expand):
<details>
    <summary>These two nodes are parents as they are direct neighbors.</summary>

```yaml
nodes:
  a1:
    name: 'Cooldown Reduction I'
    ...
    coordinates: 2,1

  a2:
    name: 'Cooldown Reduction II'
    ...
    coordinates: 2,2
```
</details>

<details>
  <summary>These 2 nodes are NOT parents, as they are not direct neighbors.</summary>

```yaml
nodes:
  a1:
    name: 'Cooldown Reduction I'
    ...
    coordinates: 2,1

  a2:
    name: 'Cooldown Reduction II'
    ...
    coordinates: 2,4
```
</details>

When setting up a proximity skill tree, you can still make use of custom soft/hard/incompatible node parenting rules. Using a proximity skill tree simply gives you a skeleton for your skill tree and spares you a little of syntax.
<details>
<summary>Defining parents inside a proximity skill tree</summary>

```yaml
nodes:
  a1:
    name: 'Cooldown Reduction I'
    ...
    coordinates: 2,1

  a2:
    name: 'Cooldown Reduction II'
    coordinates: 2,4
    parents: # This still works
      hard:
        a1: 1
```
</details>

It is impossible for MMOCore to infer skill tree roots from a linked skill tree, because every non-isolated skill tree node has at least one parent/child node. For this reason, you need to specify at least one root node manually in your proximity skill tree! As a reminder, this is done using the following option:

```yaml
nodes:
  a1:
    name: '&6Some Node'
    root: true # This option
    ...
```