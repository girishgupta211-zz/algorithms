from datetime import datetime
import pytz

timecodes_input = "2019-03-15T11:01:38+05:30,2019-03-15T11:01:38+05:30,2019-03-15T11:01:38+05:30,2019-03-15T11:01:38+05:30,2019-03-15T11:01:38+05:30,2019-03-15T11:01:38+05:30,2019-03-15T11:01:38+05:30,2019-03-15T11:01:38+05:30,2019-03-15T11:01:38+05:30,2019-03-15T11:01:38+05:30"
timecodes = timecodes_input.split(',')
timecodes_epoch = []
test_list = ['test','test_hin','test_tam','test_tel','test_kan','test_ben','test_mal','test_mar','test_dug','test_dug_hin']

for timecode in timecodes:
  from dateutil.parser import parse
  get_date_obj = parse(timecode).astimezone (pytz.utc)
  epoch =  int((get_date_obj- datetime(1970, 1, 1,tzinfo=pytz.utc)).total_seconds())
  timecodes_epoch.append(epoch)
#   print(epoch)
# print(timecodes_epoch)

test_values = dict(zip(test_list, timecodes_epoch))
# print(test_values)
