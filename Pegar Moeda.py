import requests

url_key = 'sk_7kRhQJ4HVDWnE87xlpCA-cR9Jh-4h8h-8AaXp6Qnwl01QSC49hqTpAXcsP8sx'
moedas = input('Informe a moeda que quer consultar, exemplo USD-EUR (USD base e EUR destino) : ')

url = f'https://economia.awesomeapi.com.br/json/last/{moedas}?token={url_key}'
moeda = requests.get(url)
dados = moeda.json()

# O Sigla é a sigla da informação, por conta disso usamos sigla na primeira parte do FOR, já que usei o items;
# Depois, uso a informação para fazer a nomeclatura do for, que fica informacoes;
for sigla, informacoes in dados.items(): 
    print(f"\n--- Dados para {sigla} ---")

# Aqui, o isinstance ele verifica a variavel, no caso, ele lê informacoes e no dict ele retorna
# De forma que, retorno se é boleano ou não
    if isinstance(informacoes, dict): 
        for chave, valor in informacoes.items():
            print(f"{chave}: {valor}")
    else:
        print(f"Status: {informacoes}")

# Aqui é a mesma lógica, como usei items, eu falo qual item quero puxar (nesse caso a chave)e nomeio o for
# O segundo laço desmembra cada informação de dentro do bloco
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")