# 💸 Economy

MMOCore comes along with a RPG styled physical currency system which consists in two types of items: **bank notes** and **gold coins**. Gold coins are always worth 1 gold however bank notes can be worth anything. This currency system not only add some RPGs atmosphere to your server because they can be used to trade, but they can also be added to mob drop tables e.g using MythicMobs to make dropping gold easier.

## Deposit 

Players can deposit their physical bank notes and gold coins directly into their Vault account. This can be used for instance like a bank safe where you can free some inventory space and yet still be able to use your digital Vault cash with NPCs.\
You can force open the deposit GUI using `/deposit <player>` or simply ask players to use `/deposit` if they have the `mmocore.currency` permission. Using extra plugins, you can also bind this command to specific blocks on right-click, for e.g enderchests, or even bind this command to NPCs using Citizens addons to make a Vault keeper NPC.
![IDpIfft](uploads/d83ecd44c1b52a57a45fb22271904557/IDpIfft.gif)

## Withdraw

Withdrawing enables players to withdraw some Vault cash and get physical currencies for trading or in order to pay other players. You can start a withdraw request for a player using the `/withdraw <player>` command, or ask them to use `/withdraw` if they have the `mmocore.currency` permission.\
When a withdraw request is started, players are asked to type in the chat the amount they would like to withdraw. When withdrawing $54, players will receive 4 gold coins worth $1 each, and a $50 bank note: `withdraw = <gold-coins> * 1 + <bank-notes> * 10`.
![VNe2NPr](uploads/9592bd71a53c74d7eebe57f9313521eb/VNe2NPr.gif)