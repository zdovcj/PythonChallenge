def remap(s):
    outputString = ""
    for c in s:
        numerical = ord(c)
        if numerical >= 97 and numerical <= 124:
            numerical += 2
            if numerical > 122:
                numerical -= 26
            outputString += chr(numerical)
        else:
            outputString += c
    return outputString


original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(remap(original))
print()
print("Solution:", remap("map"))