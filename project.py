
''' SOLUCIONES DE LA PHYSICA
    By
    Adarsh Arun Hoskere XI A
    Adarsh Sasikumar XI C
    Rishabh Kartik Jawagal XI C
    In this project we provide the students of class 11 a platform to quickly check their answers by providing the input of the given information in the questions.
    This helps the students to save time as they don’t have to search across the internet to verify their answers.
    INDEX
    1.MOTION IN STRAIGHT LINE
    2.PROJECTILE MOTION
    3.NEWTON’S LAWS OF MOTION
    4.WORK POWER ENERGY
    5.GRAVITATION
'''
import math
from typing import Annotated, overload
print("Hello, user\n")
print("This is a program where you can get solutions for your physics problems.\nPlease enter all inputs in lowercase\n!")

top = {1:"Motion in a Straight Line", 2: "Projectile Motion", 3:"Newton's Laws of Motion", 4:"Friction", 5:"Work Power Energy", 6:"Gravitation"}

#getting user input for the topic
chp = int(input(
'''
Available Topics are:

1)MOTION IN STRAIGHT LINE
2)PROJECTILE MOTION
3)NEWTON’S LAWS OF MOTION
4)FRICTION
5)WORK POWER ENERGY
6)GRAVITATION

Enter Topic number :'''))

if (top.get(chp) == "?"):
    print("Choose one of the topics given.")




#Motion in a straight line
if chp == 1:
    misl = {"1) average velocity":"avgv","2) equations of motion":["v","s","v^2"],"3) Relative velocity":"relvel"}
    x = list(misl.keys())
    print("The subtopics are:\n")

    for i in x:
        print(i)
    sub = int(input("Enter the number of the subtopic:"))


#average velocity
    if sub == 1:
        vel = int(input("How many velocities to average?:"))
        total = 0
        for i in range(vel):
            v = int(input("Enter velocity:"))
            total += v
        print("Average velocity =", total / vel)

#equations of motion    
    if sub == 2:

        print("Please enter '?' if value is unknown")

        #getting user input for values and unknowns

        u = input("Enter the intital velocity:")
        if u != "?":
            u = int(u)

        v = input("Enter the final velocity:")
        if v != "?":
            v = int(v)

        s = input("Enter the distance or displacement:")
        if s != "?":
            s = int(s)

        a = input("Enter the acceleration:")
        if a != "?":
            a = int(a)

        t = input("Enter the time period:")
        if t != "?":
            t = int(t)
        

        #calculating the variables when different combinations of variables are unknown

        if v == "?" and u == "?":
            u = (s - 0.5 * a * t ** 2) / t
            v = u + a * (t)

        elif v == "?" and a == "?":
            a = 2 * (s - u * t) / t ** 2
            v = u + a * t
        
        elif v == "?" and t == "?":
            v = math.sqrt(u ** 2 + 2 * a * s)
            t = (v - u) / a
        
        elif v == "?" and s == "?":
            v = u + a * t
            s = (v ** 2 - u ** 2) / 2 * a
        
        elif u == "?" and t == "?":
            u = v ** 2 - 2 * a * s
            t = (v - u) / a
            
        elif u == "?" and s == "?":
            u = v - a * t
            s = (v ** 2 - u ** 2) / 2 * a

        elif t == "?"and s == "?":
            t = (v - u) / a
            s = (v ** 2 - u ** 2) / 2 * a
        
        elif t == "?" and a == "?":
            a = (v ** 2 - u ** 2) / 2 * s
            t = (v - u) / a


        elif s == "?" and a == "?":
            a = (v - u) / t
            s = (v ** 2 - u ** 2) / 2 * a

        print("initial velocity:",u,", final velocity:",v,", Displacement:",s,", Acceleration:",a,", time period",t)

#relative velocity

vel1 = int(input("Enter velocity A:"))
vel2 = int(input("Enter velocity B:"))
print("Relative velocity of A with respect to B is :", vel1 - vel2)
print("Relative velocity of B with respect to A is :", vel2 - vel1)
        
         
        
#Projectile Motion
if chp == 2:
    proj = {"1) time":"t", "2) max range":"ran", "3) max height":"h"}
    x = list(misl.keys())
    print("The subtopics are:")
    for i in x:
        print(i)
    sub = int(input("Enter the number of the subtopic:"))



#Newton's Laws of Motion
if chp == 3:
    nlm = {"1) linear momentum":"lm", "2) impulse":"im", "3) limiting friction": "lf"}
    x = list(misl.keys())
    print("The subtopics are:")
    for i in x:
        print(i)
    sub = int(input("Enter the number of the subtopic:"))



#Work Power Energy
if chp == 4:
    wpe = {"1) work":"wk", "2) kinetic energy":"ke", "3) potential energy":"pe", "4) power":"pw"}
    x = list(misl.keys())
    print("The subtopics are:")
    for i in x:
        print(i)
    sub = int(input("Enter the number of the subtopic:"))



#Gravitation
if chp == 5:
    grav = {"1) gravitational force":"gf", "2) gravitational acceleration":"ga", "3) orbital velocity":"ov", "4) potential energy": "gpe"}
    x = list(misl.keys())
    print("The subtopics are:")
    for i in x:
        print(i)
    sub = int(input("Enter the number of the subtopic:"))







