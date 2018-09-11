import datetime
import unittest


# Calculating next valid draw date
# The Irish lottery draw takes place twice weekly on a Wednesday and a Saturday at 8pm. Write a
# function that calculates and returns the next valid draw date based on an optional supplied date
# time parameter. If no supplied date is provided, assume current date time

def next_lottery_date(input_date=None):
    """ Calculate and return the next valid Irish Lotto draw date.
           input_date = datetime object (optional, default value is current date/time) """

    # 0 = Monday, 1 = Tuesday, 2 = Wednesday, .... 6 = Sunday

    wednesday = 2
    saturday = 5
    if input_date is None:
        input_date = datetime.datetime.now()
    else:
        if not isinstance(input_date, datetime.datetime):
            return "input date format is not datetime type"

    # after 19:59 you've missed draw, so get the next date
    if input_date.hour > 19:
        input_date += datetime.timedelta(days=1)

    # Get week day from input date
    week_day_no = input_date.weekday()

    def _get_combined_date(user_date, days_diff):
        return datetime.datetime.combine((user_date + datetime.timedelta(days=days_diff)).date(),
                                         datetime.time(20, 00))

    if week_day_no in (wednesday, saturday):
        return _get_combined_date(input_date, 0)

    elif week_day_no < wednesday:
        return _get_combined_date(input_date, wednesday - week_day_no)

    elif week_day_no < saturday:
        return _get_combined_date(input_date, saturday - week_day_no)
    # case to handle sunday
    else:
        return _get_combined_date(input_date, 3)


class TestNexDrawDate(unittest.TestCase):
    def test_before_wednesday(self):
        input_date = datetime.datetime(2018, 9, 10)
        self.assertEqual(next_lottery_date(input_date), datetime.datetime(2018, 9, 12, 20, 0, 0))

    def test_after_wednesday(self):
        input_date = datetime.datetime(2018, 9, 13)
        self.assertEqual(next_lottery_date(input_date), datetime.datetime(2018, 9, 15, 20, 0, 0))

    def test_after_saturday_before_wednesday(self):
        input_date = datetime.datetime(2018, 9, 17)
        self.assertEqual(next_lottery_date(input_date), datetime.datetime(2018, 9, 19, 20, 0, 0))

    def test_on_wednesday_before_8pm(self):
        input_date = datetime.datetime(2018, 9, 12, 19, 0, 0)
        self.assertEqual(next_lottery_date(input_date), datetime.datetime(2018, 9, 12, 20, 0, 0))

    def test_on_wednesday_after_8pm(self):
        input_date = datetime.datetime(2018, 9, 12, 21, 0, 0)
        self.assertEqual(next_lottery_date(input_date), datetime.datetime(2018, 9, 15, 20, 0, 0))

    def test_on_saturday_before_8pm(self):
        input_date = datetime.datetime(2018, 9, 15, 19, 0, 0)
        self.assertEqual(next_lottery_date(input_date), datetime.datetime(2018, 9, 15, 20, 0, 0))

    def test_on_saturday_after_8pm(self):
        input_date = datetime.datetime(2018, 9, 15, 21, 0, 0)
        self.assertEqual(next_lottery_date(input_date), datetime.datetime(2018, 9, 19, 20, 0, 0))

    def test_for_wrong_date_format(self):
        input_date = "2018-9-15"
        self.assertEqual(next_lottery_date(input_date), "input date format is not datetime type")

    def test_with_current_date(self):
        self.assertGreaterEqual(next_lottery_date(), datetime.datetime.now())


if __name__ == '__main__':
    unittest.main()
