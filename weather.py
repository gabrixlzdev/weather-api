import requests
#A biblioteca requests serve para fazer chamadas HTTP — ou seja, buscar dados de outros servidores pela internet.
#Quando você acessa um site no navegador, 
#ele faz uma requisição HTTP pra um servidor e recebe uma resposta. O requests faz isso dentro do Python
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() #Lê o arquivo .env e carrega as variáveis dentro dele na memória. Precisa chamar isso antes de usar os.getenv() — se não chamar, a API key não é encontrada.
API_KEY = os.getenv("OPENWEATHER_API_KEY") #variável de ambiente para guardar a chave da API no .env, para não expor ela no código
BASE_URL = "https://api.openweathermap.org/data/2.5/weather" #URL base da API

def get_weather(city: str) -> dict | None:

    params = {
        "q": city, #cidade
        "appid": API_KEY, #chave da API
        "units": "metric", #unidade de temperatura em Celsius
        "lang": "en" #idioma da resposta
    }
    #É um dicionário com os parâmetros da requisição. O requests vai transformar isso na URL assim:
    #https://api.openweathermap.org/data/2.5/weather?q=CityName&appid=YourAPIKey&units=metric&lang=en

    try: #vamos tentar executar as seguintes linhas, mas se der algum erro, vamos tratar ele

        response = requests.get(BASE_URL, params=params, timeout = 5) #faz a requisição GET para a API
        # o timeout é o tempo máximo que o programa vai esperar pela resposta da API. Se passar disso, ele levanta um erro de timeout, que a gente pode tratar.
        # esse tempo é em segundos, então timeout=5 significa que se a API não responder em 5 segundos, o programa vai parar de esperar e levantar um erro.

        response.raise_for_status() #verifica se a resposta foi bem sucedida (status code 200)
        #Por padrão o requests não considera erro quando a API retorna 404 ou 500 — ele recebe a resposta e segue em frente

        return response.json() #retorna os dados em formato JSON (dicionário Python)
        #A API retorna os dados como texto. O .json() converte esse texto em um dicionário Python. 
        #Sem ele você teria uma string gigante impossível de usar.
    
    except requests.exceptions.HTTPError:
        #HTTPError — a API respondeu com erro, ex: cidade não encontrada (erro 404)

        print(f" City '{city}' not found. Please try again.")
        return None
    except requests.exceptions.ConnectionError:
        #ConnectionError — erro de conexão, ex: sem internet

        print(" Network error. Please check your connection.")
        return None

def parse_weather(data: dict) -> dict:
    #A API retorna um JSON enorme com dezenas de campos. Essa função extrai só o que você precisa e organiza num dicionário limpo.

    weather = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M") #a data do momento que foi feito a pesquisa, formatada como "2024-06-01 14:30"
    }
    return weather

