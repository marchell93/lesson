class Bowling:

    def __init__(self):
        self.state = None
        self.i = 0
        self.frame_count = 0
        self.total_score = 0

    def change_state(self, state):
        self.state = state

    def char_state(self, char):
        if char == 'X':
            self.total_score += self.state.strike()
        elif char == '/':
            self.total_score += self.state.spare()
        else:
            if char.isdigit() or char == '-':
                self.total_score += self.state.count(char)
            else:
                raise ValueError('Вы ввели неверный символ!!!')

    def split_on_frame(self, game_result):
        frame = game_result[self.i] + game_result[self.i + 1] if game_result[self.i] != 'X' else game_result[self.i]
        self.frame_count += 1
        if self.frame_count > 10:
            raise ValueError('Нельзя играть больше 10 фреймов')
        yield frame
        self.i += 1 if len(frame) == 2 else 0

    def get_scope(self, game_result):
        while self.i < len(game_result):
            frame_generation = self.split_on_frame(game_result)
            for frame in frame_generation:
                if len(frame) == 1:
                    self.change_state(FirstShotState())
                    self.char_state(frame[0])
                elif frame[1] == '/' and frame[0].isdigit() and frame[0] != '0':
                    self.change_state(SecondShotState())
                    self.char_state(frame[1])
                else:
                    if frame[0].isdigit() and frame[1].isdigit():
                        if int(frame[0]) + int(frame[1]) >= 10:
                            raise ValueError('Сумма очков за два броска не должна превышать или быть равной 10 ' +
                                             'очкам...здесь должен быть спэр!!!')
                    self.change_state(FirstShotState())
                    self.char_state(frame[0])
                    self.change_state(SecondShotState())
                    self.char_state(frame[1])
                self.i += 1
        if self.frame_count < 10:
            raise ValueError('Сыграно меньше 10 фрэймов, запись game_result ошибочна!!!')


# Модифицированный класс насследуемый от Bowling (необходимый класс для внешнего рынка)
class BowlingModify(Bowling):

    def __init__(self):
        super().__init__()

    def split_on_frame(self, game_result):
        if self.i + 1 == len(game_result) and game_result[self.i] == 'X':
            frame = game_result[self.i]
        elif self.i + 2 == len(game_result) and (game_result[self.i + 1] == '/' or game_result[self.i + 1] == 'X'):
            frame = game_result[self.i] + game_result[self.i + 1]
        else:
            frame = game_result[self.i] + game_result[self.i + 1] + game_result[self.i + 2] \
                if game_result[self.i] == 'X' or game_result[self.i + 1] == '/' \
                else game_result[self.i] + game_result[self.i + 1]
        self.frame_count += 1
        if self.frame_count > 10:
            raise ValueError('Нельзя играть больше 10 фреймов')
        yield frame
        if self.i != len(game_result):
            if len(frame) == 2 and frame != 'XX' or game_result[self.i] == '/':
                self.i += 1
        else:
            self.i += 0

    def get_scope(self, game_result):
        while self.i < len(game_result):
            frame_generation = self.split_on_frame(game_result)
            for frame in frame_generation:
                if len(frame) == 3:
                    if frame[0] == 'X' and frame[2] == '/':
                        self.change_state(FirstShotStateModify())
                        self.char_state(frame[0])
                        self.change_state(SecondShotStateModify())
                        self.char_state(frame[2])
                    elif frame[1] == '/' and frame[0].isdigit() and frame[0] != '0':
                        self.change_state(SecondShotStateModify())
                        self.char_state(frame[1])
                        self.change_state(FirstShotStateModify())
                        self.char_state(frame[2])
                    else:
                        self.change_state(FirstShotStateModify())
                        self.char_state(frame[0])
                        self.char_state(frame[1])
                        self.char_state(frame[2])
                elif len(frame) == 1:
                    self.change_state(FirstShotStateModify())
                    self.char_state(frame[0])
                elif frame[1] == '/' and frame[0].isdigit() and frame[0] != '0':
                    self.change_state(SecondShotStateModify())
                    self.char_state(frame[1])
                elif frame[0] == 'X' and frame[1] == 'X':
                    self.change_state(FirstShotStateModify())
                    self.char_state(frame[0])
                    self.char_state(frame[1])
                else:
                    if frame[0].isdigit() and frame[1].isdigit():
                        if int(frame[0]) + int(frame[1]) >= 10:
                            raise ValueError('Сумма очков за два броска не должна превышать или быть равной 10 ' +
                                             'очкам...здесь должен быть спэр!!!')
                    self.change_state(FirstShotState())
                    self.char_state(frame[0])
                    self.change_state(SecondShotState())
                    self.char_state(frame[1])
                self.i += 1
        if self.frame_count < 10:
            raise ValueError('Сыграно меньше 10 фрэймов, запись game_result ошибочна!!!')


# Реализация паттерна проектирования "Состояние"
class State:

    def strike(self):
        pass

    def spare(self):
        pass

    def count(self, char):
        if char == '-':
            return 0
        if char != '0':
            return int(char)
        else:
            raise ValueError('Не должно быть в строке символа 0, вместо этого пишем -')


class FirstShotState(State):

    def strike(self):
        return 20

    def spare(self):
        raise ValueError('В первом броске не может быть спэра')


class SecondShotState(State):

    def strike(self):
        raise ValueError('Во втором броске не может быть страйка')

    def spare(self):
        return 15


# Модификационные классы состояний
class FirstShotStateModify(FirstShotState):
    def strike(self):
        return 10

    def spare(self):
        raise ValueError('В первом броске не может быть спэра')


class SecondShotStateModify(SecondShotState):
    def strike(self):
        raise ValueError('Во втором броске не может быть страйка')

    def spare(self):
        return 10
