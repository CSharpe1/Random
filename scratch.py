choice = 4 #choice for how many colours to guess...
count = 0

result = ['Correct', 'Correct', 'Correct', 'Correct']

print(result[:choice])

test = ['Correct', 'Correct', 'Correct', 'Correct']

if result[:] == test:
    print("Correct")
else :
    print("BAD")

check = ['','','','','','','','','']

#check = 'Correct' * choice
loop = 0
while loop < choice:
    check[loop] = 'Correct'
    loop += 1
    print(loop)
    print(choice)
result = check[0:loop]
print(check)
print(result)