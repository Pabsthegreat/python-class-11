q1=int(input("how many elements do you want to have?"))
l1=[]
l2=[]
for j in range(q1):
    s=int(input("Enter a number"))
    l1.append(s)
    print("Your list now is =",l1)
l2=l1.sort()
if l1==l2:
    print("The list is in ascending order")
else:
    print("The list is not in ascending order")
