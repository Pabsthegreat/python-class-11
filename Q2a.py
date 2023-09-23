#With slicing operator – print the reversed string and with alternate character be replaced with ‘*’
s1=input("Enter a string")
rev=s1[::-1]
print(rev)
for i in range(0,len(rev)):
    if i%2==1:
        print("*", end="")
    else:
        print(rev[i], end="")
