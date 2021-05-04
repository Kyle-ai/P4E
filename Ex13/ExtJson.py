import urllib.request, urllib.parse, urllib.error
import json

init_url = input('Enter URL here:')
url = urllib.request.urlopen(init_url)
data = url.read()
#print(url)                     #json.loads is a json library(loadfromstring)

info = json.loads(data)
#print(info)
total = 0
for item in info['comments']:
    count = item['count']
    total = int(count) + total
print(total)
