#Write a program to prompt for a file name, and then read through the file
#and look for lines in the form:  X-DSPAM-Confidence: 0.8475, Then print the
#sum of the average spam confidence.

fname = input('Enter file name: ')
fhandle = open(fname)
count = []
for line in fhandle:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        apos = line.find(':')
        newpos = float(line[apos+1:])
        count.append(newpos)
print(sum(count))
