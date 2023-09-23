#to find the greatest of three numbers
x=int(input("Enter first Number:"))
y=int(input("Enter second Number:"))
z=int(input("Enter third Number:"))

"The greatest of the 3 numbers is"
if x>=y>=z or x>=z>=y:
    print("The greatest of the 3 numbers is = ",x)
elif y>=x>=z or y>=z>=x:
    print("The greatest of the 3 numbers is = ",y)
elif z>=y>=x or z>=x>=y:
    print("The greatest of the 3 numbers is = ",z)
elif x==y==z:
    print("All 3 numbers are equal")
