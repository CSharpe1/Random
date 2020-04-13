# Generates a random password
# Ask user how long they want their password
# how many letters 
# how many numbers 
# Have a mix of upper and lowercase letters
# , as well as numbers and symbols. 
# The password should be a minimum of 6 characters long.
import random

number = '0123456789'
letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
special =  '''!"£$%^&*()_{+}@~:<>?,./;'#[]-=¬`'''
filler = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"£$%^&*()_{+}@~:<>?,./;'#[]-=¬`'''

length = int(input("Welcom to my password Gen\nHow long do you want this password to be?") )
print("Length",length)

while length < 6:
    length = int(input("To small to be secure, please chose a bigger number") )
    print("Length",length)

letters = int(input("How many leters do you want in your password") )
numbers = int(input("How many numbers do you want in your password") )
specials = int(input("How many special characters do you want in your password") )

#while (letters + numbers) > length:
#    print("Error, you have selected to many letters and numbers for your length of password")
#    choice = input(print("Do you want to increase the length of your Password\nY or N?"))
#    if choice == "Y":
#        length = int(input("please make your password larger than $s", (letters + numbers)) )
#    else:
#        print("Lets chose some new values")
        
print(letters + numbers + specials)

count = 1
selection = ''

for i in range(letters):
    selection += random.choice(letter)
for i in range(numbers):
    selection += random.choice(number)
for i in range(specials):
    selection += random.choice(special)
while len(selection) < length:
    selection += random.choice(filler)
print("Random selection", selection)