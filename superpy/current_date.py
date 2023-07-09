from all_functions import *

from datetime import timedelta, date

# 09-07-2023 code works on the CLI just need to adjust the code with strftime and strptime
# also make sure you can adjust the date in the CLI

class CurrentDate:

    def __init__(self, today):
        self.today = today

    def time(self):
        return self.today

    def go_to_the_future(self, days):
        return self.today + timedelta(days=days)

    def go_to_the_past(self, days):
        return self.today - timedelta(days=days)