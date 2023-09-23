#find if the point lies outside or inside or on the circumference of the circle
x=float(input("Enter x coordinate of the point="))
y=float(input("Enter y coordinate of the point="))
x2=0                                           #(x2,y2) are coordinates of the origin
y2=0
p1p2=(x2-x)**2+(y2-y)**2        #distance formula.
import math                                #radius is 1 unit 
d=math.sqrt(p1p2)  
if d>1 :
    print("Point lies outside the circumference of unit circle")
if d==1:
    print("Point lies on the circumference of the unit circle")
if d<1:
    print("Point lies inside the circumference of the unit circle")
    
















































