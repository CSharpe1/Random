from room   import  Room
from item   import  Item
from character  import *


kitchen         =   Room("Kitchen")      #, 10, 30, 2)
ballroom        =   Room("Ballroom")
dining_hall     =   Room("Dining_hall")
basement        =   Room("Basement")

kitchen.set_description("A dank and dirty place, buzzing with flies!")
kitchen.set_name("The Kitchen")

ballroom.set_description("Tired and worn and wet, how many years has it been since it was last used?")
ballroom.set_name("The Ballroom")

dining_hall.set_description("Nothing remains in the empty husk")
dining_hall.set_name("The Dinning Hall")

basement.set_description("Clean, bright and warm, this is wrong...")
basement.set_name("The basemenat")

#################################
'''
kitchen.describe()
kitchen.name_description()
ballroom.describe()
ballroom.name_description()
dining_hall.describe()
dining_hall.name_description()
'''
#################################

####        Link Rooms      ####
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

basement.link_room(kitchen, "up")
kitchen.link_room(basement, "down")


###         Create enemy    ###
dave    =   Enemy("Dave","The caretaker","")
dave.set_conversation("You should never have come here hehehe")
dave.set_weakness("silver knife")
basement.set_character(dave)

####
'''
dining_hall.get_details()
kitchen.get_details()
ballroom.get_details()
beasement.get_details()
'''
####

# set up the different items
frying_pan         =   Item("Frying_Pan")      
sheet_music        =   Item("Sheet_Music")
silver_knife       =   Item("Silver_Knife")

frying_pan.set_description("What a strage Frying pan, it is obviosly very old and seen better days but somehow it is warm to the touch, as if its just been used")
frying_pan.set_name("Frying Pan")

sheet_music.set_description("So well used it almost feels like its not there, there is more than just music inscribed on here, but what is it?")
sheet_music.set_name("Sheet Music")

silver_knife.set_description("Tarnised, but still sharp, heavy and well balanced, is this really just a knfe for eating?")
silver_knife.set_name("Silver Knife")


current_room    =   kitchen

while True:
    print("\n")
    current_room.get_details()

    inhabitant  =   current_room.get_character()
    if inhabitant   is not None:
        inhabitant.describe()

    command         =   input(">")
    while command != ["north", "south", "east", "west", "up", "down", "fight", "exit"]:
        if command in ["north", "south", "east", "west", "up", "down"]:
            current_room = current_room.move(command)
        elif    command ==  "fight":
            fight_with = input()
            dave.fight(fight_with)
  #  elif command == "talk":
    # Add code here
        elif    command ==  "exit":
            exit()
        else:
            command         =   input("Inpuut not recognised, please use either\n "  '''"north", "south", "east", "west", "up", "down", "fight" or "exit" \n >"''')