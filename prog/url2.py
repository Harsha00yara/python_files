import urllib.request,urllib.parse,urllib.error
fh=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count=dict()
for line in fh:
    word=line.decode().split()
    for w in word:
        count[w]=count.get(w,0)+1
print(count)
