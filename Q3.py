#armstrong number
n=int(input("Enter a number : "))
n1=n
x=len(str(n))
sum1=0
#for i in range (1,x+1):
while (n>0):
    a=n%10
    sum1=sum1+a**x
    n=n//10
if sum1==n1:
    print(n1," is an Armstrong number")
else:
    print(n1,"is not an Armstrong number")
