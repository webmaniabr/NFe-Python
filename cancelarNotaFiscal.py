# coding=utf-8

# Cancelar Nota Fiscal
#
# Atenção: Somente poderá ser cancelada uma NF-e cujo uso tenha sido previamente
# autorizado pelo Fisco e desde que não tenha ainda ocorrido o fato gerador, ou seja,
# ainda não tenha ocorrido a saída da mercadoria do estabelecimento. Atualmente o prazo
# máximo para cancelamento de uma NF-e é de 24 horas (1 dia), contado a partir da autorização
# de uso. Caso já tenha passado o prazo de 24 horas ou já tenha ocorrido a circulação da
# mercadoria, emita uma NF-e de devolução para anular a NF-e anterior.

# Biblioteca de comunicação http/https
import requests
# Biblioteca para manipulaçao de json
import json

# Busca o arquivo que contém o json para Cancelamento de Nota Fiscal
with open('ExemploJson/cancelarNotaFiscal.json', 'r') as json_file:
   # Carrega o conteudo do arquivo e converte em array
   array = json.load(json_file)
   # Converte o array em json novamente
   json = json.dumps(array)

# Define o Host para a comunicação com a API
url = "https://webmaniabr.com/api/1/nfe/cancelar/"

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
