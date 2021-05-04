#Write a simple program to simulate the operation of the grep command on unix.
#Ask the user to enter a regular expression and count the number of lines that
#matched the regular expression.
import re
fname = input('Enter file name: ')   #use mbox.txt
try:
    fhandle = open(fname)
except:
    print('Enter valid file name')
user_input = input('Enter reg exp: ')    # java$  (this regexp means lines that
count = 0                                         #end with java)
for line in fhandle:
    line = line.rstrip()
    find_all = re.search(user_input, line)
    if find_all != None:
        count +=1
print(count)
#result = 60
