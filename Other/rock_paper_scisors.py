import random
# 0 = rock
# 1 = paper
# 2 = sciscors

comp_guess = random.randint(0,2)
guess = int(input("0 = Rock\n1 = Paper\n2 = scisors\nWhat is your Choice?"))

# 0 beats 2
# 1 beats 0
# 2 beats 1
Comp_wins   = 0
Player_wins = 0
Draw        = 0
print("Comp Guess = ", comp_guess)
if comp_guess == guess:
    print("DRAW!")
    comp_guess = random.randint(0,2)
    guess = int(input("0 = Rock\n1 = Paper\n2 = scisors"))
    Draw += 1
elif (comp_guess == 0) and (guess == 2):
    print("Computer wins")
    Comp_wins += 1
elif (comp_guess == 1) and (guess == 0):
    print("Computer wins")
    Comp_wins += 1
elif (comp_guess == 2) and (guess == 1):
    print("Computer wins")
    Comp_wins += 1
else :
    print("Player wins")
    Player_wins += 1