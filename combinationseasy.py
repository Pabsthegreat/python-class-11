name=input("Enter your name:")
praise=int(input("Enter number of times you want to be praised:"))
l1=[]
l2=[]
l3=[name]+["is"]
l4=[]
for n in range(1,praise+1):
    l1.append(n)
    pr1=input("Enter the phrase you want to praise yourself with:")
    l2.append(pr1)
for i in range(len(l1)):
    l3+=[l1[i]]+[l2[i]]
    print(l3)
    del l3[2:]
