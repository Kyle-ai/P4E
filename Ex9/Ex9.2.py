# Write a program that catagorizes each mail message by day of the week the
#commit was done. To do this look for lines that start with 'From',then look for
#the third word and keep a running count of each of the days of the week. At the
#end of the program print out the contents of your dictionary
#(order does not matter). Use mbox.txt.

fname = input('Enter file name: ')
days = dict()
try:
    fhandle = open(fname)
    for line in fhandle:
        if line.startswith('From '):
            word = line.split()[2]
            days[word] = days.get(word, 0) + 1
    print(days) #{'Sat': 1, 'Fri': 20, 'Thu': 6} is the result


except:
    print('Invalid file entered: ', fname)
