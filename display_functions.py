import color_functions
import time
import os


def update_display_and_wait_seconds(seconds, display):
	clear()
	show_display_matrix(display)
	time.sleep(seconds)

def show_display_matrix(display):
    width = get_width(display)
    height = get_height(display)

    for row_counter in range(height):
        for column_counter in range(width):
            print(display[row_counter][column_counter], end='')
        print(color_functions.reset())

    """ I try but something get wrong
    for row in display_matrix:
        for element in row:
            print(row, end='')
        print()
    """

def create_display(width, height, default_value):
    display_matrix = []
    for width_counter in range(height):
        row = [default_value] * width
        display_matrix.append(row)
    return display_matrix


def get_width(display):
    return len(display[0])

def get_height(display):
    return len(display)

def clear():
	os.system('clear')

