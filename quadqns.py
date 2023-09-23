#To find the real roots of a quadratic equation. If it has imaginary roots, display appropriate message
a=float(input("Enter the coeffecient of the quadratic term="))
b=float(input("Enter the coeffecient of the liner term="))
c=float(input("Enter the constant term ="))
x=(b**2)-4*a*c                                   
if x>=0:
    print("The quadratic equation has real roots")
    print("The roots are = ",(-b+(x**0.5))/2*a , (-b-(x**0.5))/2*a)
else:
    print("The quadratic equation has no real root")
