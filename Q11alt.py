x=[1,2,3]
a=[[]]
b=[]
for i in x:
    b=list(a)
    for j in b:
        a=a+[j+[i]]
print(a)    