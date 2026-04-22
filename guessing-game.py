"""
A simple guessing_game using the maximum
of my pyton programmig skills in 4/2026
"""

from random import randint

# Game difficulty settings
DIFFICULTY = {
    "easy": {"max": 10, "lives": 3},
    "medium": {"max": 50, "lives": 5},
    "hard": {"max": 100, "lives": 7},
}


def select_difficulty(levels):
    """
    Prompt user to select a difficulty level and return corresponding settings.
    """
    while True:
        choice = input(
                ("Select difficulty (Easy / Medium / Hard): ")
                ).strip().lower()
        if choice in levels:
            level = levels[choice]
            return 0, level["max"], level["lives"]
        print("Invalid option. Please try again.")


def bot_number():
    """
    Let the bot choose a random number based on difficulty.
    """
    min_num, max_num, lives = select_difficulty(DIFFICULTY)
    return randint(min_num, max_num), lives, min_num, max_num


def compare_numbers(secret, guess):
    """
    Compare player’s guess with bot’s secret number.
    """
    guess = int(guess)
    if guess > secret:
        print("It's greater than mine.")
    elif guess < secret:
        print("It's lesser than mine.")
    else:
        print("🎉 BINGO!! You’re Correct!!")
        return True
    return False


def game():
    """
    Run the main game loop.
    """
    number, lives, low, high = bot_number()

    print(f"\nI'm thinking of a number between {low} and {high}...")

    while lives > 0:
        player_input = input("Your guess: ").strip()

        if not player_input.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        if compare_numbers(number, player_input):
            break

        lives -= 1
        print(f"❗ {lives} {'life' if lives == 1 else 'lives'} remaining.")

    else:
        print(f"💀 Game Over! The number was {number}.")


if __name__ == "__main__":
    game()
