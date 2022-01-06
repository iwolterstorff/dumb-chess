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
                bots_move: chess.Move = evaluation.calculate_move(self.board)
                print(self.board.san(bots_move))
                self.board.push(bots_move)
            else:
                try_move = input(f"move {self.board.fullmove_number}: ")
                if try_move == "b" or try_move == "board":
                    print(self.board.unicode(borders=True))
                else:
                    try:
                        self.board.push_san(try_move)
                    except ValueError:
                        print("Illegal move. Try again")
        print(self.board.outcome())


def setup_game() -> GameState:
    response: str = input("Play black or white? ")
    if response.lower() in ["black", "b"]:
        # You have to pass the bot's color- opposite of the player's color
        return GameState(chess.WHITE)
    elif response.lower() in ["white", "w"]:
        return GameState(chess.BLACK)
    else:
        print("Specify a color for the bot to play: white/w or black/b")
        exit()


if __name__ == "__main__":
    state: GameState = setup_game()
    state.play()
