from PIL import Image

im = Image.open("oxygen.png")

pixels = im.load()

value = 0
result = ""
for i in range(0, im.size[0], 7):
    currentValue = pixels[i,im.size[1]/2][0]
    if True: #currentValue != value:
        # print(i)
        result += str(chr(currentValue))
        value = currentValue;
        # print(pixels[i,im.size[1]/2])

print(result)

finalArray = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print("".join([chr(i) for i in finalArray]))
