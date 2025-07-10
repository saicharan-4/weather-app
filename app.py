from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def load_data():
    df = pd.read_csv('weather_data.csv')
    return df.to_dict(orient='records')

@app.route('/')
def index():
    weather_data = load_data()
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
