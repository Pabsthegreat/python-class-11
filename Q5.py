m=int(input("Enter lower limit : "))
n=int(input("Enter upper limit : "))
for i in range(m,n+1):
    for j in range(2,i):
        r=i%j
        if r==0:
            print(end="")
            break
    else:
        print(i)            
