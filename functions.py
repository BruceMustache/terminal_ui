import color_functions


DISPLAY_WIDTH = None
DISPLAY_HEIGHT = None


def update():
    show_display_matrix()

def show_display_matrix(display):
    global DISPLAY_HEIGHT, DISPLAY_WIDTH
    # TODO put moving command in the display
    for row_counter in range(DISPLAY_HEIGHT):
        for column_counter in range(DISPLAY_WIDTH):
            print(display[row_counter][column_counter], end='')
        print(color_functions.reset())

    """ I try but something get wrong
    for row in display_matrix:
        for element in row:
            print(row, end='')
        print()
    """

def create_display(width, height, default_value):
    global display_matrix, DISPLAY_WIDTH, DISPLAY_HEIGHT
    DISPLAY_WIDTH = width
    DISPLAY_HEIGHT = height

    display_matrix = []
    for width_counter in range(height):
        row = [default_value] * width
        display_matrix.append(row)
    return display_matrix


