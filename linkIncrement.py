import requests


i = 1

while i < 50:
    url = "http://www.something.com:8080/" + str(i) + ".html"
    response = requests.get(url)
    print(response.text)
    i += 1