class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        step = 1 if player == 1 else -1

        self.rows[row] += step
        self.cols[col] += step

        # in the diagonal
        if row == col:
            self.diagonal += step
        if row + col == self.n - 1:
            self.anti_diagonal += step

        # check if there is winner
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagonal) == self.diagonal or abs(self.anti_diagonal) == self.anti_diagonal:
            return player

        return 0




