import datetime


# Calculating next valid draw date
# The Irish lottery draw takes place twice weekly on a Wednesday and a Saturday at 8pm. Write a
# function that calculates and returns the next valid draw date based on an optional supplied date
# time parameter. If no supplied date is provided, assume current date time

def next_valid_draw(input_date=datetime.datetime.today()):
    """
    input_date: date format input
    return: date for next valid draw
    """

    # For Wednesday and Saturday
    valid_week_day_count_1 = 3
    valid_week_day_count_2 = 6
    try:
        # Get week day from input date, add one to make week days count correct
        day_num = int(input_date.weekday()) + 1

        if day_num == valid_week_day_count_1 or day_num == valid_week_day_count_2:
            return datetime.datetime.combine(input_date.date(), datetime.time(20, 00))
        else:
            if day_num < valid_week_day_count_1:
                return datetime.datetime.combine(
                    (input_date + datetime.timedelta(days=(valid_week_day_count_1 - day_num))).date(),
                    datetime.time(20, 00))

            elif day_num < valid_week_day_count_2:
                return datetime.datetime.combine(
                    (input_date + datetime.timedelta(days=(valid_week_day_count_2 - day_num))).date(),
                    datetime.time(20, 00))

            # case to handle weekday is 7(Sunday)
            else:
                return datetime.datetime.combine((input_date + datetime.timedelta(days=3)).date(),
                                                 datetime.time(20, 00))
    except AttributeError as ex:
        return "input date format is wrong"


#############################Unit Test cases###################
# Test case 01: Check for current date
result = next_valid_draw()
print(result)
# To assert with current date, uncomment below line and update expected date and execute it.
# assert str(result) == str('2018-09-08 20:00:00')

# Test case 02: Check for before Wednesday
t = datetime.datetime(2018, 9, 3)
result = next_valid_draw(t)
assert str(result) == str('2018-09-05 20:00:00')

# Test case 03: Check for after Wednesday
t = datetime.datetime(2018, 9, 6)
result = next_valid_draw(t)
assert str(result) == str('2018-09-08 20:00:00')

# Test case 04: Check for after Sunday
t = datetime.datetime(2018, 9, 9)
result = next_valid_draw(t)
assert str(result) == str('2018-09-12 20:00:00')

# Test case 04: Check for different month
t = datetime.datetime(2018, 9, 30)
result = next_valid_draw(t)
assert str(result) == str('2018-10-03 20:00:00')

# Test case 05: Check for different year
t = datetime.datetime(2018, 12, 31)
result = next_valid_draw(t)
assert str(result) == str('2019-01-02 20:00:00')

# Test case 06: Check for wrong date format
result = next_valid_draw('2018')
assert result == 'input date format is wrong'
