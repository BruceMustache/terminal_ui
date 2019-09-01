from display_functions import *
import position_functions
import background_colors as background
import time
import os


def clear():
    # print('\n' * 100)
    os.system('clear')

def funcao_afim(a, b, inputedColor, display):
	MIDDLE_X = position_functions.MIDDLE_X
	MIDDLE_Y = position_functions.MIDDLE_Y
	for x in range(-1*MIDDLE_X, MIDDLE_X):
		y = a*x + b
		# TODO limit dont get to the end or begin
		if abs(y) >= MIDDLE_Y or abs(x) >= MIDDLE_X:
			continue
		cord = position_functions.cartesian_position(x, y, display)
		display[cord[1]][cord[0]] = inputedColor + ' '


display = create_display(80, 20, background.green+' ')
position_functions.set_variables(display)
funcao_afim(0, 0, background.red, display)
funcao_afim(1, 2, background.yellow, display)
show_display_matrix(display)

