`restrictions.yml` is where you setup what tools can mine what type of blocks.

This is a very useful feature when utilizing the MMOCore [Mining & Block Regen system](/phoenix-dvpmt/mmocore/-/wikis/Mining%20and%20Block%20Regen) to<span dir=""> </span>further customize and balance your tools.

## Breakdown

By default, the config is setup only for mining and has all of the pickaxes included. You **CAN** add axes, shovels, and even other materials (not just tools) to this list and give them their own restrictions.

The options are very simple as well. You start by choosing the tool, then specify the list of all the [block types](Mining-and-Block-Regen#target-block) this tool can break. This feature works like a whitelist: any block that is not in the list, cannot be broken by the given tool. For extra compatibility, we have broken blocks into block types, like vanilla blocks, blocks from MMOItems, and even custom skulls!

### Default permission set

The `default` option can be used to setup default break permissions. If a player happens to hold an item which has NO setup in this config file, this permission set will be used by default. It makes sense to just use `AIR` as default because it's what any player can mine when not holding a special tool.

### Inheritance

The `parent` option is used when your tools are tiering up, and you want the stronger tools to automatically inherit all of the blocks from the tools under it. This is a very handy organizational feature. If you leave it empty, it will automatically take the `default` permission set as parent.

```yaml
TOOL?DIAMOND_PICKAXE:
    parent: DIAMOND_PICKAXE
    can-mine:
    - ...
```

## Default configuration

```yaml
# The corresponding tool. It's CASE_SENSITIVE!
WOODEN_PICKAXE:
    parent: AIR

    # What the tool can mine.
    can-mine:
    - vanilla{type=COAL_ORE}

# You can also use MMOItems specifically TYPE?ID
TOOL?STONE_PICKAXE:

    # What the tool can mine.
    can-mine:
    - vanilla{type=COAL_ORE}

STONE_PICKAXE:
    can-mine:
    - vanilla{type=IRON_ORE}
    # MMOItems custom blocks with ID 1
    - mmoitems{id=1}
    
    # The block break permissions the tool inherits.
    # e.g a stone pickaxe can mine iron ores PLUS
    # any block that the wooden pickaxe can mine.
    # Used to make the config much clearer.
    parent: WOODEN_PICKAXE

IRON_PICKAXE:
    parent: STONE_PICKAXE
    can-mine:
    - vanilla{type=GOLD_ORE}
    # Custom skull with diamond ore texture
    - skull{value="eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvY2EzYmI4NWRlYzEzMjlmZTgyOWNjNmNkY2QzNGUxYmQ2MGVlODMyZjU3MjYyOTY1MWYxNGI1ZTE0NTU1ZGJiMSJ9fX0="}

GOLDEN_PICKAXE:
    parent: IRON_PICKAXE
    can-mine:
    - vanilla{type=LAPIS_ORE}

DIAMOND_PICKAXE:
    parent: GOLDEN_PICKAXE
    can-mine:
    - vanilla{type=DIAMOND_ORE}
    - vanilla{type=EMERALD_ORE}
    - vanilla{type=REDSTONE_ORE}

# Default permission set
AIR:
    default: true
    can-mine:
    - vanilla{type=OAK_LOG}
    - vanilla{type=SPRUCE_LOG}
```