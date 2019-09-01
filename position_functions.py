import display_functions


def calculate_middle_x(display):
	width = display_functions.get_width(display)
	return width // 2

def calculate_middle_y(display):
	height = display_functions.get_height(display)
	return height // 2

def cartesian_position(x, y, display):
	middle_x = calculate_middle_x(display)
	middle_y = calculate_middle_y(display)

	x += middle_x
	y = middle_y - y

	return x, y

