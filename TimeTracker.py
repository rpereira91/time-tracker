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
        self.today = datetime.today().strftime('%Y-%m-%d')
        self.file_name = "Logs/activity_log.csv"
        self.log_file = pd.read_csv(self.file_name)
        self.log_file.sort_values(by=['date'], ascending=False, inplace=True)
        #if this is the first time program is started today add todays date
        if (self.log_file.loc[self.log_file['date'] == self.today]).empty:
            self.log_file = self.log_file.append({'date':self.today}, ignore_index=True)
            self.log_file.fillna(0, inplace=True)
            self.log_file.to_csv(self.file_name, index=False)
        print(self.log_file)

    def record_activity(self, act_no, duration):
        #get the name of the current activity to display it
        current_duration = self.log_file.loc[self.log_file['date'] == self.today][act_no] + duration
        self.log_file.loc[self.log_file['date'] == self.today][act_no] = current_duration
        self.log_file.at[date[0], act_no] = current_duration
        print(self.log_file)

if __name__ == "__main__":
    tt = TimeTracker()
    tt.record_activity('act_1', 20)

        