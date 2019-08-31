from display_functions import *
import position_functions
import background_colors as background
import time


def clear():
    import os
    os.system('clear')

display = create_display(5, 3, background.red+' ')
clear()
show_display_matrix(display)
time.sleep(1)
display[1][1] = background.pink + ' '
clear()
show_display_matrix(display)
time.sleep(1)
display[1][3] = background.pink + ' '
clear()
show_display_matrix(display)

position_functions.cartesian_position(None, None, display)

