# ✈️ Airline Market Demand Web App

A real-time analytics dashboard that visualizes trends in airline flight activity using data from the [Aviationstack API](https://aviationstack.com/), with AI-generated summaries powered by the **Gemini Pro** model from Google Generative AI.

> 🧪 This project was built as part of an internship evaluation task to demonstrate real-world problem-solving, API integration, and data-driven web app development.

Live Site: https://airline-demand-8ldi.onrender.com
---

## 📊 What It Does

This Python web app fetches **real-time flight data**, processes it to identify key insights in the airline market, and displays those insights via a clean, user-friendly dashboard.

### ✨ Key Insights Generated:
- **Top Flight Routes** (e.g., SYD → MEL)
- **Most Active Airlines**
- **Top Departure and Arrival Airports**
- **AI-generated market summaries** using Gemini Pro
- **Inferred price trends** for high-demand routes and airlines (via AI)

---

## 🛠️ Tech Stack

| Layer       | Technology                            |
|-------------|----------------------------------------|
| Backend     | Python, Flask                          |
| Frontend    | HTML, CSS, Jinja2 (Templating)         |
| Charting    | Plotly.js (Optional for visualizations)|
| APIs        | Aviationstack API, Gemini Pro API      |
| Environment | `python-dotenv` for loading `.env`     |

---

## 💡 Features

- ✅ Fetches real-time flight data from Aviationstack’s `/v1/flights` endpoint  
- ✅ Identifies:
  - Top 10 routes by flight volume  
  - Most active airlines  
  - Busiest departure and arrival airports  
- ✅ Converts raw IATA codes into full airport and airline names  
- ✅ Uses **Gemini Pro** to generate a professional, paragraph-style market report  
- ✅ Infers current **price trends** based on AI’s internet-based knowledge  
- ✅ Displays raw JSON data for transparency and debugging  


## .env 

- AVIATIONSTACK_API_KEY=your_aviationstack_key_here
- GEMINI_API_KEY=your_google_generative_ai_key_here
