import random
import math

class AIPlayer:
    def __init__(self, ai_mark="O", human_mark="X"):
        self.ai = ai_mark
        self.human = human_mark
        self.difficulty = "HARD"

    def set_difficulty(self, level):
        self.difficulty = level

    def get_best_move(self, board):
        if self.difficulty == "EASY":
            return self.easy(board)
        elif self.difficulty == "MEDIUM":
            return self.medium(board)
        else:
            return self.hard(board)

    def easy(self, board):
        moves = [i for i, v in enumerate(board) if v == ""]
        return random.choice(moves) if moves else None

    def medium(self, board):
        if random.random() < 0.5:
            return self.easy(board)
        return self.hard(board)

    def hard(self, board):
        best_score = -math.inf
        best_move = None

        for i in range(9):
            if board[i] == "":
                board[i] = self.ai
                score = self.minimax(board, False)
                board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i

        return best_move

    def minimax(self, board, is_max):
        winner = self.check(board)
        if winner == self.ai:
            return 1
        if winner == self.human:
            return -1
        if "" not in board:
            return 0

        if is_max:
            best = -math.inf
            for i in range(9):
                if board[i] == "":
                    board[i] = self.ai
                    best = max(best, self.minimax(board, False))
                    board[i] = ""
            return best
        else:
            best = math.inf
            for i in range(9):
                if board[i] == "":
                    board[i] = self.human
                    best = min(best, self.minimax(board, True))
                    board[i] = ""
            return best

    def check(self, board):
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]

        for a, b, c in wins:
            if board[a] and board[a] == board[b] == board[c]:
                return board[a]
        return None
