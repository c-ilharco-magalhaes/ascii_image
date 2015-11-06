from image_tools import read_image, create_output, hex_rgb


def generate_html(output, rgbs):
	line_start = "<p><span style=\"font-family: 'andale mono', times; font-size: large;\"><strong>"
	line_end = "</strong></span></p>\n"

	html = [line_start]
	for i in range(len(output)):
		for j in range(len(output[i])):
			html.append("<span style=\"color: " + hex_rgb(rgbs[i][j]) + ";\">" + output[i][j] + "</span>")
		html.append("<br>")
	html.append(line_end)

	f = open("result.html", "w")
	f.write("".join(html))


if __name__ == '__main__':

	(pixels, width, height) = read_image("test.png")
	# Try other letter sequences. Pixel-denser characters (like '#') give sharper results.
	(output, rgbs) = create_output(pixels, width, height, "GitHub")

	generate_html(output, rgbs)