l=list()#taking words from files to a list and removing repetitive words
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line=line.rstrip()
    word=line.split()
    for element in word:
    	if element not in l:
        	l.append(element)
l.sort()
print(l)
