import random

remaing_moves = 0
selection = []
howyoudid = ['NA','NA','NA','NA']
playerguess = ['NA','NA','NA','NA']
Won = 0
Turns = False
check = 0

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
    print("User choice")
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
   

def Turn_counter():
    """Provides count down for moves
    """
    remaing_moves -= 1
    if remaing_moves == 0:
        Turns == True
        return Turns
    else:
        return remaing_moves

def Setup(rounds):
    """[How many turns to make the Game]

    Args:
        rounds ([int]): [How many turns should the game be?]
    """

def save():
    """Save user guess and the result of the check to help the user on there next choice.
    """

def guess_correct(howyoudid):
    """[summary]

    Args:
        howyoudid ([type]): [description]
    """

choice = int(input("length of choice question?"))
choice2 = choice
selection = Generate(choice)    #Computers generated string
print(selection)
UserGuess(choice)
result = Check_Guess(playerguess)
print("Result", result )
print("Won", Won)