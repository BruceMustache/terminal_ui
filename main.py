from display_functions import *
from  drawing_functions import funcao_afim
import position_functions
import background_colors as background

display = create_display(81, 20, background.black+' ')

funcao_afim(-1, -2, background.red, display)
funcao_afim(1, 2, background.red, display)

funcao_afim(1, 1, background.red, display)
funcao_afim(-1, -1, background.red, display)

funcao_afim(1, 0, background.yellow, display)
funcao_afim(-1, 0, background.yellow, display)

show_display_matrix(display)

