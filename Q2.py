#sum using while loop
sum1=0
n=0
q=input("Would you like to add more numbers?")
while q=="Yes" or "yes":
    n=int(input("Enter a number :"))
    sum1+=n
    if n<0:
        print("Can't add negative numbers")
        break
    print("The sum of the numbers is",sum1)
    q=input("Would you like to add more numbers?")
else:
    print("Sum of all numbers you have entered so far is ", sum1)
