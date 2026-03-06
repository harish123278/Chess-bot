import json
from chess_engine import ChessEngine

class ChessBot:
    def __init__(self, name="Harish G.M.", difficulty=2):
        self.name = name
        self.difficulty = difficulty
        self.engine = ChessEngine()
        self.game_history = []

    def get_best_move(self):
        if self.difficulty == 1:
            return self.get_random_move()
        elif self.difficulty == 2:
            return self.get_greedy_move()
        else:
            return self.get_minimax_move()

    def get_random_move(self):
        moves = self.engine.generate_moves(self.engine.board)
        return moves[0] if moves else None

    def get_greedy_move(self):
        moves = self.engine.generate_moves(self.engine.board)
        best_move = None
        best_value = -float('inf')
        for move in moves:
            value = self.evaluate_move(move)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move

    def get_minimax_move(self):
        moves = self.engine.generate_moves(self.engine.board)
        best_move = None
        best_value = -float('inf')
        for move in moves:
            value = self.minimax_search(move, depth=4, maximizing=False)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move

    def evaluate_move(self, move):
        return 0

    def minimax_search(self, move, depth, maximizing):
        if depth == 0:
            return self.engine.evaluate_board()
        return 0

    def play_move(self, move):
        self.game_history.append(move)
        return True

    def display_board(self):
        board = self.engine.board
        print("\n  a b c d e f g h")
        for i, row in enumerate(board):
            print(f"{8-i} {' '.join(row)} {8-i}")
        print("  a b c d e f g h\n")

    def get_stats(self):
        return {"name": self.name, "difficulty": self.difficulty, "games_played": len(self.game_history)}

if __name__ == "__main__":
    bot = ChessBot(name="Harish G.M.", difficulty=2)
    print(f"Welcome to {bot.name}!")
    print(f"Difficulty Level: {bot.difficulty}")
    bot.display_board()
    print(f"Bot Stats: {bot.get_stats()}")
