class   RPGInfo():
    """[infomation for game]
    """
    
    aurthor =   "Anonymous"
    
    def __init__(self, game_title):
        """[Title of game]

        Args:
            game_title ([string]): [retuns name of game from variable game title]
        """
        self.title = game_title
    
    def welcome(self):
        """wellcome message
        """
        print("welcome to " + self.title)
    
    @staticmethod
    def info():
        print("Made using the OOP RPG Creator (c) me")
    
    @classmethod
    def credits(cls):
        print("Thank you for playing\n")
        print("Created by " +cls.author )