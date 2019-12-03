import simple_draw as sd


def rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    x_point = 450
    y_point = -300
    radius = 850
    for color in rainbow_colors:
        point_start = sd.get_point(x_point, y_point)
        radius += 15
        sd.circle(point_start, radius, color, 10)
