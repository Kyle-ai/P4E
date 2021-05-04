    #Enter a number: 4
    #Enter a number: 5
    #Enter a number: bad data
    #Invalid input
    #Enter a number: 7
    #Enter a number: done
    #16 2 5.3333333

#Write another program that prompts for a list of numbers as above and at the
#end prints out both the maximum and the miniumum of the numbers instead of a
#average.
lst = []
while True:
    userinput = input('')
    if userinput == 'done':
        break
    else:
        newuser = float(userinput)
        lst.append(newuser)
print(max(lst),min(lst))
