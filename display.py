def display_weather(weather: dict) -> None:  #weather: dict é uma type hint — uma anotação que diz qual tipo de dado a função espera receber.
    print(f"\n  📍 {weather['city']}")
    print(f"  🌡  {weather['temp']}°C — {weather['description']}")
    print(f"  💧 Humidity: {weather['humidity']}%")
    print(f"  💨 Wind: {weather['wind_speed']} m/s")
    print(f"  🕒 {weather['timestamp']}\n")

# -> None: significa que não retorna nada nessa função 