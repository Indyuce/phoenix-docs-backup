---
order: 5
---

# 📮 Events

## BountyCreateEvent <Badge type="info" text="cancelable" />

This event is called when a bounty is about to be registered. A bounty can be created by a player using the `/bounty` command, by a command block or the console using the same command, or by the [auto bounty feature](../features/auto-bounties.md) which sets a bounty onto whoever kills a player illegally. `event#getCause()` returns the cause of the creation. Other plugins can use the `PLUGIN` event cause.

## BountyIncreaseEvent <Badge type="info" text="cancelable" />

This event is called when a bounty's reward increases, either because a player increased it manually using ``/bounty`` or because the auto-bounty increased a player's bounty. `event#getCause()` returns the cause of the increase. The amount of money added to the bounty can be edited using `event#setAdded(double)`.

## BountyExpireEvent <Badge type="info" text="cancelable" />

This event is called either when a bounty fully expires or if the total amount of the bounty drops. A bounty can decrease for several reasons: an admin running ``/bounty remove``, a player removing the bounty they created by right clicking the bounty item in the bounties list, or due to the bounty expiration system (if enabled).

This event is called when a bounty expires, either because of an admin running ``/bounty remove`` or due to a player removing the bounty he created by right clicking the bounty item in the bounties list. `event#getCause()` returns the cause of the expiration.

## BountyClaimEvent <Badge type="info" text="cancelable" />

This event is called when a player claims a bounty after killing the bounty target.

## HunterLevelUpEvent

Called when a player levels up by claiming a bounty (this event is always called after the claim event).

## HunterTargetEvent <Badge type="info" text="cancelable" />

Called when a player targets another player using the bounty list.