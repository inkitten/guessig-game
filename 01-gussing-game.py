import random
def gussing_game():
    answer = random.randint(0, 100)
    while True:
        user_guess = int(input("Guess a number between 0 and 100: "))
        if user_guess > answer:
            print("You guessed too high")
        elif user_guess < answer:
            print("You guessed too low")
        else:
            print("You guessed correctly \nIt was {0}" ,format(answer))
            break
gussing_game()