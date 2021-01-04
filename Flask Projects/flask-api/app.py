from flask import Flask, url_for, request, redirect, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb'
db = SQLAlchemy(app)
app.config['DEBUG'] = True

api_key = os.getenv('API_KEY')

class Weather(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Task %r>" % self.id

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        all_cities = Weather.query.order_by(Weather.date).all()
        weather = []
        for city in all_cities:
            weather.append(request.get(""))
        #response = request.get("api.openweathermap.org/data/2.5/weather?q={city name}&appid="+api_key)
        return render_template('weather.html')

if __name__ == "__main__":
    app.run()