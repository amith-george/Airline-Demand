from flask import Flask, render_template
from utils.scraper import fetch_flight_data
from utils.processor import analyze_flights
from utils.insights import get_ai_insights  # NEW

app = Flask(__name__)

@app.route('/')
def home():
    # Fetch and analyze data
    flights = fetch_flight_data(limit=100)
    results = analyze_flights(flights)

    # Generate Gemini AI insight if no error
    insights = ""
    if not results.get("error"):
        insights = get_ai_insights(results)

    return render_template('index.html', results=results, insights=insights)

if __name__ == '__main__':
    app.run(debug=True)
