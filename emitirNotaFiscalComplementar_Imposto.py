# coding=utf-8

# Informações da Nota Fiscal Complementar
#
# A Nota Fiscal Complementar é destinada para acrescentar dados e valores
# não informados no documento fiscal original. Utilizado para acréscimo no preço
# e quantidade da mercadoria ou somar valores faltantes dos impostos ICMS, ICMS-ST e IPI.
#
# OBS: Deve ser complementado o Preço/Quantidade OU Impostos.
# OB2: Caso deseje complementar as duas opções devem ser emitidas NF-e separadas.

# Biblioteca de comunicação http/https
import requests
# Biblioteca para manipulaçao de json
import json

# Busca o arquivo que contém o json para Complementar Nota Fiscal
with open('ExemploJson/complementarNotaFiscal_Imposto.json', 'r') as json_file:
   # Carrega o conteudo do arquivo e converte em array
   array = json.load(json_file)
   # Converte o array em json novamente
   json = json.dumps(array)

# Define o Host para a comunicação com a API
url = "https://webmaniabr.com/api/1/nfe/complementar/"

# Credenciais de acesso
headers = {
    'cache-control': "no-cache",
    'content-type': "application/json",
    'x-consumer-key': "SEU_CONSUMER_KEY",
    'x-consumer-secret': "SEU_CONSUMER_SECRET",
    'x-access-token': "SEU_ACCESS_TOKEN",
    'x-access-token-secret': "SEU_ACCESS_TOKEN_SECRET"
}

# Comunicando com a API
response = requests.request("PUT", url, data=json, headers=headers)

# Retorno da API
print(response.text)
