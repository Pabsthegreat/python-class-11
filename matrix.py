 #Create a dictionary to display 3x3 matrix in dictionary format with row number being the keys
rows=int(input("Enter number of rows of matrix:"))
mx={}

columns=int(input("Enter number of columns:"))

for i in range(1,rows+1):
    x=[]
    mx[i]=x
    print("Next row of elements")

    for j in range(columns):

        nm=int(input("Enter number:"))
        x.append(nm)

print(mx)
        
