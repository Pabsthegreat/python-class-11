n1=int(input("Enter lower limit : "))
n2=int(input("Enter upper limit : "))
#for i in range(n1,n2):
i=n1
while (i>=n1) and (i<=n2):
    sum1=0
    j=1
    #for j in range(1,i):
    while j<i:
        r1=i%j
        if r1==0:
            sum1=sum1+j
        j+=1
    if sum1==i:
        print(i)
    i+=1
