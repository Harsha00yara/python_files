import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving',url)
xml=urllib.request.urlopen(url).read()
inp=ET.fromstring(xml)
counts =  inp.findall('.//count')
print ("Count: " + str(len(counts)))

accumulator = 0

for count in counts:
    accumulator += int(count.text)

print( "Sum:" + str(accumulator))
