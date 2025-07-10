from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    
    # 🔁 Simulated weather data (instead of real API call)
    weather_data = {
        'city': city,
        'temperature': '25°C',
        'description': 'Partly cloudy',
        'humidity': '60%',
        'wind_speed': '15 km/h'
    }

    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)

