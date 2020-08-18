f = open("Future Learn\Programming 103\August2020\\names.txt", "a") #a appends to file, w makes new file     #"w")

print(f)

name = input("Hello, what is your name? ")

print("Hello " + name)

f.write(name + "\n")

f.close()