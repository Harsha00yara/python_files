fname = input("Enter file name: ")
fh = open(fname)
count = 0
for lines in fh:
    lines=lines.rstrip()
    if lines.startswith('From:'):
        d=lines.split()
        print(d[1])
        count=count+1
print("There were", count, "lines in the file with From as the first word")
