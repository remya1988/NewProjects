year = input("Year : ")
month = input("Month(1-12) : ")
day = input("Day(1-31) : ")

Months =["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
MonthIndex = int(month)-1
days = int(day)
ending=["st","nd","rd"]+17*["th"]+["st","nd","rd"]+7*["th"]+["st"]
dayOut=day + ending[days-1]
print( dayOut+" " +Months[MonthIndex]+ " "+year)