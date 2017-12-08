import re
from dataModule import charset

key = r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"

results = re.findall(key, charset)

print("Result:","".join(results))