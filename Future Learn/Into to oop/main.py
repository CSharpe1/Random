from room   import  *
from item   import  *
from character  import *
from rpginfo    import *

#############################################
#               Set up                      #
#############################################

abandoned_mansion   = RPGInfo("Abandoned Mansion")
abandoned_mansion.welcome()
RPGInfo.info()
RPGInfo.author  =   "ME"

actions         =   ["north", "south", "east", "west", "down", "up", "talk", "fight", "take", "search", "invertory","take", "leave","use", "exit" ]
directon        =   ["north", "south", "east", "west", "up", "down"]
inv =   ["STUFF"]

#   Rooms
kitchen         =   Room("Kitchen")     
ballroom        =   Room("Ballroom")
dining_hall     =   Room("Dining_hall")
basement        =   Room("Basement")
entrance        =   Room("Entrance")
down_hall       =   Room("Downstairs Hallway")
up_hall         =   Room("Upstairs Hallway")
masterbedroom   =   Room("Master Bedroom")
bedroom1        =   Room("Bedroom 1")
bathroom        =   Room("Bathroom")
toilet          =   Room("Toilet")
#   Items
frying_pan         =   Item("Frying_Pan")      
sheet_music        =   Item("Sheet_Music")
silver_knife       =   Item("Silver_Knife")
door_bell       =   Item("Door Bell")

###         Names               ###
#   Rooms 
kitchen.set_name("Kitchen")
ballroom.set_name("Ballroom")
basement.set_name("basemenat")
dining_hall.set_name("Dinning Hall")
entrance.set_name("Entrance")
down_hall.set_name("Down Stairs Hallway")
up_hall.set_name("Up stairs Hallway")
masterbedroom.set_name("Master Bedroom")
bedroom1.set_name("BedRoom 1")
bathroom.set_name("Bathroom")
toilet.set_name("Toilet")          
#   Items
frying_pan.set_name("Frying Pan")
sheet_music.set_name("Sheet Music")
silver_knife.set_name("Silver Knife")
door_bell.set_name("Door Bell")
###         Characters      ###
#Enemy    
dave    =   Enemy("Dave","The caretaker","")
dave.set_conversation("You should never have come here hehehe")
dave.set_weakness("silver knife")
basement.set_character(dave)

#Fairy 
fairy1  =   Fairy("Tele","The Transporter",  "covo")
fairy1.set_conversation("Where do you want to go I wonder?")
dining_hall.set_character(fairy1)

fairy2  =   Fairy("Wanda", "The Annoying",  "")
fairy2.set_conversation("Well hellllllooooooo...    ... ...\n If it isn't ...\nerm\n\n.\n..\n...\n ... ...\nwell come on now can't you see I can't workout what your called\nwhatever you took so long to tell me it doesn't matter anyway\njust be carful in here there is a caretaker around somewhere who haunts this place, i think he might be part warewolf...\nyou can leave now...\nGO")
entrance.set_character(fairy2)

###         Descriptions    ###
#   Rooms
kitchen.set_description("------------\nA dank and dirty place, buzzing with flies!\n------------")
ballroom.set_description("------------\nTired and worn and wet, how many years has it been since it was last used?\n------------")
dining_hall.set_description("------------\nNothing remains in the empty husk\n------------")
basement.set_description("------------\nClean, bright and warm, this is wrong...\n------------")
entrance.set_description("------------\nHard to imagen a time when anyone would have walk through this dark, dingy doorway...\n------------")
down_hall.set_description("------------\nHigh ceelings and multiple doors, where to start?\n------------")
up_hall.set_description("------------\nExposed floor boards and uneven footing is all that remains...\n------------")
masterbedroom.set_description("------------\nThe Master Beedrom...\n------------")   
bedroom1.set_description("------------\nBedroom...\n------------")        
bathroom.set_description("------------\nA bathroom that you feel dirter walking out than when you               entred\n------------")        
toilet.set_description("------------\nLets hope you dont need to use this...\n------------")          
#   Items

frying_pan.set_description("What a strage Frying pan, it is obviosly very old and seen better days but somehow it is warm to the touch, as if its just been used")
kitchen.set_item(frying_pan)
sheet_music.set_description("So well used it almost feels like its not there, there is more than just music inscribed on here, but what is it?")
ballroom.set_item(sheet_music)
silver_knife.set_description("Tarnised, but still sharp, heavy and well balanced, is this really just a knife for eating?")
dining_hall.set_item(silver_knife)
door_bell.set_description("Solid Iron and rusty")
entrance.set_item(door_bell)

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

kitchen.link_room(basement, "down")
basement.link_room(kitchen, "up")

dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

entrance.link_room(down_hall, "east")
down_hall.link_room(entrance, "west")

down_hall.link_room(dining_hall, "north")
dining_hall.link_room(down_hall, "south")

down_hall.link_room(kitchen, "south")
kitchen.link_room(dining_hall, "north")

down_hall.link_room(up_hall, "up")
up_hall.link_room(down_hall, "down")

down_hall.link_room(toilet, "west")
toilet.link_room(down_hall, "east")

up_hall.link_room(masterbedroom, "north")
masterbedroom.link_room(up_hall, "south")

up_hall.link_room(bedroom1, "south")
bedroom1.link_room(up_hall, "north")

up_hall.link_room(bathroom, "west")
bathroom.link_room(up_hall, "east")



def invertory(item):
    inv.append(item)
    print(item)
    return inv


######################################
##          Start of Game           ##
######################################

current_room    =   entrance

dead = False
while dead == False:
    current_room.get_details()
    inhabitant  =   current_room.get_character()
    item        =   current_room.get_item()
    if inhabitant   is not None:
        inhabitant.describe()

    command         =   input(">")
    if command !=   actions: 
        if command in directon:
            current_room = current_room.move(command)

        elif    command ==  "fight":
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                print("What will you fight with?")
                fight_with  =   input()
                if inhabitant.fight(fight_with) ==  True:
                    print("YOU WIN!")
                    current_room.set_character(None)
                else   :
                    print("YOU LOSE\nGAME OVER")
                    dead = True
            else    :
                print("No one to fight with.")

        elif    command ==  "talk":
            if inhabitant is not None:
                inhabitant.talk()
            else:
                print("no one here to talk with")

        elif    command ==  "search":
            print("starting the search in 3\n2\n1\nnow!!!!")
            if item   is not None:
                item.describe()
                command         =   input("What do you want to do?\n take, leave or use?\n>")
                if command  ==  "take":
                    print("You have taken")
                    invertory(item)
                elif command == "use":
                    print("You have used............")
                else:
                    print("you have left the item where it is")

        elif    command ==  "invertory":
            print("invertory contains ")
            print(inv)
            print("##################")
            

        elif    command ==  "exit":
            exit()
        else:
            command         =   input("Input not recognised \n>")
    else:
        command    =   input("Please choese an action;", actions)


RPGInfo.credits()