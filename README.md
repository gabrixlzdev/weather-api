# Weather API CLI

A command-line tool that fetches real-time weather data for any city using the OpenWeatherMap API.

## Features
- Current temperature, humidity, wind speed and description
- Search history saved locally (last 20 searches)
- Error handling for invalid cities and connection issues

## Stack
Python 3.14 · requests · python-dotenv

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