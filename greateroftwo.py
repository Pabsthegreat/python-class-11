l1=[1,2,2,3,4,4,5,6,8,]
import math
for i in range (len(l1)):
    n=l1[i]>l1[i+1]
    if n==True:
        max=l1[i]
    else:
        max=l1[i+1]
    print(max)
