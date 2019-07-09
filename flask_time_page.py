from flask import Flask, request, flash, url_for, redirect, render_template, send_file
from TimeTracker import TimeTracker

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def display_hello():
	if request.method == 'POST':
		act_name = str(request.form.get('activities'))
		duration = int(request.form.get('duration'))
		tt.record_activity(act_name, duration)

	return render_template('index.html',
		acts=tt.get_acts())

# @app.route('/plots/daily_breakdown', methods=['GET'])
# def daily_breakdown():    
#     return send_file(bytes_obj,
#                      attachment_filename='plot.png',
#                      mimetype='image/png')
if __name__ == "__main__":
    tt = TimeTracker()
    app.run(host= '127.0.0.1', port=5000, debug=True)