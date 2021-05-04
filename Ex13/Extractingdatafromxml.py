import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET   # BUILT IN XML PARSER    XML always has
                                                         #single outer tag
init_input = input('Enter URL here:')

url = urllib.request.urlopen(init_input)
data = url.read()

tree = ET.fromstring(data)

total = 0
counts = tree.findall('comments/comment')
for item in counts:
    total = total + int((item.find('count').text))
print(total)
