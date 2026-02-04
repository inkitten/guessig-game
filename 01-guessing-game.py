import random
def difficulty():
    while True:
        choosen_diff = input("which difficulty do you want? Easy, Medium, Hard")
        first = 0
        if choosen_diff == "Easy":
            second = 10
            lifes = 3
            break
        elif choosen_diff == "Medium":
            second = 50
            lifes = 5
            break
        elif choosen_diff == "Hard" :
            second = 100
            lifes = 8
            break
    return first, second , lifes
def guessing_game():
    first, second, lifes = difficulty()
    answer = random.randint(first, second)
    while lifes > 0:
        user_guess = int(input("Guess a number between {0} and {1}".format(first, second)))
        if user_guess == answer and lifes > 0:
            print("Correct! The answer was {0}.".format(answer))
            break
        elif user_guess < answer and lifes > 0:
            print("You guessed too low")
            lifes -= 1
        elif user_guess > answer and lifes > 0:
            print("You guessed too high")
            lifes -= 1
        print("you have %s guesses left" % lifes)
    if lifes <= 0:
        print("Sorry, you lose the game, it was {0}".format(answer))
guessing_game()