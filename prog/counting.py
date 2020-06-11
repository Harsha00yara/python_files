name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
words = list()
for line in handle:
    if not line.startswith("From:") : continue
    line = line.split()
    words.append(line[1])

for word in words:
	counts[word] = counts.get(word, 0) + 1


bigw=None
bigc=None
for i,j in counts.items():
    if bigc is None or j>bigc:
        bigw=i
        bigc=j
print(bigw,bigc)
