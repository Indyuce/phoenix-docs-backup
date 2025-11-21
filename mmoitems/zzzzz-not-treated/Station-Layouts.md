Layouts determine how your crafting stations look and function by creating the gui. Your layouts will reload whenever you restart the plugin or run the following command: **/mi reload stations**.
## Creating Layouts
Whenever your crafting stations are generated they will all use the default layout. Every YML file in that folder corresponds to a layout, therefore you can create a layout by creating a new YML file. Be careful when choosing the file name, because it corresponds to the ID you will be using as reference when creating the station. These are the automatically generated templates:
![auto templates files](https://i.imgur.com/N3D5bqh.png)
## Using Layouts
This is an example of a crafting stations settings. Under the layout node you can put the id the layout you want to use.
```
# Name which will be displayed
# when opening the station
name: 'Example Crafting Station (#page#/#max#)'

# The maximum amount of items in the crafting queue ie. the
# max number of items players are able to craft simultaneously.
# Must be between 1 and 64.
max-queue-size: 10

# The sound that plays whenever an action is
# completed in the crafting station.
# GET SOUND NAMES HERE:
# https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
sound: ENTITY_EXPERIENCE_ORB_PICKUP

# This is how the gui looks. You can define your own
# in crafting-stations/layouts by creating a new
# file with the name of the file as the id.
layout: expanded
```
## Default Layout
```
# The size of the gui. Must be
# between 9 and 54 and must be a multiple of 9.
slots: 54

layout:

  # The slots that display the station's recipes.
  recipe-slots: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23]

  # The slots that display the station's queue slots.
  queue-slots: [38, 39, 40, 41, 42]

  # The slots that display the arrows to navigate
  # the station's recipes.
  # Only shows when it can be used.
  recipe-previous-slot: 20

  recipe-next-slot: 24

  # The slots that display the arrows to navigate
  # the station's queue.
  # Only shows when it can be used.
  queue-previous-slot: 37

  queue-next-slot: 43
```