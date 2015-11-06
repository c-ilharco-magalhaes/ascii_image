from PIL import Image, ImageDraw, ImageFont

from image_tools import read_image, create_output, get_spacing


def draw_image(output, rgbs, font):
	width, height = len(output[0]), len(output)
	(px, py) = get_spacing(font)
	resultImage = Image.new(mode='RGBA', size=(width*px, height*py))
	draw = ImageDraw.Draw(resultImage)

	for y in range(height):
		for x in range(width):
			draw.text((x*px, y*py), output[y][x], font=font, fill=rgbs[y][x])

	resultImage.save('result.png', 'PNG')


if __name__ == '__main__':

	(pixels, width, height) = read_image("test.png")
	# Try other letter sequences. Pixel-denser characters (like '#') give sharper results.
	(output, rgbs) = create_output(pixels, width, height, "GitHub")
	font = ImageFont.truetype("FreeMonoBold.ttf", 24)
	draw_image(output, rgbs, font)
