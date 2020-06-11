score = input("Enter Score: ")
try:
    h=float(score)
except:
    print("enter a number")
    quit()
if  h>=0.0 and h<=1.0:
    if h>=0.9:
        print("A")
    elif h>=0.8:
        print("B")
    elif h>=0.7:
        print("C")
    elif h>=0.6:
        print("D")
    elif h<0.6:
        print("F")
else:
    print("Enter a valid no:")
