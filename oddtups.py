#Write a program to create two tuples of numbers. Pick only even numbers from both tuples to form a third one
ter1=int(input("Enter number of elements in first tuple:"))
t1=()

for i in range (ter1):
    ele=int(input("Enter numbers:"))
    t1+=(ele,)
    print(t1)

ter2=int(input("Enter number of elements in second tuple:"))
t2=()

for j in range (ter2):
    elm=int(input("Enter numbers:"))
    t2+=(elm,)
    print(t2)

t3=()

for k in t1:

    if k%2 == 0:
        t3+=(k,)

for l in t2:

    if l%2 == 0:
        t3+=(l,)

print(t3)
