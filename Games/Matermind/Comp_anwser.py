import random

#####################################################
#       Set up variables                            #
#####################################################
remaing_moves = 0
selection = []
howyoudid = ['NA','NA','NA','NA']
playerguess = ['NA','NA','NA','NA']
Won = 0
Turns = 0
check = 0

#####################################################
#       Functions for the code                      #
#####################################################


def Generate(selectionlen):
    """[summary]

    Args:
        selectionlen ([type]): [description]

    Returns:
        [type]: [description]
    """
    colour = 'rgboy'
    selection =[]
    print("Generate colours")
    for i in range(selectionlen):
        selection += random.choice(colour)
    return selection

def UserGuess(selectionlen):
    """[summary]

    Args:
        selectionlen ([type]): [description]

    Returns:
        [type]: [description]
    """
    print("User choice FUNCTION:")
    position = 0
    while position < selectionlen:
        print("Enter your choice for possition ", position)
        playerguess[position] = (input() )
        position += 1
    return playerguess


def Check_Guess(Guess): # I dont like what I have done here, I want to change this to something else...maybe I could use a slice on the array?
    """[check the users guess again the computers generated anwser
        Need to improve since this will only work with a fixed input]

    Args:
        Guess ([type]): [description]

    Returns:
        [type]: [description]
    """
    check = 0
    while check < len(Guess):
        if Guess[check] == selection[check]:
            howyoudid[check] = 'Correct'
            #return Won + 1
        elif (Guess[check] == selection[0]) or (Guess[check] == selection[1]) or (Guess[check] == selection[2]) or  (Guess[check] == selection[3]) :
            howyoudid[check] = 'Wrong Place'
        else:
            howyoudid[check] = 'NO'
        check += 1
    print("Out of loop")
   



def save():
    """Save user guess and the result of the check to help the user on there next choice.
    """

def guess_correct(howyoudid):
    """[summary]

    Args:
        howyoudid ([type]): [description]
    """
    #choice is the variable for how many items to guess, so i need to make this dynamicly size

    check = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',]
    loop = 0
    while loop < choice:
        check[loop] = 'Correct'
        loop += 1
    result = check[0:loop]
    if howyoudid[:] == result:
        return Won == 1 
    else :
        return        
#####################################################
#       Thsi is the start of the Game               #
#####################################################
choice = int(input("length of choice question?"))
choice2 = choice
remaing_moves = int(input("how many moves do you want??"))
selection = Generate(choice)    #Computers generated string
#remaing_moves -= 1


while True:
    print(selection)
    UserGuess(choice)
    result = Check_Guess(playerguess)
    print("Result", result )
    print("Won", Won)
 #   Turn_counter()
    remaing_moves -= 1
    print("    remaing_moves",     remaing_moves)
    print(Turns)
    guess_correct(howyoudid)
    print("End of loop starting again")

    if remaing_moves == 0:
        print("Out of moves")
        print("Thanks for playing")
        break

    if Won == 1:
        print("You Won the Game Congratulations!!!")
        print("Thanks for playing")
        break



#####################################################
#       Old code that was removed                   #
#####################################################
#def Turn_counter():
#    """Provides count down for moves
#    """
#    if remaing_moves <= 0:
#        Turns == 1
#        print("END OF MOVES")
#        return Turns
#    else:
#        return remaing_moves
#
#
#
#
#
#
#
#
#####################################################
#       Old code that was removed                   #
#####################################################
