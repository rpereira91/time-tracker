
# Time Tracker 

  

## Description

&nbsp; &nbsp; &nbsp; This started off with a friend asking me a very simple question, a question I didn’t have a good answer for. He asked me, “What do you do with your free time?”. I have a lot of hobbies but I don’t really do anything consistently enough to answer that question. So for the week after he asked me that questionI timed and recorded all my after work activities. The results were...disappointing at best. I was very inconsistent with my time, spending most of it watching tv or deciding what I want to do next. 
&nbsp; &nbsp; &nbsp; With that week done I tried writing a small CLI in Python where I can record all my activities. The first iteration of this application created a new csv file per week with the days separated per column, I found this great for keeping a week to week log of my activities, but I became more interested in keeping track of a large scale time frame. So if I wanted to check a years worth of activities I would have to parse through 52 csv files. This probably isn’t a great way to keep track of things. 
&nbsp; &nbsp; &nbsp;The second iteration of this app I moved it to one CSV file with each new row representing a date and the activities stored in a column. Storing it this way let me get a large scale idea of my time spent. Now I don't record my activities every day, so it won't be 100% accurate, but it’s close. I was also trying to get better at using Pandas and Numpy for Data Processing so I figured this would be a fun way to get some practice.
&nbsp; &nbsp; &nbsp; To make it all easier to use I added a FLASK front end to display the data. 


## How to use it
- First time:
    - Run ```pip install -r requirements.txt```
    - Run ```flask_time_page.py```
    - Go to localhost:5000/add_act
    - Add whatever you want
- Any time after that:
    - Run ```flask_time_page.py```
    - Track whatever you want

## Requirements

- Python (duh!)
- Pip (to install the libraries)
- Pandas
- Numpy
- Flask

Just run ``` pip install -r requirements.txt ``` to install all the requirements (assuming you have pip installed...)

  

## TO DO

- Add the data processing stuff

	- Total time per week

	- Total time per day

	- Average time per day/week

	- Graphs (possibly using Seaborn or Matplotlib)

- Clean up the code a bit
- Add better logic for selecting a random activity, right now it's random but in the future it could be the activity done the least 