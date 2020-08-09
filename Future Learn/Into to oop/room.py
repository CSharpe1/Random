class   Room():
    number_of_rooms =   0
       
        
    def __init__(self, room_name):        # constructor init = initialisation, self = This object 
        """[summary]

        Args:
            self ([type]): [description]
            xdimension ([type]): [description]
            ydimension ([type]): [description]
            doors ([type]): [description]
        """

        self.name           =   room_name    
        self.description    =   None        # none = start without a value
        self.linked_rooms   =   {}
        self.character      =   None
        Room.number_of_rooms    =   Room.number_of_rooms    +   1

'''
    def set_description(self,   room_description):
        """description of room

        Args:
            room_description ([type]): [description]
        """
        self.description    =   room_description
    
    def get_description(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return  self.description
'''    

#   converting these getter and setter into properties 







    def describe(self):
        """[summary]
        """
        print(self.description)
    ####################################
    def set_name(self, room_name):
        """[summary]

        Args:
            room_name ([type]): [description]
        """
        self.name   =   room_name

    def get_name(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return  self.name
    
    def set_character(self, new_character):
        """[summary]

        Args:
            new_character ([type]): [description]
        """
        self.character  =   new_character
    
    def get_character(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return  self.character


    def set_item(self, new_item):
        self.item  =   new_item
    
    def get_item(self):
        return  self.item



    def name_description(self):
        """[summary]
        """
        print(self.name)


    def link_room(self, room_to_link, direction):
        """[summary]

        Args:
            room_to_link ([type]): [description]
            direction ([type]): [description]
        """
        self.linked_rooms[direction]    =   room_to_link
#        print( self.name + " linked rooms :" + repr(self.linked_rooms) )


    def get_details(self):
        """[summary]

        Returns:
            [type]: [description]
        """
    #   Print the name
        print( "Welcome to the " + self.get_name())
    #   Print the description
        print( self.get_description()   +   "\n")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)

    def move(self, direction):
        """[summary]

        Args:
            direction ([type]): [description]

        Returns:
            [type]: [description]
        """
        if direction in self.linked_rooms:
            return  self.linked_rooms[direction]
        else:
            print("you can't go that way")
            return  self