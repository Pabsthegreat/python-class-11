q1=int(input("how many elements do u want to compare?"))
l1=[]
for j in range(q1):
    s=input("Enter a number or string")
    l1.append(s)
    print(l1)
for i in l1:
   if l1.count(i)>1:
       l1.remove(i)
print(l1)
