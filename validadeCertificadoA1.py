# coding=utf-8

# Biblioteca de comunicação http/https
import requests

# Define o Host para a comunicação com a API
url = "https://webmaniabr.com/api/1/nfe/certificado/"

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
response = requests.request("GET", url, headers=headers)

# Retorno da API
print(response.text)
