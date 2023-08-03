# make a code that reads the csv file.
# if the file not exests then make a new one
# if needed use try argument
# make sure that if the file is not exists return an ExceptionError
# if the date has been changed then store it in the file 
# make sure then when the date has been changed it calls back the new date
# same thing applies when changing the date to the past

from all_functions import *
from current_date import *
from rich.console import Console
import os
import argparse
import csv

console = Console()
current_date = CurrentDate(date.today())

class CsvReader:
    def __init__(self, filename):
        self.filename = filename

    def create_date_today(self):
        console.log(log_locals=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                new_current_date = date.today()
                file.write(str(new_current_date))
                print(f"This is the new date: {new_current_date}")
                
                return new_current_date
            
        elif os.path.exists(self.filename):
            with open(self.filename, "r") as changed_file:
                reader = csv.reader(changed_file)
                for line in reader:
                    date_object = datetime.strptime(line[0], "%Y-%m-%d").date()
                    print(f"This is the changed date: {date_object}")
                    
                    return date_object

    def change_forward(self,days):
        console.log(log_locals=True)
        current_date = CurrentDate(self.create_date_today())
        if os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                file.write(str(current_date.go_to_the_future(days)))
                print("Caution, the date has been changed")

                return current_date.time()

    def change_rewind(self,days):
        console.log(log_locals=True)
        current_date = CurrentDate(self.create_date_today())
        if os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                file.write(str(current_date.go_to_the_past(days)))
                print("Caution, the date has been changed")

                return current_date.time()
