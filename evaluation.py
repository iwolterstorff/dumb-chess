import chess

from typing import Dict, Generator, Final

KING_VALUE: Final[int] = 200
QUEEN_VALUE: Final[int] = 9
ROOK_VALUE: Final[int] = 5
BISHOP_VALUE: Final[int] = 3
KNIGHT_VALUE: Final[int] = 3
PAWN_VALUE: Final[int] = 1

PIECE_TYPE_VALUES: Final[Dict[chess.PieceType, int]] = {
    chess.KING: KING_VALUE,
    chess.QUEEN: QUEEN_VALUE,
    chess.ROOK: ROOK_VALUE,
    chess.BISHOP: BISHOP_VALUE,
    chess.KNIGHT: KNIGHT_VALUE,
    chess.PAWN: PAWN_VALUE,
}


def child_positions(board: chess.Board) -> Generator[chess.Board, None, None]:
    for move in board.legal_moves:
        new_board = board.copy(stack=False)  # Don't need to copy the move stack
        new_board.push(move)
        yield new_board


def piece_evaluation(
    board: chess.Board, to_move: chess.Color, piece_type: chess.PieceType
) -> int:
    friendly_pieces: int = len(board.pieces(piece_type, to_move))
    enemy_pieces: int = len(board.pieces(piece_type, not to_move))
    return PIECE_TYPE_VALUES[piece_type] * (friendly_pieces - enemy_pieces)


def evaluate(board: chess.Board) -> int:
    """
    Returns a numeric objective evaluation of the position specified in `board`.
    Current implementation only considers material values.

    https://www.chessprogramming.org/Evaluation
    """
    color_to_move: chess.Color = board.turn
    summation: int = 0
    for piece_type in PIECE_TYPE_VALUES.keys():
        summation += piece_evaluation(board, color_to_move, piece_type)
    return summation


def negamax(board: chess.Board, depth: int = 3, color: chess.Color = None) -> int:
    """
    Implements the Negamax algorithm, a simplified case of the minimax algorithm.
    If color is not provided, will use the color to move of the board.

    https://en.wikipedia.org/wiki/Negamax
    """
    if color is None:
        color = board.turn
    if depth == 0 or board.is_game_over():
        return (-1 * color) * evaluate(board)

    return max(
        [-negamax(child, depth - 1, not color) for child in child_positions(board)]
    )
