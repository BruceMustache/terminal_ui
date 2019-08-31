import color_functions


DISPLAY_MATRIX = []
DISPLAY_WIDTH = None
DISPLAY_HEIGHT = None


def update():
    show_display_matrix()

def show_display_matrix():
    global DISPLAY_MATRIX, DISPLAY_HEIGHT, DISPLAY_WIDTH
    for row_counter in range(DISPLAY_HEIGHT):
        for column_counter in range(DISPLAY_WIDTH):
            print(DISPLAY_MATRIX[row_counter][column_counter], end='')
        print()
    print( color_functions.reset(), end='' )

    """ I try but something get wrong
    for row in DISPLAY_MATRIX:
        for element in row:
            print(row, end='')
        print()
    """

def create_display(width, height, default_value):
    global DISPLAY_MATRIX, DISPLAY_WIDTH, DISPLAY_HEIGHT
    DISPLAY_WIDTH = width
    DISPLAY_HEIGHT = height
    for width_counter in range(height):
        row = [default_value] * width
        DISPLAY_MATRIX.append(row + [color_functions.reset()])


