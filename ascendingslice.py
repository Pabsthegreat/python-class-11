q1=int(input("how many elements do you want to compare?:"))
l1=[]
l2=[]
for j in range(q1):
	s=int(input("Enter a number:"))
	l1.append(s)
	print("Your list now is =",l1)
min=l1[0]
for j in range(len(l1)):
    min=l1[j-len(l2)]
    for i in l1:
        if min<i:
            continue
        else:
            min=i
    l1.remove(min)
    l2.append(min)
    
print("Ascending order is:",l2)
print("Descending order is:",l2[::-1])

