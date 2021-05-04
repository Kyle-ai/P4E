#Write a program to read through the mail box data and whem you find a line
#that starts with 'From', you will split the line into words using the
#split function. We are interested in who sent the message, which is the
#second word of the From line.

fname = input("Enter file name:")
fhandle = open(fname)
senders = []
for line in fhandle:
    if line.startswith("From"):
        words = line.split()
        senders.append(words[1])
print(senders)
#Out puts a list of all the email adresses of the senders in the file.
