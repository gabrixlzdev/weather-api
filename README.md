# Weather API CLI

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Status](https://img.shields.io/badge/status-complete-brightgreen)

A command-line tool that fetches real-time weather data for any city using the OpenWeatherMap API.

## Demo

Weather API
Type 'history' to see past searches, 'quit' to exit
Enter city: Indaiatuba
City: Indaiatuba
Temp: 24.16°C — clear sky
Humidity: 49%
Wind: 3.29 m/s
Time: 2026-04-20 10:22
Enter city: history
--- Last Searches ---
2026-04-20 10:17 | São Paulo | 22.15°C
2026-04-20 10:22 | Indaiatuba | 24.16°C

## Features
- Real-time weather data for any city in the world
- Temperature, humidity, wind speed and conditions
- Search history saved locally (last 20 searches)
- Error handling for invalid cities and connection issues
- API key protected via environment variables

## Stack
Python 3.14 · requests · python-dotenv

## Project Structure

weather-api/
├── main.py        # main loop and program flow
├── weather.py     # API calls and data parsing
├── display.py     # terminal output formatting
├── history.py     # save and load search history
├── .env           # API key (not included in repo)
└── .gitignore

## How to run

1. Clone the repo
   git clone https://github.com/seu-usuario/weather-api

2. Install dependencies
   pip install requests python-dotenv

3. Create a `.env` file with your API key
   OPENWEATHER_API_KEY=your_key_here

4. Run
   python main.py

## Commands
- Type a city name to get current weather
- Type `history` to see last 5 searches
- Type `quit` to exit

## API Reference
OpenWeatherMap Current Weather — openweathermap.org/current