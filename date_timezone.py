from datetime import datetime

import pytz
from dateutil.parser import parse

input_dates = "2019-03-15T11:01:38+05:30,2019-03-15T11:01:38+05:30"
input_dates_arr = input_dates.split(',')
dates_epoch = []
test_list = ['test', 'test_hin']

for input_date in input_dates_arr:
    get_date_obj = parse(input_date).astimezone(pytz.utc)
    base_date = datetime(1970, 1, 1, tzinfo=pytz.utc)
    print(get_date_obj)
    epoch = int((get_date_obj - base_date).total_seconds())
    dates_epoch.append(epoch)

test_values = dict(zip(test_list, dates_epoch))
print(test_values)
