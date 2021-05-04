#This program counts the distribution of the hour of the day of each message.
#You can pull the hour from the 'From' line by finding the time string and then
#spliting the string into parts using the colon character. Once you have
#accumulated the counts for each hour, print out the counts, one per line,
#sorted by hour.

fname = input('Enter file name: ')   #use mbox.txt
hours = {}
try:
    fhandle = open(fname)
except:
    fname = input('Enter file name: ')
for line in fhandle:
    if line.startswith('From '):
        time = line.split()[5]
        hour = time.split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1

lst = list(hours.items())   # much shorter than iterating like below:
#for key, value in hours.items():
#    lst.append((key, value))  #turns the dict into a list of key value pairs
#    lst.sort()
lst.sort()
for t in lst:
    print(t[0], t[1])
#print(lst)
