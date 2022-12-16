from datetime import datetime
now = datetime.now()
#print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
#print(day, month, year, hour, minute)
#print('timestamp', timestamp)
#print(f'{day}/{month}/{year}, {hour}:{minute}') # 8/7/2021, 7:38

'''
Formatting Date Output Using strftime

'''

from datetime import datetime
new_year = datetime(2020, 1, 1)
#print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
#print(day, month, year, hour, minute) #1 1 2020 0 0
#print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0

'''
Using date from datetime
'''

from datetime import date
d = date(2022,1,1)
#print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
# print("Current year:", today.year)   # 2019
# print("Current month:", today.month) # 12
# print("Current day:", today.day)     # 5

'''
Time Objects to Represent Time
'''
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
# print("a =", a)
# # time(hour, minute and second)
# b = time(10, 30, 50)
# print("b =", b)
# # time(hour, minute and second)
# c = time(hour=10, minute=30, second=50)
# print("c =", c)
# # time(hour, minute, second, microsecond)
# d = time(10, 30, 50, 200555)
# print("d =", d)

'''
output
a = 00:00:00
b = 10:30:50
c = 10:30:50
d = 10:30:50.200555
'''

'''
Difference Between Two Points in Time Using
'''
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
#print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
#print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00

'''
Difference Between Two Points in Time Using timedelata
'''

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
#print("t3 =", t3)


'''
###########################################################################################################
###########################################################################################################
'''

'''
Exercises:
'''


'''
1.Get the current day, month, year, hour, minute and timestamp from datetime module
2.Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
3.Today is 5 December, 2019. Change this time string to time.
4.Calculate the time difference between now and new year.
5.Calculate the time difference between 1 January 1970 and now.
6.Think, what can you use the datetime module for? Examples:
-ime series analysis
-To get a timestamp of any activities in an application
-Adding posts on a blog
'''

'''
###################################
................ 1 ................
###################################
'''

current_time = datetime.now()

day_now = current_time.day
month_now = current_time.month
year_now = current_time.year
hour_now = current_time.hour
minute_now = current_time.minute
second_now = current_time.second
time_stamp = current_time.timestamp

'''
###################################
................ 2 ................
###################################
'''

current_date = current_time.strftime("%m/%d/%Y, %H:%M:%S")

'''
###################################
................ 3 ................
###################################
'''
time_now = datetime(year_now,month_now,day_now, hour_now, minute_now,second_now )
my_new_date = f'{year_now} {month_now} {day_now}'

my_date = datetime.strptime(my_new_date, "%Y %m %d")

#print(my_date)

'''
###################################
................ 4 ................
###################################
'''
time_newyear = datetime(year= 2023, month=1, day= 1, hour= 00,  minute=00, second= 00)

time_left_for_newyear = time_newyear - time_now

#print('Time left for new year:',time_left_for_newyear)

'''
###################################
................ 5 ................
###################################
'''

time_1970 = datetime(year= 1970, month=1, day= 1, hour= 00,  minute=00, second= 00)

time_difference = time_now - time_1970

#print(time_difference)

'''
###################################
................ 6 ................
###################################
'''

# 1. Take notes with the current time
# 2. Calculate user age