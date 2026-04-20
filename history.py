import json
import os
from datetime import datetime

HISTORY_FILE = "history.json" #constantes que nunca mudam inscrita em maiúsculo

def save_to_history (weather: dict) -> None:
    history = load_history() #carrega o histórico 
    history.append(weather) #adiciona a última pesquisa

    with open(HISTORY_FILE, "w") as f: #w significa abrir o arquivo no modo escrita e o arquivo vai chamar f
        json.dump(history[-20:], f, indent=2) #para guardar só as últimas 20 pesquisas
        #O [-20:] é uma slice — um recorte de lista.
        #A sintaxe é sempre [início:fim]. Quando você omite o fim, ele vai até o final da lista.
        #history[0:5] do índice 0 até o 4 — primeiros 5
        # indent é formatar o arquivo json com espaçmento legível
        #O with open(...) as f é um jeito seguro de abrir arquivos — ele fecha automaticamente quando termina, mesmo se der erro.
        #o que salvar → history[-20:]
        #onde salvar → f (o arquivo aberto)

def load_history() -> list:
    #O os.path é um conjunto de ferramentas para trabalhar com caminhos de arquivos e pastas

    if not os.path.exists(HISTORY_FILE): # verifica se não existe retorna true or false
        return [] # se não existir retorna lista vazia
    
    with open(HISTORY_FILE, "r") as f: #se exisitir abre no modo leitura
        return json.load(f) # retorna seu conteudo
    
def show_history() -> None:
    history = load_history() #carrega o histórico
    
    if not history: #se estiver vazia
        print(" No history yet.")
        return
    
    print("\n ---Last Searches---")
    for entry in history [-5:]: #percorre somente os 5 últimos itens
        print (f"   {entry['timestamp']} | {entry['city']} | {entry['temp']}°C | humidity: {entry['humidity']}%")
    print()
    #Cada entry é um dicionário — por isso acessa com entry['city'], entry['temp'] etc.

# jeito atual
#if not history:

# equivalente com len
#if len(history) == 0:

# equivalente comparando com lista vazia
#if history == []: