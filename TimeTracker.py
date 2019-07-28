import pandas as pd
import numpy as np
import random
from datetime import datetime
# import matplotlib.pyplot as plt

import os.path
from os import path
import io

class TimeTracker(object):
    """docstring for TimeTracker."""
    def __init__(self):
        self.file_name = "Logs/activity_log.csv"
        self.log_file = pd.read_csv(self.file_name)
        self.log_file.sort_values(by=['date'], ascending=False, inplace=True)
        self.set_today()
        #if this is the first time program is started today add todays date
        

    def set_today(self):
        self.today = datetime.today().strftime('%Y-%m-%d')
        if (self.log_file.loc[self.log_file['date'] == self.today]).empty:
            self.log_file = self.log_file.append({'date':self.today}, ignore_index=True)
            self.save_file()

    def save_file(self):
        self.log_file.fillna(0.0, inplace=True)
        self.log_file.to_csv(self.file_name, index=False)

    
    def add_activity(self, activity_name):
        self.log_file[activity_name] = 0.0
        self.save_file()
    def remove_activity(self, activity_name):
        self.log_file.drop(activity_name, axis=1, inplace=True)
        self.save_file()
    def do_random_act(self):
        all_Acts = self.get_acts()
        return (all_Acts[random.randint(0,len(all_Acts)-2)])
    def show_log(self):
        print (self.log_file.head(7))

    def record_activity(self, act_no, duration):
        self.set_today()
        self.log_file.loc[self.log_file['date'] == self.today , act_no] += duration
        self.save_file()

    def get_acts(self):
        return list(self.log_file.columns[1:])

    def get_today_total(self):
        return (self.log_file.loc[self.log_file['date'] == self.today,self.get_acts()].sum())

    def get_all_act_total(self):
        totals = []
        for act in self.get_acts():
            totals.append(self.get_act_total(act))
        return totals

    def get_act_total(self, act_name=""):
        return (int(self.log_file[act_name].sum()))

    def show_act_totals(self):
        acts = self.get_acts()
        y_pos = np.arange(len(acts))
        performance = self.get_acts()

        plt.bar(y_pos, self.get_all_act_total(), align='center', alpha=0.5)
        plt.xticks(y_pos, self.get_acts())
        plt.ylabel('Activities')
        plt.title('Time spent (minutes)')

        plt.show()
if __name__ == "__main__":
    tt = TimeTracker()
    tt.show_log()
    # tt.record_activity('act_2',20)
    # tt.record_activity('act_5',40)
    tt.show_act_totals()
    

        