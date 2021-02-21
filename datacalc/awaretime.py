import datetime
import pytz

local_time=datetime.datetime.now()
utc_time=datetime.datetime.utcnow()

print("naive local time  {}".format(local_time))
print("naive utc time {}".format(utc_time))
