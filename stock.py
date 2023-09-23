stock="Apple=40,Orange=100,Pineapple=40,kiwi=20"
s=stock.split(",")
d1={}
s2=[]
for i in s:
    s2+=i.split("=")
for j in range(0,8,2):
    d1[s2[j]]=s2[j+1]
print(d1)
    
    
