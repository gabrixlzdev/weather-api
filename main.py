# Weather API - projeto do mês 1
# Consulta clima em tempo real pela OpenWeatherMap

from display import display_weather
from weather import get_weather, parse_weather
from history import save_to_history, show_history

def main():
    print('\n Wheather API')
    print(" Type 'history' to see past searches, 'quit' to exit\n")

    while True:             #loop infinito até o usuário digitar quit
        city = input(" Enter city: ").strip() #qual cidade .strip remove os espaços

        if city.lower() == "quit": #se a pessoa digitar quit aqui se encerra, .lower() transforma em minunculo
            break #quebra o loop
        
        if city.lower() == "history":
            show_history()
            continue #volta para o topo do loop

        if not city: #se o user clicou em enter sem digitar nada
            continue

        data = get_weather(city) #busca o clima
        
        if data:
            weather = parse_weather(data) #processa os dadoso
            display_weather(weather) #exibe no terminal
            save_to_history(weather) #salva no histórico

if __name__== "__main__":
    main() # só roda se você executar esse arquivo diretamente