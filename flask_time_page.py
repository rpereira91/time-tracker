from flask import Flask, request, flash, url_for, redirect, render_template, send_file
from time_tracker import TimeTracker

app = Flask(__name__)

week_day_totals = []
@app.route('/')
def display_hello():
    return render_template('index.html', 
        totals=tt.get_day_totals())

@app.route('/plots/daily_breakdown', methods=['GET'])
def correlation_matrix():
    bytes_obj = tt.show_daily_totals()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')
if __name__ == "__main__":
    tt = TimeTracker()
    app.run()