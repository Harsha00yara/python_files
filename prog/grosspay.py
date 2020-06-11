hrs=input("enter hrs")
rate=input("enter rate")
try:
        h=float(hrs)
        r=float(rate)
except:
        print("Enter an int")
        quit()
if h<=40:
        print(h*r)
else:
        print(40*r +(h-40)*r*1.5)
