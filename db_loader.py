import datetime
import time


print(datetime.datetime.now())
now = datetime.datetime.now()
if now.hour < 17:
    print('before 17')
else:
    print('after 17')
