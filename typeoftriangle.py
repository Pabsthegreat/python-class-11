#To find whether a triangle is isosceles, equilateral or scalene
x=input("Do you want to check with sides(y) or angles(n)?")
if x=="y":                                                   #checking with sides
    AB=float(input("Enter the length of first side ="))
    BC=float(input("Enter the length of second side ="))
    AC=float(input("Enter the length of third side ="))
    if AB+BC+AC>180 or AB+BC+AC<180:
        print("Triangle cannot be formed, please try again")
    if AB==BC==CA:
        print("The triange is equilateral")
    elif AB==BC or AB==AC or BC==AC:
        print("The triangle is isoscles")
    if AB!=BC!=AC:
        print("The triangle is scalene")
elif x=="n":                                                  #checking with angles
        A=float(input("Enter the first angle="))
        B=float(input("Enter the second angle ="))
        C=float(input("Enter the third angle ="))
        if A+B+C>180 or A+B+C<180:
            print("Triangle cannot be formed, please try again")
        elif A==B==C:
            print("The triange is equilateral")
        elif A==B or A==C or B==C:
            print("The triangle is isoscles")
        else:
            print("The triangle is scalene")
    
