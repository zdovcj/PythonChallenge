import collections
from dataModule import charset

counterDict = collections.OrderedDict()

for c in charset:
    if c in counterDict:
        counterDict[c] += 1;
    else:
        counterDict[c] = 1;

result = ""
for c in counterDict:
    if counterDict[c] < 5:
        result += c;

print("Result: ", result)
