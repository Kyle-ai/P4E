#Write a program to look for lines of the form: 'New Revision: 39772'
#Extract the number from each of the lines using a regular expression and
#the findall() method. Compute the average of the numbers and print out the
#average as a integer.

import re
fname = input("Enter user name:")
try:
    fhandle = open(fname)
except:
    print('Please enter valid file number')
lst = []
for line in fhandle:
    line = line.rstrip()
    x = re.findall('New\sRevision:\s(\d+)', line)
    if len(x) > 0:
        for num in x:
            num = float(num)
        lst.append(num)
print(sum(lst)/len(lst))
#result = 39756.92592592593
