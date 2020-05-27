
class Bowling:

    def __init__(self, state):
        self.state = state
        self.i = 0
        self.frame_count = 0

    def get_scope(self, game_result):
        while self.i < len(game_result):
            self.determination_state(game_result)
            self.i += 1

    def determination_state(self, game_result):
        self.frame_count += 1
        frame = game_result[self.i] + game_result[self.i + 1] if game_result[self.i] != 'X' else ''
        if game_result[self.i] == 'X':
            self.state.strike()
        elif '/' in frame:
            self.state.spare()
            self.i += 1
        else:
            summa = sum([int(x) for x in frame if x != '-'])
            if summa >= 10:
                raise ValueError(f'Ошибка в {self.frame_count} фрэйме. Вы ввели неверные числа...на площадке всего '
                                 f'10 кегель!!!')
            else:
                self.state.count(summa)
                self.i += 1


# Реализация паттерна проектирования "Состояние"
class State:

    def strike(self):
        pass

    def spare(self):
        pass

    def count(self, summa):
        pass


class StateBowling(State):  # TODO Обычно за состояние выбирают бросок (первый/второй)
    # TODO Тогда можно по-очереди вызывать объекты двух классов и чередовать их для расчёта
    # TODO Так в одном классе страйк вызывает ошибку (второй бросок) а в другом +20 очков (первый бросок)

    def __init__(self):
        super().__init__()
        self.result = 0  # TODO Подсчёт при этом производить надо в том классе, который будет управлять бросками

    def strike(self):
        self.result += 20

    def spare(self):
        self.result += 15

    def count(self, summa):
        self.result += summa


state = StateBowling()
gaming_bowling = Bowling(state)
gaming_bowling.get_scope('XXXXXXXXXXX')  # TODO Нужно считать фреймы и если их больше 10 (или меньше) - вызывать ошибку
print(state.result)

state = StateBowling()
gaming_bowling = Bowling(state)
gaming_bowling.get_scope('XXXXXXXXX00')  # TODO 0 в результатах тоже должен вызывать ошибку
print(state.result)

state = StateBowling()
gaming_bowling = Bowling(state)
gaming_bowling.get_scope('XXXXXXXXX//')  # TODO / в начале фрейма должен вызывать ошибку
print(state.result)

state = StateBowling()
gaming_bowling = Bowling(state)
gaming_bowling.get_scope('1XXXXXXXXXX')  # TODO Тут тоже должно быть отдельное исключение для страйка на втором броске
print(state.result)
