print("Would you like to see palindromes in a range?")
see=input("Yes or No?\n")
while see=="Yes" or "yes":
    print("1. Palindrome\
           2. Exit")
    x=input("1 or 2? \n")
   
    if x=="1":
        n1=int(input("Enter lower limit : "))
        n2=int(input("Enter upper limit : "))
        for n in range(n1,n2+1):
              a=len(str(n))
              t=n
              sum1=0
              while n>0:
                o=n%10
                sum1=sum1+o*10**(a-1)
                a=a-1
                n=n//10
              if sum1==t:
                print(t)
              if sum1!=t:
                print(end="")
        print()      
    elif x=="2":
        print("Thank You")
        break
else:
    print("Maybe next time")
    
