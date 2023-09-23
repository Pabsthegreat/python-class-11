#reversing a string without slicing ands checking if it is a palindrome
s1=input("Enter a string")
s2=""
for a in range(len(s1)-1,-1,-1):
    s2+=s1[a]
if s1== s2:
    print("The entered word is a palindrome")
else:
    print("The entered word is not a palindrome")
    
