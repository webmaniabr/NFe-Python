# coding=utf-8

# Consulta de Nota fiscal
#
# Atenção: Somente é permitido consultar a chave da nota fiscal emitida pelo
# emissor da WebmaniaBR, não sendo possível consultar nota fiscal de terceiro
# ou emitida em outro sistema.

# Biblioteca de comunicação http/https
import requests
# Biblioteca para manipulaçao de json
import json

# Busca o arquivo que contém o json para Consulta de Nota Fiscal
with open('ExemploJson/consultarNotaFiscal.json', 'r') as json_file:
   # Carrega o conteudo do arquivo e converte em array, que pode ser passado diretamente como parametro no momento da requisição
   array = json.load(json_file)

# Define o Host para a comunicação com a API
url = "https://webmaniabr.com/api/1/nfe/consulta/"

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
response = requests.request("GET", url, headers=headers, params=array)

# Retorno da API
print(response.text)
