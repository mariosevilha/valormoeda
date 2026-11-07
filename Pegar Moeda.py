import requests

url_key = 'sk_7kRhQJ4HVDWnE87xlpCA-cR9Jh-4h8h-8AaXp6Qnwl01QSC49hqTpAXcsP8sx'
moedas = input('Qual moeda quer saber? ')

url = f'https://economia.awesomeapi.com.br/json/last/{moedas}?token={url_key}'
moeda = requests.get(url)
dados = moeda.json()
lista_siglas = list(dados.keys())
lista_nomes = list(dados.values())
print(lista_nomes , lista_siglas)