#sum of sequences
n=int(input("Enter the power : "))
x=int(input("Enter the base : "))
sum1=0
for y in range(1,n+1):
    if y%2==0:
        sum1-= x**y/y
    if y%2==1:
        sum1+= x**y/y
print("The sum of the sequence is", sum1)
