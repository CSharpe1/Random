class   Item():
    def __init__(self, item_name):        #, xdimension, ydimension, doors):          # constructor init = initialisation, self = This object 
        """[summary]

        Args:
            self ([type]): [description]
            xdimension ([type]): [description]
            ydimension ([type]): [description]
            doors ([type]): [description]
        """
        self.name           =   item_name    
        self.description    =   None        # none = start without a value
 #       self.linked_items   =   {}

    def set_description(self,   item_description):
        """[summary]

        Args:
            item_description ([type]): [description]
        """
        self.description    =   item_description
    
    def get_description(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return  self.description
    
    def describe(self):
        """[summary]
        """
        print(self.description)
    ####################################
    def set_name(self, item_name):
        """[summary]

        Args:
            item_name ([type]): [description]
        """
        self.name   =   item_name

    def get_name(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return  self.name
    
    def name_description(self):
        """[summary]
        """
        print(self.name)

    def describe(self):
        print("The [" + self.name + "] is here - " + self.description )
