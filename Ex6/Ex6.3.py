#The following program counts the number of times 'a' appears in a string.
#word = 'bananas'
#count = 0
#for letter in word:
#    if letter == 'a':
#        count = count + 1
#    print(count)
#Encapsulate this code in a function named count, and generalize it so that it
#accepts the string and the letter as arguments .

def count(string,par2):
    count = 0
    for letter in string:
        if letter == par2:
            count += 1
    print(count)

count('kylekylekyle','k')
