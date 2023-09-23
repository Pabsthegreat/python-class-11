#To check if a character is an alphabet (lowercase, uppercase) or number or a special character.
ch = input("Enter a character:")
if (ord(ch) >= 65 and ord(ch) <= 90):
    print("Uppercase")
if (ord(ch) >= 97 and ord(ch) <= 122):
    print("Lowercase")
elif (ord(ch) >= 48 and ord(ch) <= 57):
    print("Number")
else:
    print("Special character")
