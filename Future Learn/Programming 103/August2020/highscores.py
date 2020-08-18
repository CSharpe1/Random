try:
    print("The 10 highest scores previously were")
    with open("Future Learn\Programming 103\August2020\\highscore.txt", "r") as f:
        highscore = f.read()
        print(highscore)
except FileNotFoundError:
    print("Creating a new highscore.txt file")
    f = open('Future Learn\Programming 103\August2020\\highscore.txt', 'w')
    f.write("0")
    f.close()
    highscore   =   0

while True:

    name = input("Player Name;")
    score = 0
    scores = []
    names = []

    with open("Future Learn\Programming 103\August2020\\highscore.txt", 'r') as file:
        for line in file:
            line = line.strip("\n")
            line = line.split(" ")
            names.append(line[0])
            scores.append(int(line[1]))

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



    position = 0
    for compare_score in scores:
        if score < compare_score:
            position = position + 1
    scores.insert(position, score)
    names.insert(position, name)
    response = input("Would you like to play again? (Y/N)")
   

    scores = scores[:3]
    names = names[:3]

    print("HIGHSCORES")
    with open("Future Learn\Programming 103\August2020\\highscore.txt", 'w') as file:
        for i in range(len(scores)):
            file.write(names[i] + " " + str(scores[i]) + "\n")
            print(names[i] + " " + str(scores[i]))
    if response == "N" or response == "n":
        exit()
    else:
        print("Alright")