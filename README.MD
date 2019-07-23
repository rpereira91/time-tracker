
# Time Tracker 

  

## Description

I found myself with a lot of free time and a lot of hobbies I just felt like I would forget a lot of them and just end up doing nothing useful with my time. So I decided to write something that will help keep track of the smaller things I would often forget about. Right now it's only a CLI but the logic can be expanded to a web application or directly ported to mobile using React or something similar.

###EDIT: 2019-07-08
- Added flask front end and changed up how the data was stored/read. 

  

I was also trying to get better at using Pandas and Numpy for Data Processing so I figured this would be a fun way to get some practice.

## How to use it
Run the ```flask_time_page.py```
### Old
Add whatever activities you want to do in the ```actvities.csv``` file, I personally have my hobbies and random things I need to do (laundry, dishes, cleaning etc) but I'm usually too lazy to do. 

Once the activities are added to the list just run it and follow the instructions :D

It's pretty simple right now so there's not a lot to do in it. 

It creates a new log file each 

## Requirements

- Python (duh!)

- Pip (to install the libraries)

- Pandas

- Numpy

Just run ``` pip install -r requirements.txt ``` to install all the requirements

  

## TO DO

- Add the data processing stuff

	- Total time per week

	- Total time per day

	- Average time per day/week

	- Graphs (possibly using Seaborn or Matplotlib)

- Clean up the code a bit

- Input validation
- Add better logic for selecting a random activity, right now it's random but in the future it could be the activity done the least 