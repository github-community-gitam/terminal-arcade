"""Tic Tac Toe.

You are X, the computer is O. Squares are numbered 1-9:

    1 | 2 | 3
    --+---+--
    4 | 5 | 6
    --+---+--
    7 | 8 | 9
"""

from __future__ import annotations

import random

from arcade import art
from arcade.input_utils import ask_int

NAME = "Tic Tac Toe"
DESCRIPTION = "The classic, against a computer that plays at random"

EMPTY = " "
PLAYER = "X"
COMPUTER = "O"

WINNING_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def new_board() -> list[str]:
    """Return an empty nine-square board."""
    return [EMPTY] * 9


def render(board: list[str]) -> str:
    """Draw the board as text.

    Empty squares show their number so the player knows what to enter.
    """
    cells = [
        board[i] if board[i] != EMPTY else str(i + 1)
        for i in range(9)
    ]

    return (
        f"\n     {cells[0]} | {cells[1]} | {cells[2]}\n"
        f"    ---+---+---\n"
        f"     {cells[3]} | {cells[4]} | {cells[5]}\n"
        f"    ---+---+---\n"
        f"     {cells[6]} | {cells[7]} | {cells[8]}\n"
    )


def winner(board: list[str]) -> str | None:
    """Return the winning mark, or None if there is no winner."""
    for a, b, c in WINNING_LINES:
        if (
            board[a] != EMPTY
            and board[a] == board[b]
            and board[b] == board[c]
        ):
            return board[a]

    return None


def free_squares(board: list[str]) -> list[int]:
    """Return the indexes of all empty squares."""
    return [
        i for i, cell in enumerate(board)
        if cell == EMPTY
    ]


def is_full(board: list[str]) -> bool:
    """Return True if the board has no empty squares."""
    return EMPTY not in board


def computer_move(board: list[str]) -> int:
    """Choose a random empty square for the computer."""
    return random.choice(free_squares(board))


def play() -> int:
    """Run one game of Tic Tac Toe.

    Returns:
        100 points if the player wins, otherwise 0.
    """
    print(art.banner("TIC TAC TOE"))
    print(f"\n  You are {PLAYER}. The computer is {COMPUTER}.")

    board = new_board()
    result = None

    while result is None and not is_full(board):

        # Display current board
        print(render(board))

        # -----------------------------
        # Player's move
        # -----------------------------
        while True:
            choice = ask_int(
                "  Your move (1-9): ",
                minimum=1,
                maximum=9
            )

            index = choice - 1

            if board[index] == EMPTY:
                board[index] = PLAYER
                break

            print(
                art.red(
                    "  That square is taken. Pick another."
                )
            )

        # Check if player won
        result = winner(board)

        if result is not None:
            break

        # Check for draw
        if is_full(board):
            break

        # -----------------------------
        # Computer's move
        # -----------------------------
        move = computer_move(board)
        board[move] = COMPUTER

        print(
            art.dim(
                f"\n  Computer plays square {move + 1}."
            )
        )

        # Check if computer won
        result = winner(board)

    # -----------------------------
    # Game over
    # -----------------------------
    print(render(board))

    if result == PLAYER:
        print("  You win!\n")
        return 100

    elif result == COMPUTER:
        print("  Computer wins!\n")
        return 0

    else:
        print("  It's a draw!\n")
        return 0