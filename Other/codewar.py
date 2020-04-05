# replace string of letters with the equivilent numeric value
# e.g. 'a' = 1, 'b' = 2 etc.

sample = "The sunset sets at twelve o' clock."

count=0

for i in sample:
    print(ord(sample[count])-96)
    count += 1