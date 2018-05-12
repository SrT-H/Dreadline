from datetime import datetime, time

now = datetime.now()
beginning_of_day = datetime.combine(now.date(), time(0))
print (now - beginning_of_day).seconds
