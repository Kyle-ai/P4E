#Add code to the above program(last exersise) to figure out who has the most
#messages in the file. After all the data has been read and the dictionary has
#been created, look thoguh the dictioinary using a maximum loop to find who
#has the most messages and print how many they have
fname = input('Enter file name: ')
emails = dict()
try:
    fhandle = open(fname)
except:
    print('Invalid file entered: ', fname)
for line in fhandle:
    if line.startswith('From '):
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1
max_num = 0
max_email = None
for key in emails:
    if emails[key] > max_num:
        max_email = key
        max_num = emails[key]
print(max_num, max_email)
#result = 5 cwen@iupui.edu
