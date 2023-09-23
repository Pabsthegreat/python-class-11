n2=int(input("Enter a number: "))
d=12+(n2-1)*20
sum1=0
print("The given AP is 12,32,52...")
for i in range (12,d+1,20):
    sum1+=i
print("The sum of the series is",sum1)
