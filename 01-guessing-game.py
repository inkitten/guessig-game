import random
def difficulty():
    while True:
        choosen_diff = input("which difficulty do you want? Easy, Medium, Hard: ")
        first = 0
        if choosen_diff == "Easy":
            second = 10
            lives = 3
            break
        elif choosen_diff == "Medium":
            second = 50
            lives = 5
            break
        elif choosen_diff == "Hard" :
            second = 100
            lives = 8
            break
    return first, second , lives
def guessing_game():
    min_num, max_num, lives = difficulty()
    answer = random.randint(min_num, max_num)
    while lives > 0:
        user_guess = int(input("Guess a number between {0} and {1}: ".format(min_num, max_num)))
        if user_guess == answer:
            print("Correct! The answer was {0}.".format(answer))
            break
        elif user_guess < answer:
            print("You guessed too low")
            lives -= 1
        elif user_guess > answer:
            print("You guessed too high")
            lives -= 1
        print("you have %s guesses left" % lives)
    if lives <= 0:
        print("Sorry, you lose the game, it was {0}".format(answer))
guessing_game()