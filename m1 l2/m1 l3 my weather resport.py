
city=input("city:")
temp=float(input("temperature: "))
if temp> 35: 
    print("very hot")
elif temp >25:
    print("warm- go outside")
elif temp > 20:
    print("nice weather")
else:
    print("take a jacket")
print("city: ,",city)
import datetime
import calendar
now=datetime.datetime.now()
print("city",city)
print("time now", now)
print (calendar.calendar(now.year))
print("time:" , datetime.datetime.now())

