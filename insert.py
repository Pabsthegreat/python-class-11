q1=int(input("how many elements do you want to have?"))
l1=[]
l2=[]
for j in range(q1):
	s=int(input("Enter a number"))
	l1.append(s)
	print("Your list now is =",l1)

ans=input("Do u wanna operate on a list?")

while ans=="Yes" or ans=="yes":
        print('''\nWhat action would you like to perform : \n1.Insert\n2.Append\n3.Modify existing element\n4.Delete\n5.Sort list\n6.Display the list in ascending and descending order\n7.Stop\n''')
        ans1=int(input("Enter an option"))

#inserting elements
        if ans1==1:
                print("The list is  =",l1)
                for x in range (len(l1)):
                        l2.append(x)
                print("Index of are =",l2)
                ap=int(input("Enter an element u want to insert"))
                ind=int(input("Enter index u want to insert"))
                l1.insert(ind,ap)
                print("Your list now is =",l1)
#append a list
        if ans1==2:
                q2=int(input("how many elements do you want to have in in the list you want to append to the previous list?"))
                l3=[]
                for j in range(q2):
                        r=int(input("Enter a number"))
                        l3.append(r)
                        print("Your list now is =",l3)
                print("Your new list is",l1.extend([l3]))
#Modify element
        if ans1==3:
                print("List now is=     ", l1)
                l2.clear()
                for x in range (len(l1)):
                        l2.append(x)
                print("Index of val are =",l2)
                q1=int(input("Index of element you want to modify="))
                mod=int(input("element you want to add instead="))
                l1[q1]=mod
                print("your list now is =",l1)
                
#deleting an element by using its index
        if ans1==4:
                print("your list now is =",l1)
                print("Index of val are =",l2)
                q1=int(input("Index of element you want to delete="))
                l1.pop(q1)
                print("your list now is =",l1)

#deleting element with given value
        if ans1==5:
                mod=int(input("value you want to delete="))
                l1.remove(mod)
                print("your list now is =",l1)

#ascending order
        if ans1==6:
                l1.sort()
                print("List in ascending order is =", l1)

#descending order
        
                l1.sort(reverse=True)
                print("List in descending order is =", l1)

                
        if ans1==7:
                print("Thank you, maybe another time")
	









