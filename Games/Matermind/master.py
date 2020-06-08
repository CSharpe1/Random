import random

colour = 'BW'
playerguess = ['NA','NA','NA','NA']
position = 0
computerguess = []
length = 4
howyoudid = ['NA','NA','NA','NA']
check = 0
correct = 0

##########################

for i in range(length):
    computerguess += random.choice(colour)
print(computerguess)


while correct != 1:
######################
    while position < length:
        playerguess[position] = (input("Enter your choice for possition ") )
        position += 1
####################
    print(playerguess)  

    while check < len(playerguess):
        if playerguess[check] == computerguess[check]:
            howyoudid[check] = 'Correct'
        elif (playerguess[check] == computerguess[0]) or (playerguess[check] == computerguess[1]) or (playerguess[check] == computerguess[2]) or (playerguess[check] == computerguess[3]) :
            howyoudid[check] = 'Wrong Place'
        else:
            howyoudid[check] = 'NO'
        check += 1
#    print(howyoudid)
    length = 0
    print("Your last guess;", playerguess)
    print("How you did;", howyoudid)

    if (howyoudid[0] == 'Correct') and (howyoudid[1] == 'Correct') and (howyoudid[2] == 'Correct') and (howyoudid[3] == 'Correct'):
        correct += 1
    else :
        length = 0

print("Congratulations you have won this game")
