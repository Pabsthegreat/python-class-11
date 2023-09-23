q1=int(input("how many elements do u want to compare?"))
l1=[]
for j in range(q1):
    s=input("Enter a number or string")
    l1.append(s)
    print(l1)
import math
half=math.ceil((len(l1))/2)
l2=l1[0:half]
del l1[0:half]
l1.extend(l2)
print(l1)
