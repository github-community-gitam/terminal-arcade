"""The arcade menu — pick a game, play it, come back to the menu.

Games are registered in GAMES below. Each entry points at a module that
provides NAME, DESCRIPTION, and a play() function returning a score.
"""

from __future__ import annotations

import random
from types import ModuleType

from arcade import __version__, art, scoreboard
from arcade.games import guess, hangman, rps, tictactoe
from arcade.input_utils import ask, ask_int, confirm, pause

# To add a game: write arcade/games/yourgame.py, import it above, and add it
# here. That is the whole process. See docs/how-to-add-a-game.md.
GAMES: list[ModuleType] = [
    guess,
    hangman,
    rps,
    tictactoe,
]

# Extra menu options are defined in one place.
SURPRISE_OPTION = len(GAMES) + 1
SCORES_OPTION = len(GAMES) + 2
QUIT_OPTION = len(GAMES) + 3


def show_menu() -> None:
    """Print the list of games and the extra options."""
    print(art.ARCADE_BANNER)
    print(art.dim(f"  v{__version__}  ·  github-community-gitam\n"))

    for number, game in enumerate(GAMES, start=1):
        print(f"  {number}. {art.bold(game.NAME)}")
        print(f"     {art.dim(game.DESCRIPTION)}")

    print(f"\n  {SURPRISE_OPTION}. Surprise me")
    print(f"  {SCORES_OPTION}. High scores")
    print(f"  {QUIT_OPTION}. Quit\n")


def show_high_scores() -> None:
    """Print the overall top scores."""
    print(f"\n{art.bold('  HIGH SCORES')}\n")
    print(scoreboard.format_scoreboard(scoreboard.top_scores(limit=10)))
    print()


def run_game(game: ModuleType) -> None:
    """Play one game and offer to save the score.

    Args:
        game: A game module with NAME and play().
    """
    print()
    score = game.play()

    if score and score > 0:
        if confirm("  Save this score to the scoreboard?"):
            name = ask("  Your name:").strip() or "anonymous"
            scoreboard.save_score(game.NAME, name, score)
            print(art.green("  Saved.\n"))


def run_surprise() -> None:
    """Choose and play a random game."""
    game = random.choice(GAMES)
    print(art.cyan(f"\n  Surprise! You got: {game.NAME}\n"))
    run_game(game)


def main() -> None:
    """Start the arcade. Loops until the player chooses to quit."""
    while True:
        show_menu()
        choice = ask_int(
            "  What would you like to play?",
            minimum=1,
            maximum=QUIT_OPTION,
        )

        if choice == QUIT_OPTION:
            print(art.cyan("\n  Thanks for playing. See you next time.\n"))
            return

        if choice == SCORES_OPTION:
            show_high_scores()
            pause()
            continue

        if choice == SURPRISE_OPTION:
            run_surprise()
            pause()
            continue

        run_game(GAMES[choice - 1])
        pause()


if __name__ == "__main__":
    main()