# coding=utf-8

# Status do Sefaz
#
# OBS: A utilização do endpoint deve ser realizada como demonstrativo do Status do
# Sefaz em sua plataforma, sendo necessário trabalhar com cache de ao menos 10 minutos.
# Não é necessário realizar a requisição antes da emissão de cada Nota Fiscal,
# porque este procedimento é realizado de forma automática em todos os endpoints.

# Biblioteca de comunicação http/https
import requests

# Define o Host para a comunicação com a API
url = "https://webmaniabr.com/api/1/nfe/sefaz/"

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
