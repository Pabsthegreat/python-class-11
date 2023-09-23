a=(0,1)
b=(0,1)
for i in range (1,9):
    c=a[i]+a[i-1]
    a+=c,
print(a)

x=int(input("Enter a number in the Fibonacci series : "))
for j in range (1,x):
    f=b[j]+b[j-1]
    b+=f,
    if f==x:
        print(j+2)
