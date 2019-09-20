import datetime

import time


def countdown_timer(hours):
    delta = datetime.timedelta(hours=hours)
    past_time = datetime.datetime.now() - delta
    seconds_decrement = 1
    while True:
        ticker = past_time - datetime.timedelta(seconds=seconds_decrement)
        print("{}:{}:{}".format(ticker.hour, ticker.minute, ticker.second))
        seconds_decrement += 1
        time.sleep(1)


if __name__ == '__main__':
    decrement_units = 1
    countdown_timer(decrement_units)
