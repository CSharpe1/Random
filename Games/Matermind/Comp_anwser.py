import random

#####################################################
#       Set up variables                            #
#####################################################
remaing_moves = 0
Won = 0
Turns = 0
check = 0

def array_setup(length):
    """[generates the different arrarys into a blank format of 'NA']
    """
    arraytest = []
    while len(arraytest) < (length):
        arraytest.append('NA')
    howyoudid   = arraytest
    playerguess = arraytest
    check       = arraytest 
    return howyoudid
    return playerguess
    return check

def Generate(selectionlen):
    """[summary]

    Args:
        selectionlen ([type]): [description]

    Returns:
        [type]: [description]
    """
    colour = 'rgboy'
    selection =[]
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
    print("How you did", howyoudid)
    return howyoudid




def guess_correct(howyoudid):
    """Check if the guess was correct
    Args:
        howyoudid ([type]): [description]
    """
    #choice is the variable for how many items to guess, so i need to make this dynamicly size
    check = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','',]
    loop = 0
    while loop < choice:
        check[loop] = 'Correct'
        loop += 1
    result = check[0:loop]
    if howyoudid[:] == result:
        return Won == 1 
    else :
        return        
<<<<<<< HEAD
=======


>>>>>>> 9a33a1bd1cce7cd4c30aa7cbe852707668d36fc9
#####################################################
#       Thsi is the start of the Game               #
#####################################################
choice = int(input("length of choice question?"))
choice2 = choice
remaing_moves = int(input("how many moves do you want??"))
selection = Generate(choice)    #Computers generated string
#remaing_moves -= 1
array_setup(choice)

while True:
    print(selection)
#    UserGuess(choice)
#######################
    print("Player Guess")
    playerguess = selection


#######################
    result = Check_Guess(playerguess)
    remaing_moves -= 1
    print("    remaing_moves",     remaing_moves)
    print(Turns)
    guess_correct(howyoudid)

    if remaing_moves == 0:
        print('''Out of moves \nThanks for playing''')
        break

    if Won == 1:
        print(''' You Won the Game Congratulations!!! \nThanks for playing''')
        break



