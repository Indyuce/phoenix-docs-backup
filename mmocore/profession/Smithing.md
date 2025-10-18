Smithing is a specific type of profession where players can earn EXP when repairing items using the vanilla anvil. The experience earned by the player depends on the item the player is repairing, and on the amount of durability the player is repairing.

The config file is pretty self explanatory: you can setup how much smithing experience you want the player to earn when repairing 100 durability points of a specific item using the vanilla anvil.

## smithing.yml
```
# Experience given by repairing 100
# durability points from a specific material.

# Warning, diamonds/iron ingots/<any material
# which repairs a specific type of tool> do
# not repair the same amount of durability!
repair-exp:

    # Swords
    DIAMOND_SWORD: 1.923 # Max durability: 1561
    GOLDEN_SWORD: 62.5 # Max durability: 32
    IRON_SWORD: 8 # Md: 250
    STONE_SWORD: 7.634 # Md: 131
    WOODEN_SWORD: 13.56 # Md: 59
    
    # Picks
    DIAMOND_PICKAXE: 1.923
    GOLDEN_PICKAXE: 62.5
    IRON_PICKAXE: 8
    STONE_PICKAXE: 7.634
    WOODEN_PICKAXE: 13.56
    
    # Add as many as you want: bows, shields..
```

## Note
All items do not have the same amount of maximum durability however repairing a tool in the anvil **always repairs 25% of that maximum amount!** This is why the experience values look a bit weird. When repairing a diamond pickaxe using a diamond in the anvil, you are repairing 25% of these 1561 durability points which is about 390 durability points corresponding to `390 / 100 * 1,923 = 7.6 EXP`.

When repairing a golden sword, you are only repairing 25% of 32 durability points i.e 8 durability points which represents `8 / 100 * 62.5 = 5 EXP`. Repairing a diamond sword using the vanilla anvil gives more experience that repairing a golden sword.