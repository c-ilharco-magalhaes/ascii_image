from PIL import Image, ImageDraw, ImageFilter


def read_image(filename):
	image = Image.open(filename, "r").convert("RGBA")
	# Optional: Filters can increase contrast.
	# image = image.filter(ImageFilter.SHARPEN)
	# image = image.filter(ImageFilter.EDGE_ENHANCE)
	pixels = list(image.getdata())
	(width, height) = image.size
	return (pixels, width, height)

def create_output(pixels, width, height, letters):
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

def get_spacing(font):
	testImage = Image.new(mode='RGBA', size=(50,50))
	testDraw = ImageDraw.Draw(testImage)
	char_spacing = testDraw.textsize('A', font=font)[0] - 1
	line_spacing = testDraw.textsize('A', font=font)[1] - 1
	# By making vertical and horizontal spacing equal, the image proportion is preserved.
	max_spacing = max(char_spacing, line_spacing)
	return (max_spacing, max_spacing)

def hex_rgb(rgb):
	number = (rgb[0]<<16) + (rgb[1]<<8) + rgb[2]
	return "#%0.6X" % number
