n=10
for i in range (n,0,-1):
    for x in range (i,n):
        print(x, end =" ")
    print()

for i in range (n,0,-1):
    for j in range(1,i):
        print(end='   ')
    for x in range (i,n):
        print(x,end=" ")
    print()
