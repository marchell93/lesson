import simple_draw as sd

x_number_of_snowflake = []
y_number_of_snowflake = []
length_number_of_snowflake = []


def create_snowflake(number_of_snowflake):
    for _ in range(number_of_snowflake):
        x_number_of_snowflake.append(sd.random_number(0, 600))
        y_number_of_snowflake.append(sd.random_number(300, 650))
        length_number_of_snowflake.append(sd.random_number(10, 50))
    return x_number_of_snowflake, y_number_of_snowflake, length_number_of_snowflake


def draw_snowflake_color(number_of_snowflake, x, y, length_of_snowflake, color):
    for i in range(number_of_snowflake):
        point_0 = sd.get_point(x[i], y[i])
        sd.snowflake(center=point_0, length=length_of_snowflake[i], color=color)


def move_snowflake(number_of_snowflake, x, y):
    for i in range(number_of_snowflake):
        y[i] -= 5
        x[i] += sd.random_number(-5, 5)


def count_snowflake_bottom_of_screen(number_of_snowflake, y, length_of_snowflake):
    count_bottom_of_scr = []
    for i in range(number_of_snowflake):
        if y[i] < length_of_snowflake[i]:
            count_bottom_of_scr.append(i)
    return count_bottom_of_scr


def delete_snowflake(count_bottom_of_scr, x, y, length_of_snowflake):
    for count in count_bottom_of_scr:
        point_0 = sd.get_point(x[count], y[count])
        sd.snowflake(center=point_0, length=length_of_snowflake[count], color=sd.background_color)
        x[count] = 0
        y[count] = 0


def create_snowflake_modified(count_bottom_of_scr, x, y):
    for count in count_bottom_of_scr:
        x[count] = sd.random_number(0, 600)
        y[count] = sd.random_number(600, 650)
