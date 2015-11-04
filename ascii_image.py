from PIL import Image, ImageFont, ImageDraw, ImageFilter


def readImage(filename):
	image = Image.open(filename, "r").convert("RGBA")
	# Optional: Filters can increase contrast.
	image = image.filter(ImageFilter.SHARPEN)
	image = image.filter(ImageFilter.EDGE_ENHANCE)
	pixels = list(image.getdata())
	(width, height) = image.size
	return (pixels, width, height)

def createOutput(pixels, width, height, letters):
	charOutput = []
	charRgbs = []
	letterIndex = 0
	for i in range(height):
		line = []
		rgbs = []
		for j in range(width):
			p = width*i + j
			line.append(letters[letterIndex])
			letterIndex = (letterIndex+1)%len(letters)
			rgbs.append(tuple(list(pixels[p])[0:3]+[255]))

		charOutput.append(line)
		charRgbs.append(rgbs)

	return (charOutput, charRgbs)

def getSpacing(font):
	testImage = Image.new(mode='RGBA', size=(50,50))
	testDraw = ImageDraw.Draw(testImage)
	char_spacing = testDraw.textsize('A', font=font)[0] - 1
	line_spacing = testDraw.textsize('A', font=font)[1] - 1
	# By making vertical and horizontal spacing equal, the image proportion is preserved.
	max_spacing = max(char_spacing, line_spacing)
	return (max_spacing, max_spacing)


(pixels, width, height) = readImage("test.png")

# Try other letter sequences. Pixel-denser characters (like '#') give sharper results.
(output, rgbs) = createOutput(pixels, width, height, "GitHub")

font = ImageFont.truetype("FreeMonoBold.ttf", 24)

(px, py) = getSpacing(font)


resultImage = Image.new(mode='RGBA', size=(width*px, height*py))
draw = ImageDraw.Draw(resultImage)

for y in range(len(output)):
	for x in range(len(output[y])):
		draw.text((x*px, y*py), output[y][x], font=font, fill=rgbs[y][x])

resultImage.save('result.png', 'PNG')

