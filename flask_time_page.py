from flask import Flask, request, flash, url_for, redirect, render_template
from time_tracker import TimeTracker

app = Flask(__name__)


@app.route('/')
def display_hello():
    return render_template('index.html')

if __name__ == "__main__":
    tt = TimeTracker()
    app.run()