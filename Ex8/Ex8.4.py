#Write a program to open the file romeo.txt and read it line by line. For each
#line,split the line into a list of words using the split function. For each
#word,check to see if the words is already in a list. If the word
#is not in the list,.When the program completes, sort and print the
#resulting words in alphabetical order:
fname = input('Enter file name:')
fhandle = open(fname)
result = []
for line in fhandle:
    words = line.split()
    for word in words:
        if word in result:
            continue
        result.append(word)
print(sorted(result))
