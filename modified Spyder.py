import requests

urllist = []

def checkurllist(url):
    if url in urllist:
        return True
    else:
        return False
    
url = "http://192.168.198.68:8080/crawling"

response = requests.get(url)
output = response.content.decode()

start = "crawling"
end = "\" "

for line in output.split("\n"):
    if "a href" in line:
        parsed = (line[line.index(start):line.index(end)])
        link = "http://192.168.198.68:8080/" + parsed
        if checkurllist(link) == False:
            urllist.append(link)

for url in urllist:
    resp = requests.get(url)
    out = resp.content.decode()
    print(out)