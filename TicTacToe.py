import random


class TicTacToe():
    def __init__(self):
        self.board = []

    def createBoard(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("#")
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def start(self):
        self.createBoard()
        player = 'X' if self.get_random_first_player() == 1 else 'O'

        while not self.isBoardFilled():
            self.show_board()

            row, colum = input(f"Player {player} enter row and column:")
            if self.fix_Spot_Check_Free_Spot(row, colum, player):
                if self.is_win(player):
                    print(f"Player {player} won.")
                    break

                if not self.is_win(player):
                    player = self.swap_player_turn(player)
            else:
                print("\nPlace taken!\n")
        if not self.is_win(player):
            print("Draw")
        self.show_board()

    def fix_Spot_Check_Free_Spot(self, row, column, player):
        if self.board[int(row) - 1][int(column) - 1] == "#":
            self.board[int(row) - 1][int(column) - 1] = player
            return True
        return False

    def is_win(self, player):
        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking column
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][len(self.board) - 1 - i] != player:
                win = False
                break
        if win:
            return win

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def isBoardFilled(self):
        for e in range(3):
            for e2 in range(3):
                if self.board[e][e2] == "#":
                    return False
        else:
            return True


t = TicTacToe()
t.start()
