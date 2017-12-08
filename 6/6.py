import zipfile
import re

archive = zipfile.ZipFile("channel.zip")


for name in archive.namelist():
    #print(archive.getinfo(name))
    archive.extract(name, "channel/")


index = 90052

result = ""
while(1):
    f = open("channel/%d.txt"%(index))
    inside = f.read()
    comment = archive.getinfo(str(index)+".txt").comment
    print(inside, comment)
    result += comment.decode("utf-8");
    f.close()
    match = re.findall("Next nothing is (\d+)", inside)
    try:
        index = int(match[0])
    except:
        break
    

print(result)