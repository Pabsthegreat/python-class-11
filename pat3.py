#pat3
s=4
for i in range (1,6,):
    for j in range (s,0,-1):
        print(end=" " )
    for x in range(1,i):
        print("*",end=" ")
    s-=1
    print()


