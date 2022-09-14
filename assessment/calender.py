import calendar

def display_calender(y,m):
    print(calendar.month(y,m))
    print(calendar.calendar(y))

y=int(input("Enter the year : "))
m=int(input("Enter the month : "))
display_calender(y,m)