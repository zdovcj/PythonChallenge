import pickle


f = open("banner.p", "r")
fileString = f.read()
loadResult = pickle.loads(fileString.encode())

for i in loadResult:
    line = ""
    for a in i:
        line += a[0]*a[1]
    print(line)
    
    