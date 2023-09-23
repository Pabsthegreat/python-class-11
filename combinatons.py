l1=["Adarsh","is",[1,2,3,4,5],["the greatest","the best","the dumbest","the most legendary","the smartest"]]
for i in range(5):
    num=l1[2][i]
    adj=l1[3][i]
    print(l1[0:2]+[num]+[adj])

