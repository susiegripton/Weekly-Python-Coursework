# ask user to enter year
year=input("Enter a year: ")
year=int(year)
# years divisible by 400 are leap years
if year % 400==0:
    print("Leap year")
# remainding years divisible by 100 are not leap years
elif year % 100==0:
    print("Not a leap year")
# remainding years divisible by 4 are leap years
elif year % 4==0:
    print("Leap year")
# all other years are not leap years
else:
    print("Not a leap year")
    
