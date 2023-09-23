#factorial sum
import math
n=int(input("Enter a number : "))
sum1=0
for i in range (1,n+1):
    x=math.factorial(i)
    sum1= sum1+ x
print("The sum of the factorials of the numbers till",n,"is", sum1)
