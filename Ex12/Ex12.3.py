#Use urllib to replicate the previous exersise of (1) retrieving the document
#from a URL, (2) displaying up to 3000 characters, and (3) counting the overall
#number of characters in the document.Dont worry about the headers for this
#exersise, simply show the first 3000 characters in the document contents.

import urllib.request   #test with: http://data.pr4e.org/romeo.txt *len(received) = 536
#try:
url = input('Enter URL: ')
data = urllib.request.urlopen(url).read()
data = data.decode()

print(data[:3000])
print(len(data))


#except:
#    print('Please enter in the proper format')
