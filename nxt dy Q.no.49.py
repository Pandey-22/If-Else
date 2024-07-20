# year=int(input("Input a year: "))
# if (year % 400 == 0):
#     leap_year=year
# elif (year % 100 == 0):
#     leap_year = year
# elif (year % 4 == 0):
#     leap_year = year
# else:
#     leap_year = year
# month=int(input("Input a month [1-12]: "))
# if month in (1, 3, 5, 7, 8, 10, 12):
#     month_length = 31
# elif month == 2:
#     if leap_year:
#         month_length = 29
#     else:
#         month_length = 28
# else:
#     month_length = 30
# day=int(input("Input a day [1-31]: "))

# if day < month_length:
#     day += 1
# else:
#     day = 1
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1
# print(year,month,day)



day=int(input("enter the day[1-31]"))
month=int(input("enter the month[1-12]"))
year=int(input("enter the year"))
if month in (1,3,5,7,8,10,12):
    if day==31:
        print("1",month+1,year)
    else:
        print("1",month,year)
elif month==2:
    if day==28:
        print("1","3",year)
    elif day==29 and year % 4==0:
        print("leap year")
        print("1",month+1,year)
    else:
        print(day,month,year)
elif month in (4,6,9,11):
    if day==30:
        print("1",month+1,year)
    else:
        print("error")
else:
    print("nothing")