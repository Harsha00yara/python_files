import json
import urllib.request,urllib.parse,urllib.error
url=input('Enter location:')
hm=urllib.request.urlopen(url).read()
print('Retrieving',url)
new=json.loads(hm)
sum=0
print('Retrieved',len(hm),'characters')
for i in new['comments']:
    sum=sum+int(i['count'])
print(sum)
