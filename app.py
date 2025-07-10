from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data
df = pd.read_csv('weather_data.csv')

@app.route('/')
def index():
    city = request.args.get('city', '')
    date = request.args.get('date', '')
    filtered_df = df

    if city:
        filtered_df = filtered_df[filtered_df['city'].str.lower() == city.lower()]
    if date:
        filtered_df = filtered_df[filtered_df['date'] == date]

    return render_template('index.html', tables=filtered_df.to_html(classes='data', index=False), city=city, date=date)

if __name__ == '__main__':
    app.run(debug=True)
