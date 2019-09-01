import position_functions


def funcao_afim(a, b, inputedColor, display):
	middle_x = position_functions.calculate_middle_x(display)
	middle_y = position_functions.calculate_middle_y(display)
	for x in range(-1*middle_x, middle_x):
		y = a*x + b
		# TODO limit dont get to the end or begin
		if abs(y) >= middle_y or abs(x) >= middle_x:
			continue
		cord = position_functions.cartesian_position(x, y, display)
		display[cord[1]][cord[0]] = inputedColor + ' '

