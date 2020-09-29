
class PicPacPoe():
    def __init__(self):
        self.board = list(0 for n in range(9))
        self.curr_move = None
        self.curr_player = 1
        self.curr_column = None
        self.curr_row = None
        self.curr_space = None
        self.all_wins = None
        self.tot_moves = 0
    
    def __str__(self):
        return f"It is {'player ones' if self.curr_player == 1 else 'player twos'} turn with {self.tot_moves} moves played"

    def print_board_row(self, row):
        print('   ---------')
        print(f'{row}) ', end='', flush=True)
        for space in [self.board[n] for n in range(row - 1, row + 6, 3)]:
            print(f"{' X ' if space == 1 else ' O ' if space == -1 else '   '}", end='', flush=True)
        print('')

    def print_board(self):
        print('    A  B  C ')
        self.print_board_row(1)
        self.print_board_row(2)
        self.print_board_row(3)

    def calc_row_column(self):
        self.curr_column = self.curr_move[0].lower()
        self.curr_row = int(self.curr_move[1])

    def is_not_valid_entry(self): 
        if self.curr_column not in ('a', 'b', 'c') or self.curr_row not in (1, 2, 3):
            print('not valid entry')
            return True

    def calc_space(self):
        self.curr_space = self.curr_row - 1 if self.curr_column == 'a' else self.curr_row + 2 if self.curr_column == 'b' else self.curr_row + 5

    def is_space_taken(self):
        if self.board[self.curr_space] != 0:
            print('space taken')
            return True
    
    def set_space(self):
        self.board[self.curr_space] = self.curr_player

    def calc_all_wins(self):
        win_horiz_a = sum(self.board[n] for n in range(0, 7, 3))
        win_horiz_b = sum(self.board[n] for n in range(1, 8, 3))
        win_horiz_c = sum(self.board[n] for n in range(2, 9, 3))
        win_diag_a = sum(self.board[n] for n in range(0, 9, 4))
        win_diag_b = sum(self.board[n] for n in range(2, 7, 2))
        win_verts = [sum(self.board[0:3]), sum(self.board[3:6]), sum(self.board[6:])]
        self.all_wins = win_verts + [win_horiz_a, win_horiz_b, win_horiz_c, win_diag_a, win_diag_b]

    def is_win(self):
        if 3 in self.all_wins or -3 in self.all_wins: 
            print(f"{'player one' if 3 in self.all_wins else 'player two'} wins!")
            return True

    def is_tie(self):
        if self.tot_moves == 9:
            print('tie!')
            return True
    
    def play_game(self):
        while True:
            self.curr_move = input(f"{'player one' if self.curr_player == 1 else 'player two'} please enter your move (example B3): ")
            if self.curr_move == 'quit': break
            self.calc_row_column()
            if self.is_not_valid_entry(): continue
            self.calc_space()
            if self.is_space_taken(): continue
            self.set_space()
            self.print_board()
            self.tot_moves += 1
            self.calc_all_wins()
            if self.is_win(): break
            if self.is_tie(): break
            self.curr_player *= -1

picpac = PicPacPoe()
picpac.play_game()
print(picpac)

