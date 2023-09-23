#to find if a given number is odd or even
x=int(input("ENter a number"))
if x==0:
    print("Number entered is 0")
if x%2==0:
    print(x, "is even")
if x%2 != 0:
    print(x, "is odd")
