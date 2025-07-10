from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return jsonify({'error': 'City not found'}), 404

    weather_info = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
    }
    return jsonify(weather_info)
