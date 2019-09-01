from display_functions import *
from  drawing_functions import funcao_afim
import position_functions
import background_colors as background

display = create_display(81, 20, background.black+' ')
waiting = 0.5

funcao_afim(-1, -2, background.red, display)
update_display_and_wait_seconds(waiting, display)

funcao_afim(1, 2, background.red, display)
update_display_and_wait_seconds(waiting, display)

funcao_afim(1, 1, background.red, display)
update_display_and_wait_seconds(waiting, display)

funcao_afim(-1, -1, background.red, display)
update_display_and_wait_seconds(waiting, display)

funcao_afim(1, 0, background.yellow, display)
update_display_and_wait_seconds(waiting, display)

funcao_afim(-1, 0, background.yellow, display)
update_display_and_wait_seconds(waiting, display)

