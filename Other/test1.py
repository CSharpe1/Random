
with open ("doctest.txt") as f:
    sequence = f.read().splitlines()
    for i in sequence:
        print(i)
