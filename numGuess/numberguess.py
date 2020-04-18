import random
size = int(input("What range of numbers do you want to guess?"))
check = random.randint(0, size)
guess = int(input("What is your guess?"))
while guess != check:
    if guess < check:
        print("To small try again!")
        guess = int(input("What is your guess?"))
    elif guess > check:
        print("To large, try again!")
        guess = int(input("What is your guess?"))
print("Correct your guess was ", guess)