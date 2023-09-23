d1={}
num=int(input("Enter number of players:"))
for i in range(num):
    nm=input("Enter player's name:")
    d1[nm]=0
print(d1)

for i in range(num):
    nm=input("Enter player's name:")
    runs=int(input("Enter runs scored by the above player:"))
    d1[nm]=runs
print(d1)
    
    
