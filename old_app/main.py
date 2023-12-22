from flask import Flask, render_template, Request
from flask_htmx import HTMX
import os
import pandas as pd

app = Flask(__name__)
htmx = HTMX(app)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
df = pd.read_csv(os.path.join(DATA_DIR, 'laurier_courses.csv'), index_col=['school', 'title'])

@app.route('/')
def index():
    return render_template('index.html', courses=df.to_records())

@app.route('/schools/<school>')
def school(school: str):
    return render_template('index.html', school=school, courses=df.loc[school].to_records())

@app.route('/schools/<string:school>/courses/<string:courseName>')
def classId(school: str, courseName: str):
    course: dict = df.loc[school, courseName].to_dict()

    return render_template('course.html', school=school, title=courseName, course=course)

if __name__ == '__main__':
    app.run(debug=True)