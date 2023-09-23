#Menu driven program
print("Total marks , percentage and grade calculator")                            #Accept the name of the student and display the below options addressing the student once.
name=input("Enter your name")
print(name)
print("What do u wish to do?\n\
              1)Print your marks in 5 subjects\n\
              2)Calculate total marks and percentage in 5 subjects\n\
              3)Find your grade")
option=int(input("Enter your option"))
if option=="1":
    print("Please enter all marks out of 100")                                  #Accept marks (out of 100) of 5 major subjects in class X and display the same.

math=float(input("Enter your marks in Math :"))
science=float(input("Enter your marks in Science :"))
english=float(input("Enter your marks in English :"))
social=float(input("Enter your marks in Social Science :"))
lang=float(input("Enter your marks in 2nd Language :"))
print("\n\n\nYour marks in math is = ",math,
        "\nYour marks in Science is = ",science,
        "\nYour marks in English is = ",english,
        "\nYour marks in Social Science is = ",social,
        "\nYour marks in 2nd Language is = ",lang)
exit()

if option=="2":                                                                                      #Accept marks (out of 100) of 5 major subjects in class X and display the same.

    print("Please enter all marks out of 100")
math=float(input("Enter your marks in Math :"))
science=float(input("Enter your marks in Science :"))
english=float(input("Enter your marks in English :"))
social=float(input("Enter your marks in Social Science :"))
lang=float(input("Enter your marks in 2nd Language :"))
total=math+science+social+english+lang
print("Your total is = ", total, " out of 500")
print("Your total percentage is +", (total / 500)*100,"%")
exit()

if option=="3":                                                                                          #Find the grade of a student
percentage=int(input("Enter your percentage")
if y>85:
    print("Your grade is = A")
if percentage<85 and percentage>=75:
    print("Your Grade is = B")
if percentage<75 and percentage>=50:
    print("Your grade is = C")
if percentage>=30 and percentage<=50:
    print("Your grade is = D")
if percentage<30 :
    print("You have to reappear for the exams")
exit()


