'''
JSON request:

{
  "chave":"45150819652219000198550990000000011442380343",
  "correcao":"O CFOP correto é 5.102 referente a revenda tributada no mesmo estado.",
  "ambiente":1
}
'''

import requests

url = "https://webmaniabr.com/api/1/nfe/cartacorrecao/"

payload = "{\"chave\": \"45150819652219000198550990000000011442380343\",\"correcao\": \"O CFOP correto é 5.102 referente a revenda tributada no mesmo estado.\",\"ambiente\": \"1\"}"
headers = {
    'cache-control': "no-cache",
    'content-type': "application/json",
    'x-consumer-key': "SEU_CONSUMER_KEY",
    'x-consumer-secret': "SEU_CONSUMER_SECRET",
    'x-access-token': "SEU_ACCESS_TOKEN",
    'x-access-token-secret': "SEU_ACCESS_TOKEN_SECRET"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
