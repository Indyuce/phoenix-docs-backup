# Sword / Weapon Stat Examples


_If any are missing please ping me in the support discord._

```
WIKISWORD:  
  base:  
    material: NETHERITE_SWORD
```
> The material field is where you insert the Minecraft material type that you want the item to be, this  means it supports all valid Material Enums from your current MC version.
```  
    revision-id: 2
```
> The revision-id field defines what current "version" your item is. This is up to you to change at your will, and any items that players have that don't match the revision ID set in your editor will get updated to their most recent version upon interaction.
```
    durability: 100.0
```
> The durability field, despite being somewhat annoyingly named, is the old method of doing custom textures pre 1.14 custom model data. It sets the physical current durability of the item and does not affect actual max durability.
```
    custom-model-data: 5.0
```
> This field is self explanatory for custom model data.
```
    max-durability: 1000.0
```
> Max-durability is where you set the custom durability for this item.
```
    will-break: true
```
> Should this item break when it hits 0 custom durability, or simply become unusable?
```
    name: '&cThis is a test sword.'
```
> Display name for the item.
```
    lore:
    - reeee
    - fffffffff
```
> The lore for the item, given in a list. Supports color codes of course.
```
    custom-nbt:
    - NBT_TAG_KEY TAG_VALUE
```
> You can set arbitrary and custom NBT Tags here to support external plugins, or use Minecraft can-place system etc.
```
    lore-format: lore-format
```
> This is where you can input a custom lore-format file from the lore-formats folder so that different item types can have different formats. EXTREME CUSTOMIZATION.
```
    displayed-type: Fake Type Here
```
> Instead of displaying the items actual item type like SWORD you can put an arbitrary "Kings Sword" or whatever here.
```
    enchants:
      sharpness: 1.0
      mending: 2.0
```
> Indented list of enchantments to go on this item.
```
    hide-enchants: true
```
> Should the enchants be hidden just to make the item glow.
```
    permission:
    - useme.sword
```
> What permission do you need in order to use this item?
```
    item-particles:
      type: FIREFLIES
      particle: FLAME
      amount: 5.0
      radius: 1.4
      speed: 1.0
      rotation-speed: 2.0
      height: 2.0
```
> A list of item particles that can go on the item, all of the valid types are given with the list command in game and particles are all of minecrafts valid particle types. Different particles have different modifiers and there is no way to know which ones work unless you use the handy dandy in game editor.
```
    disable-interaction: true
```
> Should interactions be disabled with this item, like block placing.
```
    disable-crafting: true
```
> Should this item be able to be used in crafting recipes?
```
    disable-smelting: true
```
> Should this item be used in smelting?
```
    disable-smithing: true
```
> Should this item be usable in smithing?
```
    disable-enchanting: true
```
> Should this item be enchantable?
```
    disable-repairing: true
```
> Should this item be repairable / renameable?
```
    disable-attack-passive: true
```
> Should this items MMOItems Blunt/Slashing/Piercing attack passive effects be toggled off.
```
    required-level: 5.0
```
> Required level from compatible RPG plugin, or vanilla experience level.
```
    required-class:
    - ARCHER
```
> Required class from compatible RPG plugin.
```
    attack-damage: 10.0
```
> Set the weapons base attack damage when hitting, or arrow damage when shooting.
```
    attack-speed: 10.0
```
> Attack speed of item in attacks per second.
```
    critical-strike-chance: 5.0
```
> Chance for a critical strike to occur.
```
    critical-strike-power: 5.0
```
> Extra multiplier done by a crit, combines with the base from MythicLib config.yml
```
    block-power: 5.0
```
> The percent of damage that this item CAN block.
```
    block-rating: 5.0
```
> The chance for this to actually block, again, combines with the base from MythicLib config.yml
```
    block-cooldown-reduction: 5.0
```
> Extra reduction of block cooldown from the base in config.yml mythiclib.
```
    dodge-rating: 5.0
```
> The chance to completely dodge an attack.
```
    dodge-cooldown-reduction: 5.0
```
> Extra reduction of dodge cooldown from the base in config.yml mythiclib.
```
    parry-rating: 5.0
```
> The chance to parry an attack, this negates damage and knocks back attacker.
```
    parry-cooldown-reduction: 5.0
```
> Extra reduction of parry cooldown from the base in you know the drill.
```
    cooldown-reduction: 5.0
```
> Reduces cooldowns of item and player skills (%)
```
    mana-cost: 5.0
```
> Mana cost to use said item.
```
    stamina-cost: 5.0
```
> Stamina cost to use said item.
```
    pve-damage: 5.0
```
> Additional damage against non human entities in %
```
    pvp-damage: 5.0
```
> Additional damage against human entities in %
```
    weapon-damage: 5.0
```
> Additional base weapon damage in %
```
    skill-damage: 5.0
```
> Additional mmoitems ability damage in %
```
    projectile-damage: 5.0
```
> Additional Skill/Weapon projectile damage.
```
    magic-damage: 5.0
```
> Additional magic ability and staff damage in %
```
    physical-damage: 5.0
```
> Additional ability/weapon physical (melee) damage.
```
    defense: 100.0
```
> Defense given, formula is set in mythiclib config.yml
```
    damage-reduction: 5.0
```
> Overall damage reduction in %
```
    fall-damage-reduction: 5.0
```
> Fall damage reduction in %
```
    projectile-damage-reduction: 5.0
```
> Projectile damage reduction in %
```
    physical-damage-reduction: 5.0
```
> Physical (melee) damage reduction in %
```
    fire-damage-reduction: 5.0
```
> Fire damage reduction in %
```
    magic-damage-reduction: 5.0
```
> Potion damage reduction in %
```
    pve-damage-reduction: 5.0
```
> Damage taken only from mobs reduction in %.
```
    pvp-damage-reduction: 5.0
```
> PVP damage taken reduction in %.
```
    undead-damage: 5.0
```
> Increases damage to undead in %
```
    unbreakable: true
```
> Is the item unbreakable?
```
    tier: RARE
```
> Set the items tier.
```
    set: STARTER
```
> Set the items... set.
```
    armor: 5.0
```
> Set the items armor value, capped at 20 visually, 30 functionally.
```
    armor-toughness: 5.0
```
> Armor toughness vanilla attribute, this has some whack ass formula idk.
```
    max-health: 10.0
```
> Increase max health, additive.
```
    unstackable: true
```
> Should this item be stackable?
```
    max-mana: 20.0
```
> Increase mana, like max health.
```
    knockback-resistance: 0.7
```
> The chance to negate knockback, 0.7 is 70%
```
    movement-speed: 0.2
```
> Movement speed to add to player, vanilla is 0.1
```
    two-handed: true
```
> Should this item be two handed, aka you cant offhand something with it.
```
    equip-priority: 5.0
```
> New equip priority stat, detailed on a separate wiki page.
```
    perm-effects:
      POISON: 1.0
```
> Give effects to the holder. Why would you want poison 1? I don't know.
```
    granted-permissions:
    - tempperm.ree
```
> Give temporary permissions when holding/wearing.
```
    item-cooldown: 10.0
```
> This is in seconds and applies to consumables and item commands.
```
    crafting:
      shaped:
        '1':
        - diamond AIR AIR
        - AIR diamond AIR
        - AIR AIR netherite_block
      shapeless:
        '1':
        - AIR
        - AIR
        - AIR
        - AIR
        - nether_star
        - AIR
        - AIR
        - slime_ball
        - AIR
      furnace:
        '1':
          item: COAL
          time: 200
          experience: 10.0
      blast:
        '1':
          item: COAL
          time: 200
          experience: 10.0
      smoker:
        '1':
          item: COAL
          time: 200
          experience: 10.0
      campfire:
        '1':
          item: COD
          time: 100
          experience: 10.0
      smithing:
        '1':
          input1: DIAMOND_SWORD
          input2: DIAMOND
```
> All the crafting recipe types.
```
    craft-permission: youneedthis.tocraft
```
> Crafting permission, duh.
```
    crafted-amount: 10.0
```
> How many of this mmoitem should it craft.
```
    sounds:
      on-attack:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-pickup:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-consume:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-right-click:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-left-click:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-item-break:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-block-break:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-craft:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-placed:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
```
> Add custom sounds.
```
    element:
      fire:
        damage: 10.0
      earth:
        defense: 10.0
```
> Elemental damage/defense. This system is getting reworked.
```
    commands:
      cmd0:
        format: -d1 bc Hello, this is a test command.
        delay: 0.0
        op: true
      cmd1:
        format: -d1 bc Hello, this is a test command from console.
        delay: 0.0
        console: true
```
> Add commands to the item when right clicked.
```
    gem-sockets:
    - RED
    - GREEN
    - Poop
```
> add arbitrary gem sockets to match ur gems.
```
    repair-type: EXAMPLE_REPAIR_STAT
```
> This repair-type stat needs to match on the consumable that you're repairing with, or leave blank for blank to match all.
```
    ability:
      ability1:
        type: BLOODBATH
        mana: 3.0
        mode: RIGHT_CLICK
```
> This is ability format, much like particles, not typing all 90 out with possible modifiers. Use the GUI.
```
    upgrade:
      workbench: true
```
> Please see the wiki page on item upgrading and use the GUI to learn configuring this first. Too much toe explain here.
```
    health-regeneration: 10.0
```
> MMOCore health regeneration in %
```
    mana-regeneration: 10.0
```
> MMOCore mana regeneration in %
```
    max-stamina: 10.0
```
> MMOCore max stamina additive.
```
    stamina-regeneration: 10.0
```
> MMOCore stamina regeneration in %.
```
    additional-experience: 50.0
```
> Additional MMOCore experience in %.
```
    faction-damage-enemy: 50.0
```
> Set mythicmobs faction increases here.
```
    required-dexterity: 10.0
    required-strength: 10.0
```
> Required MMOCore attributes.
```
    profession-enchanting: 10.0
    profession-smithing: 10.0
    profession-mining: 10.0
```
>Required MMOCore professions.

