import simple_draw as sd


def tree(start_point, angle, length, delta):
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
    tree(start_point=next_point, angle=next_angle_left, length=next_length, delta=delta)
    tree(start_point=next_point, angle=next_angle_right, length=next_length, delta=delta)
