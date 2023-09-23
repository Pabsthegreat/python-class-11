#Write a python program that creates a tuple storing first 9 terms of Fibonacci series. Fromthe created tuple, if the program receives a Fibonacci term, return the index of the number
t=(0,1)
for i in range (2,11):
    t += (t[i-2]+t[i-1],)
print(t)

num=int(input("Enter a fibonacci number:"))
print(t.index(num)+1)