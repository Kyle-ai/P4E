#Figure out which line in the program is not properly gaurded. See if you can
#construct a text file which causes the program to fail and then modify the
#program so that the line is proeprly gaurded and test it to make sure it
#handles the text file.
#try:
#    fhand = open('mbox.xt')    #Original code, the problem is when a user
#except:                         #inputs a incorect file name so protect the
#    print('Please enter the correct file name')   #fhand expression
#    continue
#count = 0
#for line in fhand:
#    words = line.split()
    #print('Debug:', words)
#    if len(words) == 0: continue
#    if words[0] != 'From' : continue
#    print(words[2])


try:
    fhand = open('mbox.xt')
    count = 0
    for line in fhand:
        words = line.split()
        #print('Debug:', words)
        if len(words) == 0: continue
        if words[0] != 'From' : continue
        print(words[2])
except:
    print('Please enter the correct file name')
