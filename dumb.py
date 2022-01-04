import chess

import evaluation


class GameState:
    def __init__(self, bot_color: chess.Color):
        self.bot_color = bot_color
        self.board = chess.Board()

    def play(self):
        """
        Plays through a game of chess, looping between making a move and receiving a move from the user.
        """
        while not self.board.is_game_over():
            if self.board.turn == self.bot_color:
                self.board.push(evaluation.calculate_move(self.board))
            else:
                try_move = input(f"move {self.board.fullmove_number}: ")
                try:
                    self.board.push_san(try_move)
                except ValueError:
                    print("Illegal move. Try again")
        print(self.board.outcome())


def setup_game() -> GameState:
    response: str = input("Play black or white? ")
    if response.lower() in ["black", "b"]:
        return GameState(chess.BLACK)
    elif response.lower() in ["white", "w"]:
        return GameState(chess.WHITE)
    else:
        print("Specify a color for the bot to play: white/w or black/b")
        exit()


if __name__ == "__main__":
    state: GameState = setup_game()
    state.play()
