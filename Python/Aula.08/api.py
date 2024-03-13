import requests 

cep = "40270240"

try:
    response = requests.get("http://cep.awesomeapi.com.br/json/40270240")

except requets.exceptions.RequestExpetion as e:
    print(e)
    
    