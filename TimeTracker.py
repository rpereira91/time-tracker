import pandas as pd
import numpy as np
import random
from datetime import datetime
import matplotlib.pyplot as plt

import os.path
from os import path
import io

class TimeTracker(object):
    """docstring for TimeTracker."""
    def __init__(self):
        self.set_today()
        self.file_name = "Logs/activity_log.csv"
        self.log_file = pd.read_csv(self.file_name)
        self.log_file.sort_values(by=['date'], ascending=False, inplace=True)
        #if this is the first time program is started today add todays date
        if (self.log_file.loc[self.log_file['date'] == self.today]).empty:
            self.log_file = self.log_file.append({'date':self.today}, ignore_index=True)
            self.save_file()

    def set_today(self):
        self.today = datetime.today().strftime('%Y-%m-%d')

    def save_file(self):
        self.log_file.fillna(0, inplace=True)
        self.log_file.to_csv(self.file_name, index=False)

    
    def add_activity(self, activity_name):
        self.log_file[activity_name] = 0.0
        self.save_file()
    def remove_activity(self, activity_name):
        self.log_file.drop(activity_name, axis=1, inplace=True)
        self.save_file()
    def show_log(self):
        print (self.log_file.head(7))

    def record_activity(self, act_no, duration):
        self.log_file.loc[self.log_file['date'] == self.today , act_no] += duration
        self.save_file()

    def get_acts(self):
        return list(self.log_file.columns[1:])

    def get_today_total(self):
        print(self.log_file.loc[self.log_file['date'] == self.today])
        
if __name__ == "__main__":
    tt = TimeTracker()
    tt.show_log()
    # tt.record_activity('act_2',20)
    # tt.record_activity('act_5',40)
    print(tt.get_acts())

        