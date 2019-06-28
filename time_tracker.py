# You don't need to use pandas or numpy for this but it's something I was trying to practice using more so I used it here
import pandas as pd
import numpy as np
import random
from datetime import datetime

import os.path
from os import path
# time tracker class
class TimeTracker(object):
    def __init__(self):
        #get the base activities, these are used to create the log file if the log file doesn't exist
        # new activities will be added at the end of the week once a new file is created
        self.activities = pd.read_csv("activities.csv")
        #get todays date for any use down the line 
        self.today = datetime.today()
        # create the log file with todays week number
        self.file_name = "Logs\Week_"+str(self.today.isocalendar()[1])+".csv"
        # week day array with the names for log file creation and used to display shit if we need to
        self.weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']
        #create the log file or set the log file variable 
        self.set_log()


    def set_log(self):
        #if the file exists read the file and store it in a dataframe called log file
        if path.exists(self.file_name):
            self.log_file = pd.read_csv(self.file_name)
        else:
            #create the log file for the week if one doesn't exist 
            # there's probably an easier way to make this but I'm lazy
            f = open(self.file_name, "w+")
            f.write("activity_name")
            for w in self.weekdays:
                f.write(','+w)
            f.write("\n")
            for a in self.activities['activity_name']:
                f.write(a+",0,0,0,0,0,0,0\n")
            f.close()
            #the log file is recorded 
            self.log_file = pd.read_csv(self.file_name)
    #record an activity, the activity number is passed in along with the duration worked 
    def record_activity(self, act_no, duration):
        #get the name of the current activity to display it
        current_act = self.activities['activity_name'][act_no]
        #print out the activity and the duration
        print("Activity Name: {} Duration: {}".format(current_act,duration))
        #edit the log file with the new duration
        self.log_file.ix[act_no,(self.today.weekday()+1)] += duration
        # write the dataframe to the log file
        self.log_file.to_csv(self.file_name, index=False)

    #pick a random activity, right now it's randomly selected but down the line it 
    # would be useful to use some kind of algorithm to pick the activity done the least or something
    # passed variables are the max time you want to work for and if you just want to do a quick activity or not
    def pick_random(self, max_time=30, quick = False):
        # pick a random activity you want to do from the list
        rand_act = random.randint(0,len(self.activities)-1)
        #if you only want to do something quickly it will do it for 5 minutes 
        if quick:
            self.record_activity(rand_act,5)
        # if you want to do a longer activity create an array of timers from 5 minutes to the max time with 5 minute intervals 
        #  (np.arange(5,max_time+1,5) 
        # pick one of the elements from the array
        #  np.random.choice
        else:
            duration = np.random.choice((np.arange(5,max_time+1,5)))
            self.record_activity(rand_act,duration )

        # Print out the activity, used earlier for debugging
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
        