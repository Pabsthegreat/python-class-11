#to find out if the given year is a leap year
year=int(input("Enter the year"))
if year%100==0 & year%400==0:
    print("The year is a leap year")
elif year%4==0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
