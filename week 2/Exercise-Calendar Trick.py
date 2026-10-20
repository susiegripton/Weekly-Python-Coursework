print("Please think of a date")
day=int(input("Please enter a day of the month (1,2,3, etc.):"))
month=int(input("Please enter the month (1=Jan, 2=Feb, etc.):"))
fullyear=input("Please enter the year (2025, etc.)")
century=int(fullyear[0:2])
year=int(fullyear[2:])
print(f"day:{day},month:{month},century:{century},year:{year}")
D=day
if (century==17 and year==52 and month==9 and day<=2) or (century==17 and year==52 and month<9) or (century==17 and year<52) or century<17:
    print("julian calendar")
else:
    print("gregorian calendar")
if (century==17 and year==52 and month==9 and day<=2) or (century==17 and year==52 and month<9) or (century==17 and year<52) or century<17:
    C=18-century
else:
    rem=century%4
    C=(3-rem)*2
rem=year%12
twelves=int(year/12)
fours=int(rem/4)
Y=twelves+rem+fours
month_numbers=[]
thismonth=0
for n in range(1,13):
    month_numbers.append(thismonth)
    if n in (1,3,5,7,8,10,12):#Jan,Mar,May,Jul,Aug,Oct,Dec
        thismonth+=31
    elif n in (4,6,9,11):#Apr,Jun,Sep,Nov
        thismonth+=30
    else:#Feb
        thismonth+=28
    thismonth=thismonth%7
M=month_numbers[month-1]
print(C,Y,M,D)
w=(C+Y+M+D)%7
weekdays=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
wly=(C+Y+M+D-1)%7
if(century==17 and year<=52) or century<17:
    leap=(int(fullyear)%4==0)
else:
 leap=(int(fullyear)%400==0 or(int(fullyear)%4==0 and int(fullyear)%100!=0))

if (int(fullyear)%400==0 or int(fullyear)%4==0) and month>=2:
    print(weekdays[wly])
else:
    print(weekdays[w])
    
