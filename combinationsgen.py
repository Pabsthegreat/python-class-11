name=input("Enter your name:")
praise=int(input("Enter number of times you want to be praised:"))
l1=[]
l3=[]
l4=[]
for n in range(1,praise+1):
    l3.append(n)
    pr1=input("Enter the phrase you want to praise yourself with:")
    l4.append(pr1)
l1=[name]+["is"]+[l3]+[l4]
l2=[]
l2+=l1[0:2]
for i in range(2,len(l1)-1):
    l2.clear()
    l2+=l1[0:2]
    print(l1[i],l1[1+i])
    for j in range(len(l1[i])):
        l2+=[l1[i][j]] + [l1[i+1][j]]
        print(l2)
        del l2[2:]
