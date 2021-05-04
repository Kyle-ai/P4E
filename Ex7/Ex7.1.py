#Write a file to read through a file and print the contents of the
#file(line by line) all in uppercase.
fname = open('mbox.txt')
for line in fname:
    line = line.strip()
    print(line.upper())