**Extra Stats Added by Consumables**
```
WIKICONSUMABLE:
  base:
    material: APPLE
    disable-right-click-consume: true
```
> Should this consumable be eatable with right click?
```
    restore-health: 10.0
```
> How much health to restore on eating?
```
    restore-food: 10.0
```
> How much food to restore on eating.
```
    restore-saturation: 10.0
```
> How much saturation to restore on eating?
```
    restore-mana: 10.0
```
> How much mana to restore on eating?
```
    restore-stamina: 10.0
```
> How much stamina to restore on eating?
```
    can-identify: true
```
> Can this item be used to identify unidentified items.
```
    can-deconstruct: true
```
> Can this item be used to deconstruct other items.
```
    can-deskin: true
```
> Can this item remove the skin off an item.
```
    effects:
      REGENERATION:
        duration: 100.0
        amplifier: 1.0
```
> List of effects this gives when consumed.
```
    soulbinding-chance: 100.0
```
> chance to soulbind an item.
```
    soulbound-break-chance: 100.0
```
> Chance it breaks if it fails.
```
    soulbound-level: 1.0
```
> Level of soulbind to apply.
```
    item-cooldown: 5.0
```
> Cooldown when eating.
```
    vanilla-eating: true
```
> Vanilla eating animation? Only works on materials that can normally be eaten.
```
    inedible: true
```
> NOT EDIBLE
```
    max-consume: 5.0
```
> How many uses does the item have?
```
    repair: 100.0
```
> How much custom dura this item repair?
```
    repair-type: EXAMPLE_STAT
```
> Which items can this repair, the receiving item needs to have matching repair-type.

**Extra Stats Added by Bows**
```
ELF_KINGS_LOST_BOW:
  base:
    material: BOW
    name: '&aElf King''s Lost Bow'
    arrow-particles:
      particle: FLAME
      amount: 5
      offset: 1.0
      speed: 1.0
```
> Particles when flying through air.
```
    arrow-velocity: 100.0
```
> How far the bow can shoot.
```
    arrow-potion-effects:
      POISON:
        duration: 100.0
        amplifier: 1
```
> The potion effects the bow gives on hit.