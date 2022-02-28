from flask import Flask, jsonify
from flask_cors import CORS
import service

app = Flask(__name__)
CORS(app)

@app.route('/data/bar-chart')
def bar():
    return jsonify(service.get_bar_chart_data())

@app.route('/data/calendar-chart')
def calendar():
    return jsonify(service.get_calendar_chart_data())

@app.route('/data/pie-chart')
def pie():
    return jsonify(service.get_pie_chart_data())

@app.route('/data/radar-chart')
def radar():
    return jsonify(service.get_radar_chart_data())

@app.route('/data/radial-bar-chart')
def radial():
    return jsonify(service.get_radial_bar_chart_data())

if __name__ == "__main__":
    app.run()
