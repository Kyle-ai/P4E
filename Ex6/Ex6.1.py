# Write a While loop that starts in the last character of the string and works
#its way backwards to the first character in the string.Printing each letter of
index =''
string = 'kyle'
count = len(string)
while count > 0:
    index += string[count -1]
    count = count -1
    print(index)
