
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


class StateBowling(State):

    def __init__(self):
        super().__init__()
        self.result = 0

    def strike(self):
        self.result += 20

    def spare(self):
        self.result += 15

    def count(self, summa):
        self.result += summa
