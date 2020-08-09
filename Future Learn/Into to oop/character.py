class Character():
    
    # Create a character        # CONSTRUCTOR
    def __init__(self, char_name, char_description  , char_talk):
        """[summary]

        Args:
            char_name ([type]): [description]
            char_description ([type]): [description]
            char_talk ([type]): [description]
        """
        self.name = char_name
        self.description = char_description
        self.conversation = char_talk

    # Describe this character
    def describe(self):
        """[summary]
        """
        print( self.name + " is here!" )
        print( self.description )
    

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """[summary]

        Args:
            conversation ([type]): [description]
        """
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        """[summary]
        """
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        """[summary]

        Args:
            combat_item ([type]): [description]

        Returns:
            [type]: [description]
        """
        print(self.name + " doesn't want to fight with you")
        return True

###########################
class   Enemy(Character):
    """[summary]

    Args:
        Character ([type]): [description]
    """
    def __init__(self, char_name, char_description, char_talk):
        """[summary]

        Args:
            char_name ([type]): [description]
            char_description ([type]): [description]
            char_talk ([type]): [description]
        """
         # calls a method of the supper class here, Character class above
        super().__init__(char_name, char_description, char_talk)
        self.weakness       =   None
    
    def set_weakness(self, enemy_weakness):
        """[summary]

        Args:
            enemy_weakness ([type]): [description]
        """
        self.weakness = enemy_weakness

    def get_weakness(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return  self.weakness  

    def fight(self, combat_item):
        """[summary]

        Args:
            combat_item ([type]): [description]

        Returns:
            [type]: [description]
        """
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

#############################


class   Fairy(Character):
    """[summary]

    Args:
        Character ([type]): [description]
    """
    def __init__(self, char_name, char_description, char_talk):
        """[summary]

        Args:
            char_name ([type]): [description]
            char_description ([type]): [description]
            char_talk ([type]): [description]
        """
         # calls a method of the supper class here, Character class above
        super().__init__(char_name, char_description, char_talk)
    
    def teleport(self, room):
        """[summary]

        Args:
            room ([type]): [description]
        """
        print("Time to Teleport you toooooooo...............", room)
        current_room    =   room