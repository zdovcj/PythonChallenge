from urllib.request import urlopen
import re

urlTemplate = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d"
index = 12345

print(urlTemplate%(index))

while(1):
    url = urlTemplate%(index)
    response = str(urlopen(url).read())
    print(response)
    match = re.findall(r"and the next nothing is (\d+)", response)

    try:
        index = int(match[0])
        url = urlTemplate
    except:
        break

index = 16044 / 2
while(1):
    url = urlTemplate%(index)
    response = str(urlopen(url).read())
    print(response)
    match = re.findall(r"and the next nothing is (\d+)", response)

    try:
        index = int(match[0])
        url = urlTemplate
    except:
        break