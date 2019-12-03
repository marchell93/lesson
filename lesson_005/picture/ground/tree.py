import simple_draw as sd


sd.resolution = (1200, 600)


def draw_branches(start_point, angle, length, delta):
    if length < 5:
        return
    elif 10 > length > 5:
        color = sd.COLOR_GREEN
    else:
        color = sd.COLOR_YELLOW
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    v1.draw(width=1, color=color)
    next_point = v1.end_point
    next_length = length * .75
    next_angle_left = angle - delta
    next_angle_right = angle + delta
    draw_branches(start_point=next_point, angle=next_angle_left, length=next_length, delta=delta)
    draw_branches(start_point=next_point, angle=next_angle_right, length=next_length, delta=delta)


root_point = sd.get_point(950, 30)
root_angle = 90
root_length = 80
delta = 30
draw_branches(start_point=root_point, angle=root_angle, length=root_length, delta=delta)