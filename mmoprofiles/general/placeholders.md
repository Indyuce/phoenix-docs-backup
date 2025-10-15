# 🏷️ Placeholders

All placeholders automatically register on plugin load, also requiring **PlaceholderAPI** to work. You do not need to run any commands and/or download anything else to initialize the placeholders.

Note: You can access the PAPI placeholders from MVdWPlaceholderAPI using `{placeholderapi_mmoprofiles_...}`

## Main Placeholders

| **Placeholder** | **Description** |
|-----------------|-----------------|
| `%mmoprofiles_real_uuid%` | The official player's UUID (only has sense if proxy-based profiles are enabled) |
| `%mmoprofiles_current_profile_uuid%` | The UUID of the player's current profile. |
| `%mmoprofiles_current_profile_name%` | Returns the profile name of the player's current profile |
| `%mmoprofiles_current_profile_slot%` | Returns the slot (integer) corresponding to the current profile. |
| `%mmoprofiles_amount_profiles%` | The number of profiles the player registered. |
| `%mmoprofiles_profile_slots%` | The total number of profiles the player can register. |
| `%mmoprofiles_remaining_profile_slots%` | The remaining amount of profiles the player can register. |
| `%mmoprofiles_profile_name_{slot}%` | The name of the profile at slot {slot}. |

