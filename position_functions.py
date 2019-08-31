import display_functions

WAS_SET = False
MIDDLE_X = MIDDLE_Y = None
WIDTH = HEIGHT = None

def set_variables(display):
    global WIDTH, HEIGHT
    WIDTH = display_functions.get_width(display)
    HEIGHT = display_functions.get_height(display)

    global MIDDLE_X, MIDDLE_Y
    MIDDLE_X = WIDTH // 2
    MIDDLE_Y = HEIGHT // 2

    global WAS_SET
    WAS_SET = True

def cartesian_position(x, y, display):
    global WAS_SET
    if not WAS_SET:
        set_variables(display)

    global MIDDLE_X, MIDDLE_Y
    x += MIDDLE_X
    y = MIDDLE_Y - y
    return x, y

