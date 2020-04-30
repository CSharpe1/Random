import random


def arrayfun(number):
    '''
    >>> arrayfun(4)
    [4, 1]
    >>> arrayfun(4)
    [4, 1, 2]

    >>> arrayfun(4)
    [4, 1, 2, 3]




    '''
    test = random.randrange(2,4)
    testarray = [number]
 #   print("Test Array", testarray)
    count = 1
    while (len(testarray)) < test:
        testarray.append(count)
       # print(testarray)
        count += 1
    return testarray


#arrayfun(4)

if __name__ == "__main__":
    import doctest
    doctest.testmod()