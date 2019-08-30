FOREGROUND_ID = 3
BACKGROUND_ID = 4


def color(parameters=''):
    return f'\033[{parameters}m'

def foreground(color_id):
    global FOREGROUND_ID
    parameter = str(FOREGROUND_ID) + str(color_id)
    return color(parameter)

def background(color_id):
    global BACKGROUND_ID
    parameter = str(BACKGROUND_ID) + str(color_id)
    return color(parameter)

