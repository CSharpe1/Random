import random

colour = 'RGBOY'
selection = []
userselection = []
guess = 0
guesscount = 1

selectionlen = 4

for i in range(selectionlen):
    selection += random.choice(colour)

print(selection)
userselection = input("what is your guess")
print(userselection)



#while (guesscount <= 200) or (guess == 1):
#    print("What is your guess") 
#    print(guesscount)
#    print("Guess", guess)
#    guesscount +=   1
 #   if guesscount == 5:
 #       guess = 1
 #   else:
 #       print("Nothing")       