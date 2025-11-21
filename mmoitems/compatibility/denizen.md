---
order: 10
---

# 📝 Denizen

::: warning
This feature was experimental and is no longer available.

:::

## Getting a MI item
First you will have to retrieve the item template using `<mmoitem_template[type=SWORD>;id=KATANA]>`, which returns an MMOItemTemplateTag. Then you will have to generate the item using the `<templateTag.generate[]>` subtag.

The following example will generate an item with a random level and tier. If you don't specify any tier, it will be chosen randomly, based on the chances you chose when setting up the tier [item generator options](../features/tiers.md#modifier-capacity-item-generation).\
`<mmoitemTemplateTag.generate[]>`

The following example will generate an item with a specific level, and tier.\
`<mmoitemTemplateTag.generate[level=10;tier=RARE]>`

The following example will generate an item, which level will scale with the target player's level. The target player is a PlayerTag and must be passed in the tag context. If you don't specify an item level, MMOItems will take a completely random level unless you enable the `match-level` option.\
`<mmoitemTemplateTag.generate[player=SomePlayerTag;match-level=TRUE]>`

## New properties for ItemTags
Using the following tag you can check if an item is an MMOItem or not\
`<itemTag.is_mmoitem>`

Using the following tag, you can check if an item is unidentified\
`<itemTag.is_unidentified>`

Using the following tag, you can generate the identified version of an item, after making sure it is unidentified\
`<itemTag.identify>`

In the following example, we are checking if a basic iron sword is an MMOItem, so this will always return false.\
`<item[DIAMOND_SWORD].is_mmoitem>`