class   Room():
    def __init__(self, room_name):        #, xdimension, ydimension, doors):          # constructor init = initialisation, self = This object 
        self.name           =   room_name    
        self.description    =   None        # none = start without a value
 #       self.x              =   xdimension
  #      self.y              =   ydimension
   #     self.doors          =   doors
        self.linked_rooms   =   {}
        self.character      =   None

    def set_description(self,   room_description):
        self.description    =   room_description
    
    def get_description(self):
        return  self.description
    
    def describe(self):
        print(self.description)
    ####################################
    def set_name(self, room_name):
        self.name   =   room_name

    def get_name(self):
        return  self.name
    
    def set_character(self, new_character):
        self.character  =   new_character
    
    def get_character(self):
        return  self.character


    def name_description(self):
        print(self.name)


    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction]    =   room_to_link
#        print( self.name + " linked rooms :" + repr(self.linked_rooms) )


    def get_details(self):
    #   Print the name
        print( "Welcome to the " + self.get_name())
    #   Print the description
        print( self.get_description()   +   "\n")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return  self.linked_rooms[direction]
        else:
            print("you can't go that way")
            return  self