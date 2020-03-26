search = int(input("What is the input number;"))

while int(search) > 31:
    print("Your number is to large!")
    search = input("What is the input number;")
binary = bin(int(search))
for binary2 in binary:
    binary2 = binary[2:]
    #pack out to 5 binary levels
while len(binary2) < 5:
    binary2 = ('0' + (binary2))



E   =   int(binary2[0])
D   =   int(binary2[1])
C   =   int(binary2[2])
B   =   int(binary2[3])
A   =   int(binary2[4])

print(binary2)

if E == 1:
    print("E")
if D == 1:
    print("D")
if C == 1:
    print("C")
if B == 1:
    print("B")
if A == 1:
    print("A")