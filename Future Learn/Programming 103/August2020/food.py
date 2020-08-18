f = open("Future Learn\Programming 103\August2020\\food.txt", "r") #r = read, a appends to file, w makes new file     #"w")

#data = f.read()
#print(data)

#for line in f:
#    print(line)


with open("Future Learn\Programming 103\August2020\\food.txt") as f:
    data = f.read()
    print(data)

f.close()