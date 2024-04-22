import requests

urllist = []
isFollowed = {}

def checkurllist(URL):
    if URL in urllist:
        return True
    else:
        return False

def checkFollow(URL):
    for key in isFollowed.keys():
        if key != URL:
            return False
        else:
            if isFollowed[URL] == "yes":
                return True
            else:
                return False

URL = ("https://www.columbia.edu/~fdc/sample.html")

urllist.append(URL)


for URL in urllist:
    if checkFollow(URL) != True:
        page = requests.get(URL)
        isFollowed[URL] = "yes"
        start = "http"
        for line in page.text.split("\n"):
            if "http" in line:
                #print(line)
                if "\">" in line:
                    end = "\">"
                elif "&gt;" in line:
                    end = "&gt;"
                elif " +" in line:
                    end = " +"
                else:
                    end = "</tt>"
                sliced = (line[line.index(start):line.index(end)])
                if "&gt;" in sliced:
                    end = "&gt;"
                    parsed = sliced[sliced.index(start):sliced.index(end)]
                else:
                    parsed = sliced
                #print(parsed)
                if checkurllist(parsed) == False:
                    urllist.append(parsed)
                    isFollowed[parsed] = "no"

for URL in urllist:
    print(URL)