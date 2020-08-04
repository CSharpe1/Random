class   Item():
    def __init__(self, item_name):        #, xdimension, ydimension, doors):          # constructor init = initialisation, self = This object 
        self.name           =   item_name    
        self.description    =   None        # none = start without a value
        self.linked_items   =   {}

    def set_description(self,   item_description):
        self.description    =   item_description
    
    def get_description(self):
        return  self.description
    
    def describe(self):
        print(self.description)
    ####################################
    def set_name(self, item_name):
        self.name   =   item_name

    def get_name(self):
        return  self.name
    
    def name_description(self):
        print(self.name)

