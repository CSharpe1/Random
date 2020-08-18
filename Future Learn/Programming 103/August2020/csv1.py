with open("Future Learn\Programming 103\August2020\\foods.csv","r") as f:
    data = f.read()
    print(data)

    name = "Les"
    food = "Lasagne"
    f = open("Future Learn\Programming 103\August2020\\foods.csv","a")
    f.write(name + "," + food + "\n")
    f.close()




#    import csv
#    with open('Future Learn\Programming 103\August2020\\foods.csv') as csvfile:
#        favourites = csv.reader(csvfile, delimiter=',')
#        for row in favourites:
#            print(row)

    import csv
    name = "Portia"
    food = "Steak"
    with open('Future Learn\Programming 103\August2020\\foods.csv', mode="a") as csvfile:
        favourites = csv.writer(csvfile, delimiter=',')
        favourites.writerow([name,food])

    import csv
    with open('Future Learn\Programming 103\August2020\\numbers.csv', newline= '') as csvfile:
        favourites = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        print(type(favourites))
        for row in favourites:
            print(type(row[0]), type(row[1]))








