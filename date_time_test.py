import datetime

print(datetime.timedelta(days=1, hours=30, minutes=100))
print(datetime.timedelta(days=5, seconds=63000))
print(datetime.timedelta(weeks=7))

print(datetime.datetime.now())

print(datetime.date.today())
print(datetime.date.today().replace(year=2020))

datetime.timezone(datetime.timedelta(hours=9))

print(datetime.date(2019, 12, 25))
print(datetime.date.fromisoformat('2019-12-25'))

print(datetime.time(13, 42, 35))
print(datetime.time.fromisoformat('13:42:35.458+09:00'))