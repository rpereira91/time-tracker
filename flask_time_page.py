from flask import Flask, request, flash, url_for, redirect, render_template, send_file
from TimeTracker import TimeTracker

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def display_hello():
	if request.method == 'POST':
		act_name = str(request.form.get('activities'))
		duration = int(request.form.get('duration'))
		tt.record_activity(act_name, duration)
	todays_totals = (tt.get_today_total())
	todays_sum = 0
	for total in todays_totals:
		todays_sum += total
	
	
	return render_template('index.html',
		acts=tt.get_acts(),total_min=todays_totals, min_sum = todays_sum)

@app.route('/add_act', methods=['GET', 'POST'])
def add_acts():
	if request.method == 'POST':
		act_name = str(request.form.get('new_act'))
		tt.add_activity(act_name)

	return render_template('add_acts.html',
		acts=tt.get_acts())
@app.route('/random_act', methods=['GET', 'POST'])
def random_act():
	if request.method == 'POST':
		return render_template('random_act.html',
		random_act=tt.do_random_act())

	return render_template('random_act.html',
	random_act=tt.do_random_act())
# @app.route('/plots/daily_breakdown', methods=['GET'])
# def daily_breakdown():    
#     return send_file(bytes_obj,
#                      attachment_filename='plot.png',
#                      mimetype='image/png')
if __name__ == "__main__":
    tt = TimeTracker()
    app.run(host= '127.0.0.1', port=5000, debug=True)