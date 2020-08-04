class   Room():
    def __init__(self, room_name):        #, xdimension, ydimension, doors):          # constructor init = initialisation, self = This object 
        self.name           =   room_name    
        self.description    =   None        # none = start without a value
 #       self.x              =   xdimension
  #      self.y              =   ydimension
   #     self.doors          =   doors
        self.linked_rooms   =   {}

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
    
    def name_description(self):
        print(self.name)


    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction]    =   room_to_link
#        print( self.name + " linked rooms :" + repr(self.linked_rooms) )


