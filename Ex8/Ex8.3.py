# Rewrite the gaurdian code in the previous example without two if statments
#Instead, use a compound logical expression using the or logical operator
#with a single if statment

#try:
#    fhand = open('mbox.xt')
#    count = 0
#    for line in fhand:          #ORIGINAL CODE
#        words = line.split()
#        #print('Debug:', words)
#        if len(words) == 0: continue
#        if words[0] != 'From' : continue
#        print(words[2])
#except:
#    print('Please enter the correct file name')

try:
    fhand = open('mbox.t')
    count = 0
    for line in fhand:
        words = line.split()
        #print('Debug:', words)
        if len(words) == 0 or words[0] != 'From': continue
        print(words[2])
except:
    print('Please enter the correct file name')
