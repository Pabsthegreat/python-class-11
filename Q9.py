n=int(input("Enter a number : "))
D=len(str(n))
if D%2==0:
    for d1 in range(2,n+1):
        r=n%d1
        if r==0:
            m=len(str(d1))
            if D==2*m:
                    d2=n//d1
else:
    print("The number is not a vampire number")

                                         
