#Write a program as follows: Read and parse the 'From' lines and pull out
#adresses from the line.Count the number of messages from each person using
#a dictionary. After all the data has been read, print the person
#with the most commits by creating a list of (count,email) tuples from the
#dictionary. Then sort the list in reverse order and print out the person who
#has the most commits.

fname = input('Enter file name: ')   #use mbox.txt
emails = {}
try:
    fhandle = open(fname)
except:
    fname = input('Enter file name: ')
for line in fhandle:
    if line.startswith('From '):
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1
lst = []
for key, value in emails.items():
    lst.append((value, key))  #turns the dict into a list of key value pairs
    lst.sort(reverse = True)
print(lst[0])
# result = (5, 'cwen@iupui.edu')
