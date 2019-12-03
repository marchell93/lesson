import simple_draw as sd


def wall():
    # Счётчик для циклов
    count = 1
    # Цикл считающий координату y
    for y in range(50, 270, 30):
        # Условие необходимое для определения какой ряд кирпичей мы кладем
        x_range = -25 + 350 if count % 2 != 0 else 350  # Можно тут тернальный оператор применить
        for x in range(x_range, 375 + 350, 50):
            if x == 325:
                point_start = sd.get_point(350, y)
            else:
                point_start = sd.get_point(x, y)
            point_finish = sd.get_point(x + 50, y + 30)
            sd.rectangle(point_start, point_finish, width=3)
        count += 1

    point_wall_start = sd.get_point(0 + 350, 50)
    point_wall_finish = sd.get_point(400 + 350, 290)
    sd.rectangle(point_wall_start, point_wall_finish, color=sd.COLOR_YELLOW, width=3)


def window():
    point_start = sd.get_point(470, 80)
    sd.square(point_start, side=180, color=sd.background_color)
    point_finish = sd.get_point(470+180, 80+180)
    sd.rectangle(point_start, point_finish, color=sd.COLOR_YELLOW, width=3)


def smile():
    x = 560
    y = 200
    color = sd.COLOR_CYAN
    # Прорисовываем овал лица...точнее круг)))
    point = sd.get_point(x, y)
    radius = 50
    sd.circle(point, radius, color, 4)
    # Прорисовываем правый глаз смайлика
    point_right_eyes = sd.get_point(x + 15, y + 15)
    radius_right_eyes = radius - 45
    sd.circle(point_right_eyes, radius_right_eyes, color)
    # Прорисовываем левый глаз смайлика
    point_left_eyes = sd.get_point(x - 15, y + 15)
    radius_left_eyes = radius - 45
    sd.circle(point_left_eyes, radius_left_eyes, color)
    # Прорисовываем рот смайлика
    point_mouth_first = sd.get_point(x - 30, y - 5)
    point_mouth_second = sd.get_point(x - 15, y - 20)
    point_mouth_third = sd.get_point(x + 15, y - 20)
    point_mouth_fourth = sd.get_point(x + 30, y - 5)
    point_list = []
    point_list.extend([point_mouth_first, point_mouth_second, point_mouth_third, point_mouth_fourth])
    sd.lines(point_list, closed=False, color=color)
    # Рисуем туловище
    point_body_start = sd.get_point(560, 150)
    point_body_finish = sd.get_point(560, 80)
    sd.line(point_body_start, point_body_finish, color=color, width=4)
    # Рисуем руки
    point_arms = sd.get_point(560, 120)
    arm_right = sd.get_vector(point_arms, angle=35, length=60, width=4)
    arm_right.draw(color=color)
    arm_left = sd.get_vector(point_arms, angle=140, length=60, width=4)
    arm_left.draw(color=color)


def roof():
    angle = 0
    length = 450
    color = sd.COLOR_DARK_RED
    point_triangle = sd.get_point(325, 290)
    v1 = sd.get_vector(start_point=point_triangle, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 160, length=length/2, width=3)
    v2.draw()
    sd.line(start_point=v2.end_point, end_point=point_triangle, width=3)
