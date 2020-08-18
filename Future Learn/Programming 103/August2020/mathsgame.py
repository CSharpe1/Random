try:
    with open("Future Learn\Programming 103\August2020\\highscore.txt", "r") as f:
        highscore = f.read()
        highscore = int(highscore)
        print("The highest score previously was ")
        print(highscore)
except FileNotFoundError:
    print("Creating a new highscore.txt file")
    f = open("Future Learn\Programming 103\August2020\\highscore.txt", "w")
    f.write("0")
    f.close()
    highscore = 0





while True:
    score = 0




    print("Welcome to the Maths Quiz")
    print("Can you answer three questions and score maximum points?")
    print("Question 1: What is the product of 2x2x2?")


    answer = int(input("Your answer :>> "))

    if answer == 8:
        print("Correct")
        score = score + 1
        print("Your score is ", score)
    else:
        print("Incorrect, the answer is 8")
        print("Your score is ", score)

    print("Question 2: What is the product of 1x2?")


    answer = int(input("Your answer :>> "))

    if answer == 2:
        print("Correct")
        score = score + 1
        print("Your score is ", score)
    else:
        print("Incorrect, the answer is 2")
        print("Your score is ", score)


    print("Question 3: What is the product of 200x2?")


    answer = int(input("Your answer :>> "))

    if answer == 400:
        print("Correct")
        score = score + 1
        print("Your score is ", score)
    else:
        print("Incorrect, the answer is 400")
        print("Your score is ", score)



    if score >= highscore:
        highscore = score
        print("You have set a new highscore")
        with open("Future Learn\Programming 103\August2020\\highscore.txt", "w") as f:
            f.write(str(highscore))
    else:
        print("Better luck next time")