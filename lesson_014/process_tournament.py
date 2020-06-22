from bowling import Bowling, BowlingModify


class TournamentInfo:

    def __init__(self, input_file, output_file, market):
        self.input_file = input_file
        self.output_file = output_file
        self.winner = []
        self.name_count_game = {}
        self.name_count_win = {}
        self.market = market

    def game_info(self):
        markets = {'home': Bowling, 'foreign': BowlingModify}
        output_file = open(self.output_file,  mode='a+', encoding='utf-8')
        with open(self.input_file, mode='r', encoding='utf-8') as file:
            for line in file:
                line = line.strip('\n')
                try:
                    if '\t' in line:
                        line = line.split('\t')
                        name = line[0]
                        scope = line[1]
                        bowling_game = markets[self.market]()
                        bowling_game.get_scope(scope)
                        digit_scope = bowling_game.total_score
                        new_line = f'{name}\t{scope}\t{digit_scope}'
                        output_file.write(f'{new_line}\n')
                        self.winner_info(name, digit_scope)
                        self.count_game(name)
                    elif 'winner is' in line:
                        winner_line = f'winner is {self.winner[0]}'
                        output_file.write(f'{winner_line}\n')
                        self.count_win(self.winner[0])
                        self.winner.clear()
                    else:
                        output_file.write(f'{line}\n')
                except ValueError as exc:
                    new_line = f'{name}\t{scope}\t{exc.args}'
                    output_file.write(f'{new_line}\n')

                except IndexError:
                    new_line = f'{name}\t{scope}\t(Количество бросков во фрейме не хватает ' \
                        f'для корректного подсчета очков.)'
                    output_file.write(f'{new_line}\n')
        output_file.close()

    def winner_info(self, name, total_score):
        if not self.winner:
            self.winner.append(name)
            self.winner.append(total_score)
        elif self.winner[1] < total_score:
            self.winner.clear()
            self.winner.append(name)
            self.winner.append(total_score)

    def count_game(self, name):
        if name in self.name_count_game:
            self.name_count_game[name] += 1
        else:
            self.name_count_game[name] = 1

    def count_win(self, name):
        if name in self.name_count_win:
            self.name_count_win[name] += 1
        else:
            self.name_count_win[name] = 1

    def write_on_console(self):
        format_chars = ['+', '-', 'Игрок', 'сыграно матчей', 'всего побед']
        head_line = f'{format_chars[0]:-<11}{format_chars[0]:-<19}{format_chars[0]:-<15}{format_chars[0]}'
        words_line = f'|{format_chars[2]:^10}|{format_chars[3]:^18}|{format_chars[4]:^14}|'
        print(head_line)
        print(words_line)
        print(head_line)
        for key, value in self.name_count_game.items():
            win_size = self.name_count_win[key]
            line = f'|{key:^10}|{value:^18}|{win_size:^14}|'
            print(line)
        print(head_line)
