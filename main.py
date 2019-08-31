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
time.sleep(0.1)
display[1][1] = background.pink + ' '
clear()
show_display_matrix(display)
time.sleep(0.1)
display[1][3] = background.pink + ' '
clear()
show_display_matrix(display)

cord = position_functions.cartesian_position(1, -1, display)
display[cord[1]][cord[0]] = background.yellow + ' '
time.sleep(0.1)
clear()
show_display_matrix(display)

y = position_functions.MIDDLE_Y
for x in range(0, position_functions.MIDDLE_X+1):
   cord = position_functions.cartesian_position(x, y, display)
   display[cord[1]][cord[0]] = background.yellow + ' '
   time.sleep(0.1)
   clear()
   show_display_matrix(display)

