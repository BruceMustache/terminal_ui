DISPLAY_MATRIX = []


def update():
    show_display_matrix()

def show_display_matrix():
    global DISPLAY_MATRIX
    for row in DISPLAY_MATRIX:
        for element in row:
            print(row, end='')
        print()

def create_display(width, hegith, default_value):
    for width_counter in range(width):
        row = [default_value] * width
        DISPLAY_MATRIX.append(row)


