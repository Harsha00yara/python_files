name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d=dict()
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        line=line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(line,0)+1
b=list()
for k,v in d.items():
    new=(k,v)
    b.append(new)
b.sort()
for k,v in b:
    print(k,v)
