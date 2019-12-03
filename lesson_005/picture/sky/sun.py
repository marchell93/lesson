import simple_draw as sd


def sun():
    point = sd.get_point(1100, 500)
    radius = 50
    sd.circle(point, radius, width=0)

    for angle_int in range(0, 350, 25):
        vec = sd.get_vector(point, angle=angle_int, length=100, width=5)
        vec.draw()
