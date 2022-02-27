import json

bar_chart_data = './data/BarChart.json'
calendar_chart_data = './data/CalendarChart.json'
pie_chart_data = './data/PieChart.json'
radar_chart_data = './data/RadarChart.json'
radial_bar_chart_data = './data/RadialBarChart.json'

def get_bar_chart_data():
    with open(bar_chart_data) as file:
        return json.load(file)

def get_calendar_chart_data():
    with open(calendar_chart_data) as file:
        return json.load(file)

def get_pie_chart_data():
    with open(pie_chart_data) as file:
        return json.load(file)

def get_radar_chart_data():
    with open(radar_chart_data) as file:
        return json.load(file)

def get_radial_bar_chart_data():
    with open(radial_bar_chart_data) as file:
        return json.load(file)