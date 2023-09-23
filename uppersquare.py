#squaring nos, upper of letters
q1=int(input("how many elements do u want to compare?"))
l1=[]
for j in range(q1):
    s=input("Enter a number or string")
    if s.isdigit():
        sqr=int(s)**2
        l1.append(sqr)
    if s.isalpha():
        upper=s.upper()
        l1.append(upper)
print(l1)
