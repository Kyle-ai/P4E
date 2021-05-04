
#Exercise 1: Write a program which repeatedly reads numbers until the user
#enters “done”. Once “done” is entered, print out the total, count, and average
#of the numbers. If the user enters anything other than a number, detect their
#mistake using try and except and print an error message and skip to the next
#number.
count = 0
lst = []
while True:
    userinput = input('')
    if userinput == 'done':
        break
    else:
        try:
            newinput = float(userinput)
        except:
            print("enter valid input")
        lst.append(newinput)
        continue
print(sum(lst))
