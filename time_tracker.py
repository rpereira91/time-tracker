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
        self.set_log()


    def set_log(self):
        file_name = "Logs\Week_"+str(self.today.isocalendar()[1])+".csv"
        if path.exists(file_name):
            self.log_file = pd.read_csv(file_name)
        else:
            f = open(file_name, "w+")
            f.write("activity_name,0,1,2,3,4,5,6\n")
            for a in self.activities['activity_name']:
                f.write(a+",\n")
            f.close()
            self.log_file = pd.read_csv(file_name)
        self.log_file.set_index(self.log_file['activity_name'])
    
    def record_activity(self, act_no, duration):
        current_act = self.activities['activity_name'][act_no]
        print("Activity Name: {} Duration: {}".format(current_act,duration))
        print(self.log_file)

    def pick_random(self, max_time=30):
        rand_act = random.randint(0,len(self.activities)-1)
        current_act = self.activities['activity_name'][rand_act]
        durations = (np.arange(5,max_time+1,5))
        print("Do {} for {} minutes".format(current_act, np.random.choice(durations,1)))
        # gets the same result but looks sloppier imo
        # print("Do {} for {} minutes".format(self.activities['activity_name'][random.randint(0,len(self.activities)-1)], np.random.choice((np.arange(5,max_time+1,5)),1)))
     
    def print_activities(self):
        print(self.activities)
        return True

if __name__ == "__main__":
    tt = TimeTracker()
    tt.record_activity(0,10)
    tt.print_activities()
    tt.pick_random()
        