n1=int(input("Enter a number : "))
n2=int(input("Enter a number : "))
sum1=0
for i in range(1,n1):
    r1=n1%i
    if r1==0:
        sum1=sum1+i
if sum1==n2:
    sum2=0
    for j in range(1,n2):
        r2=n2%j
        if r2==0:
            sum2=sum2+j
    if sum2==n1:
        print("The numbers are Amicable")
    else:
        print("The numbers are not Amicable")
else:
    print("The numbers are not Amicable")
