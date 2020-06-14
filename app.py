from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from weather import weather_here
import os


host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Playlister')
client = MongoClient(host=f'{host}?retryWrites=false')
app = Flask(__name__)

db = client.get_default_database()
weather = db.weather
moods = db.moods

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/mood', methods=['POST'])
def mood_post():
    mood_id = request.form.get('my_mood')
    mood = {
        'mood': request.form.get('my_mood')
    }
    return redirect(url_for('index'))

@app.route('/weather')
def weather_display():
    weather = weather_here()
    return render_template('weather_info.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
