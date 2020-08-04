from room   import  Room

kitchen         =   Room("Kitchen")      #, 10, 30, 2)
ballroom        =   Room("Ballroom")
dinning_hall    =   Room("Dinning_hall")

kitchen.set_description("A dank and dirty place, buzzing with flies!")
kitchen.get_description()
kitchen.set_name("The Kitchen")
kitchen.get_name()

ballroom.set_description("Tired and worn and wet, how many years has it been since it was last used?")
ballroom.get_description()
ballroom.set_name("The Ballroom")
ballroom.get_name()

dinning_hall.set_description("Nothing remains in the empty husk")
dinning_hall.get_description()
dinning_hall.set_name("The Dinning Hall")
dinning_hall.get_name()

#################################
kitchen.describe()
kitchen.name_description()
ballroom.describe()
ballroom.name_description()
dinning_hall.describe()
dinning_hall.name_description()
#################################

####        Link Rooms      ####
kitchen.link_room(dinning_hall, "south")



