from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


Now = datetime.now()
print("today is", Now)

print(datetime.time(datetime.now()))

print("the time now is:", Now.strftime("%X"))

t = Now - timedelta(weeks=2)
s = t.strftime("%A %B, %d, %Y")
print ("2 weeks ago, it was", s)

today = date.today()
afd = date(today.year, 4, 1 )
print ("Time to next april fools day:", today - afd)
if afd < today:
    print ("april fool day already gone %d days ago" %((today-afd).days))
    afd = afd.replace(year=today.year+1)
time_to_afd = afd-today
print("Its just", time_to_afd.days, "days until next april fools day")


import os

print(os.name)