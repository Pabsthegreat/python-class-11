#biggest and smallest number.
q1=int(input("how many numbers do u want to compare?"))
l1=[]
for j in range(q1):
    s=int(input("Enter a number"))
    l1.append(s)
    print("Your list now is",l1)
    
greater=[0]
lesser=[0]
for i in range (len(l1)):
    b=l1[i:1+i]
    if greater>b:
        continue
    else:
        greater=b
    if lesser<b:
        continue
    else:
        lesser=b
print("The greatest number is =",greater)
print("The least number is =",lesser)

l2=[]
import math
for x in range (len(l1)):
    m=l1[i:1+i]
    y=m[0]
    n=math.sqrt(y)
    l2.append(n)
print("The square roots of the numbers in order are=",l2)
#how to extract every element as a string
#indexing returns as string m[0]

    

    
