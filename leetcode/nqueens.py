# In a n x n board with n queens, what positions have the queens not attacking each other?

from icecream import ic
import sys

class Board:
    def __init__(self, n):
        self.n = n
        self.board = [['.' for _ in range(n)] for _ in range(n)]
    def place_queen(self, row, col):
        ic(row, col)
        self.board[row][col] = 'Q'
    def rem_queen(self, row, col):
        self.board[row][col] = '.'

def is_safe_pos(board, row, col):
    # Check from position, to left side of board for horiz attack
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    # Check upper left diagonal
    for i, j in 

def main():
    n = int(sys.argv[1])
    curr_board = Board(n)
    curr_board.place_queen()
    ic(curr_board.board)
    curr_board.val_board()

if __name__ == '__main__':
    main()