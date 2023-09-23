n=int(input("Enter a number : "))
print("+", "/\/\ " * n ,"+",sep="")
for i in range(1,n+1):
    print("|", " "*8*n, "|")
    print()
print("+", "/\/\ " * n ,"+", sep="")
