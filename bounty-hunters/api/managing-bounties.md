# 📜 Bounties

You may use the `BountyManager` class to register/unregister bounties or to simply check existing bounties. You can access the class instance using`BountyHunters.getInstance().getBountyManager()`
## Creating & registering a bounty
To create a bounty, you have to use the `Bounty` constructor.\
`Bounty bounty = new Bounty(creator, target, reward)`
* creator - OfflinePlayer
* target - OfflinePlayer
* reward - Double

To register the bounty, `bountyManager.registerBounty(bounty)`. It'll trigger the **BountyCreateEvent**. To unregister a bounty, you need to use `bountyManager.unregisterBounty(bounty)`. The _Bounty_ class no longer has any register or unregister methods to reduce confusion and potential data glitches.

These methods both reset the bounty hunters. That means players hunting the bounty target will stop their hunt.
## Getting the list of active bounties
Use `bountyManager.getBounties()` to get a collection of all active bounties. Bounties are stored in a linked hash map, therefore that collection is ordered. You may translate it to an array list using `new ArrayList<Bounty>(bountyManager.getBounties())`
## Getting a bounty
You can use `bountyManager.getBounty(OfflinePlayer)` to get the bounty on a player.\
You will first have to check if there is any bounty on the player using `bountyManager.hasBounty(OfflinePlayer)` as the `getBounty(OfflinePlayer)` method will throw a NPE error if the player does **not** have any bounty on him.
***