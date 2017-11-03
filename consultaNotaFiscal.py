import requests

url = "https://webmaniabr.com/api/1/nfe/consulta/"

querystring = {"chave":"45150819652219000198550990000000011442380343","ambiente":"1"}

headers = {
    'cache-control': "no-cache",
    'content-type': "application/json",
    'x-consumer-key': "SEU_CONSUMER_KEY",
    'x-consumer-secret': "SEU_CONSUMER_SECRET",
    'x-access-token': "SEU_ACCESS_TOKEN",
    'x-access-token-secret': "SEU_ACCESS_TOKEN_SECRET"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
