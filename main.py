from display_functions import *
import position_functions
import background_colors as background
import time
import os


def clear():
    # print('\n' * 100)
    os.system('clear')

def funcao_afim(a, b, display):
	MIDDLE_X = position_functions.MIDDLE_X
	MIDDLE_Y = position_functions.MIDDLE_Y
	a = 1
	b = 0
	for x in range(-1*MIDDLE_X, MIDDLE_X):
		y = a*x + b
		if abs(y) >= MIDDLE_Y or abs(x) >= MIDDLE_X:
			continue
		cord = position_functions.cartesian_position(x, y, display)
		display[cord[1]][cord[0]] = background.yellow + ' '
		time.sleep(0.3)
		clear()
		show_display_matrix(display)


display = create_display(80, 20, background.green+' ')
position_functions.set_variables(display)
funcao_afim(1, 2, display)

