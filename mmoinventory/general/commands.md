# 💾 Commands

| Command | Description | 
|---------|-------|
| `/mmoinv reload` | Reload the plugin |
| `/mmoinv export-data` | Export player data from YAML flat storage to SQL database | 
| `/mmoinv open <inventory> <owner>` | Open a custom inventory to a player | 
| `/mmoinv open <inventory> <owner> <player> <can_edit>` | Open `owner`'s custom inventory to player `player`. `can_edit` can be set to `true` (permission to equip/unequip items) or `false` (cannot equip/unequip items) |
| `/mmoinv inspect <inventory> <owner>` | Inspect a player's custom inventory | 

The following aliases work for the main command: `/mmoinv`, `/rpginv`, `/rpginventory`. The main command requires the `mmoinventory.admin` permission.