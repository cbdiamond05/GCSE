import math
print ("----TURF CALCULATOR----")
def calculate(w,l,r):
    lawnArea=w*l
    bedArea=math.pi*r*r
    turf=lawnArea-bedArea
    print("You need",turf,"square metres of turf")
    return
width=int(input("Enter the width of the lawn: "))
length=int(input("Enter the length of the lawn: "))
radius=int(input("Enter the radius of the flower bed: "))
calculate(width,length,radius)
