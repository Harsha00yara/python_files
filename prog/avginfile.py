# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
s=0
c=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    f=float(line[21:])
    s=s+f
    c=c+1
avg=s/c
print("Average spam confidence:",avg)
