class X_O:
    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.winner = None

    def print_board(self):
        for row in self.board:
            print("| " + " | ".join(row) + " |")

    def make_move(self, row, col, letter):
        if self.board[row][col] == " ":
            self.board[row][col] = letter
            if self.win(row, col, letter):
                self.winner = letter
            return True
        return False
   
    def win(self, row, col, letter):
        row_count = 0
        for i in range(3):
            if self.board[row][i] == letter:
                row_count += 1
        if row_count == 3:
            return True

        col_count = 0
        for i in range(3):
            if self.board[i][col] == letter:
                col_count += 1
        if col_count == 3:
            return True

        diag1_count = 0
        diag2_count = 0
        for i in range(3):
            if self.board[i][i] == letter:
                diag1_count += 1
            if self.board[i][2 - i] == letter:
                diag2_count += 1
        if diag1_count == 3 or diag2_count == 3:
            return True

        return False


def play():
    game = X_O()
    player_letter = ["X", "O"]
    turn = 0

    while 1:
        current_letter = player_letter[turn % 2]
        print(f"{current_letter} ходит")

        game.print_board()
        row = int(input("Введите строку "))
        col = int(input("Введите столбик "))

        if game.make_move(row, col, current_letter):
            if game.winner:
                print(f"{current_letter} победил!")
                game.print_board()
                break
            turn += 1

        game.print_board()



play()
