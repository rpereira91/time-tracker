import pandas as pd
import numpy as np
import random
from datetime import datetime

import os.path
from os import path

class TimeTracker(object):
    def __init__(self):
        self.activities = pd.read_csv("activities.csv")
        self.today = datetime.today()
        self.file_name = "Logs\Week_"+str(self.today.isocalendar()[1])+".csv"
        
        self.set_log()


    def set_log(self):
        if path.exists(self.file_name):
            self.log_file = pd.read_csv(self.file_name)
        else:
            f = open(self.file_name, "w+")
            f.write("activity_name,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday, Sunday\n")
            for a in self.activities['activity_name']:
                f.write(a+",0,0,0,0,0,0,0\n")
            f.close()
            self.log_file = pd.read_csv(self.file_name)
    
    def record_activity(self, act_no, duration):
        current_act = self.activities['activity_name'][act_no]
        print("Activity Name: {} Duration: {}".format(current_act,duration))
        self.log_file.ix[act_no,(self.today.weekday()+1)] += duration
        self.log_file.to_csv(self.file_name, index=False)

    def pick_random(self, max_time=30, quick = False):
        rand_act = random.randint(0,len(self.activities)-1)
        if quick:
            self.record_activity(rand_act,5)
        else:
            duration = np.random.choice((np.arange(5,max_time+1,5)))
            self.record_activity(rand_act,duration )
        # Print out the activity
        # current_act = self.activities['activity_name'][rand_act]
        # print("Do {} for {} minutes".format(current_act, duration))
        # gets the same result but looks sloppier imo
        # print("Do {} for {} minutes".format(self.activities['activity_name'][random.randint(0,len(self.activities)-1)], np.random.choice((np.arange(5,max_time+1,5)),1)))
     
    def print_log(self):
        print(self.log_file)
    
    # Data Processing 
    #get the total minutes for the week
    def get_total(self):
        return True
    #get the totals per day
    def get_day_totals(self):
        return True
    #get the hours for the day
    def get_daily_hours(self):
        return True
    # get the total average 
    def get_total_average(self):
        return True
    #get the average for the days
    def get_daily_average(self):
        return True

if __name__ == "__main__":
    tt = TimeTracker()
    # tt.record_activity(0,10)
    # tt.record_activity(2,10)
    tt.print_log()
    tt.pick_random(quick=True)
    tt.print_log()
    tt.get_total()
        