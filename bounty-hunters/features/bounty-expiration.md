---
order: 8
---

# ⌛ Bounty Expiration

You can choose to have bounties automatically removed if they have been inactive for a certain amount of time. An inactive bounty is a bounty that hasn't been updated (either claimed or increased) for a certain amount of time.

This can be toggled on in the `config.yml` file:

```yml
# Automatically remove bounties if they have been inactive for a long time.
# Time is the amount of time in hours before a bounty is considered
# inactive if it is not updated (either claimed or someone increases it).
# 720 hours = 30 days, 360 hours = 15 days are good values
# 
# Bounties are checked every 1min.
# Changing this option requires a reload.
inactive-bounty-removal:
  enabled: true
  time: 720
```