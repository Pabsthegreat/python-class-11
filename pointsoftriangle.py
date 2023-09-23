x1=float(input("Enter x coordinate of the first point="))
y1=float(input("Enter y coordinate of the first point="))
x2=float(input("Enter x coordinate of the second point="))
y2=float(input("Enter y coordinate of the second point="))
x3=float(input("Enter x coordinate of the third point="))
y3=float(input("Enter y coordinate of the third point="))
p1p2=(x2-x1)**2+(y2-y1)**2                             #using distance formula
p2p3=(x3-x2)**2+(y3-y2)**2
p3p1=(x1-x3)**2+(y1-y3)**2
import math
d1=math.sqrt(p1p2)                                           #using inequality of triangle that sum of 2 sides is greater than the third side.
d2=math.sqrt(p2p3)
d3=math.sqrt(p3p1)
if d1+d2>d3 and d2+d3>d1 and d1+d3>d2:
    print("A triangle can be formed with the given points")
else:
    print("Triangle cannot be formed with the given points")


