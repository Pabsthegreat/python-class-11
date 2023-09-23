#to calculate compound interest
print("compound interest calculator")
k=float(input("Enter the principal amount :"))
r=float(input("Enter the interest rate (%):"))
t=float(input("Enter time period (years) :"))
n=int(input("Enter the number of times the interest is compunded in a year:"))
y=n*t
z=r/(100*n)
x=float(k*(1+z )**y)
print("The total interest you will recieve is :" ,x-k, "rupees")
      
