class   RPGInfo():
    
    aurthor =   "Anonymous"
    
    def __init__(self, game_title):
        self.title = game_title
    
    def welcome(self):
        print("welcome to " + self.title)
    
    @staticmethod
    def info():
        print("Made using the OOP RPG Creator (c) me")
    
    @classmethod
    def credits(cls):
        print("Thank you for playing\n")
        print("Created by " +cls.author )