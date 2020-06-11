import urllib.request,urllib.parse,urllib.error
import re
from bs4 import BeautifulSoup
url=input('Enter-')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('span')
x=list()
for tag in tags:
    line=re.findall('[0-9]+',str(tag))
    x=x+line
sum=0
count=0
for z in x:
    sum=sum+int(z)
    count=count+1
print('Count',count)
print('Sum',sum)
