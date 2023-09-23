t=()
t1=[]
num=int(input("Enter number of numbers:"))
for i in range(num):
    n=int(input("Enter number:"))
    t+=(n,)
for j in t:
    if j%2 != 0:
        t1.append(j)
print(t1)
