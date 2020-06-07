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
                    self.change_state(FirstShotState())
                    self.char_state(frame[0])
                    self.change_state(SecondShotState())
                    self.char_state(frame[1])
                self.i += 1


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
