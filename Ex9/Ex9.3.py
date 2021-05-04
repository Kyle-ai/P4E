# Write a program to read through a mail log, build a histogram using a
#dictionary to count how many messages have come from each email adress,
#and print the dictionary.
fname = input('Enter file name: ')
emails = dict()
try:
    fhandle = open(fname)
    for line in fhandle:
        if line.startswith('From '):
            email = line.split()[1]
            emails[email] = emails.get(email, 0) + 1
    print(emails)
#result = {'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3,
#'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5,
#'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1,
#'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1,
#'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}

except:
    print('Invalid file entered: ', fname)
