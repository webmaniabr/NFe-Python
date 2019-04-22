# coding=utf-8

# Informações da Nota Fiscal Eletrônica
# Verificar emissaoNotaFiscal.py

# A Nota Fiscal de Ajuste é destinada somente para fins específicos de escrituração
# contábil para empresas de Lucro Normal ou Presumido, não representando saída ou entrada
# de produtos. Utilizado para nota de crédito de ICMS como transferência, ressarcimento
# ou restituição do ICMS.

# Biblioteca de comunicação http/https
import requests
# Biblioteca para manipulaçao de json
import json

# Busca o arquivo que contém o json para Ajuste de Nota Fiscal
with open('ExemploJson/emitirNotaFiscalAjuste.json', 'r') as json_file:
   # Carrega o conteudo do arquivo e converte em array
   array = json.load(json_file)
   # Converte o array em json novamente
   json = json.dumps(array)

# Define o Host para a comunicação com a API
url = "https://webmaniabr.com/api/1/nfe/ajuste/"

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