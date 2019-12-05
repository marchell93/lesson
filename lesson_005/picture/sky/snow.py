import simple_draw as sd


def snowfall():
    N = 100
    x = []
    y = []
    length_of_snowflake = []

    for _ in range(N):
        x.append(sd.random_number(0, 260))
        y.append(sd.random_number(300, 440))
        length_of_snowflake.append(sd.random_number(5, 12))
    while True:
        sd.start_drawing()
        for i in range(N):
            point_0 = sd.get_point(x[i], y[i])
            sd.snowflake(center=point_0, length=length_of_snowflake[i], color=sd.background_color)
            y[i] -= 5
            if y[i] < length_of_snowflake[i] + 50:
                y[i] = sd.random_number(400, 440)
                x[i] = sd.random_number(0, 260)
                sd.snowflake(center=point_0, length=length_of_snowflake[i], color=sd.COLOR_WHITE)
            x[i] += sd.random_number(-5, 5)
            point_1 = sd.get_point(x[i], y[i])
            sd.snowflake(center=point_1, length=length_of_snowflake[i], color=sd.COLOR_WHITE)
            sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
