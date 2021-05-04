# Add an easter egg to your code!
fname = input('Enter file name: ')
if fname == 'break':
    print('Not Today!')
try:
    fhandle = open(fname)
    count = []
    for line in fhandle:
        line = line.rstrip()
        if line.startswith('X-DSPAM-Confidence'):
            apos = line.find(':')
            newpos = float(line[apos+1:])
            count.append(newpos)
    print(sum(count))
except:
    print('Please enter valid input')
