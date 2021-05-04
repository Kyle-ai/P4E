#Write a program that reads through the words in a file and stores them
#as keyes in a dictionary. It doesnt matter what the values are. Then you can
#use the in oeprator as a fastvway to check wether a string is in the dictionary
fname = input('Enter file name: ')
newdict = dict()
try:
    fhandle = open(fname)
    for line in fhandle:
        words = line.split()
        for word in words:
            newdict[word] = word
    print('fair' in newdict)    #true
    print('kyle' in newdict)    #false

except:
    print('Invalid file entered: ', fname)
