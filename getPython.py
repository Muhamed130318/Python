import requests

url = "http://www.offensive-security.com:8080"

response = requests.get(url)

print(response.status_code)