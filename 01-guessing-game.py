import random
def difficulty():
    while True:
        choosen_diff = input("which difficulty do you want? Easy, Medium, Hard")
        if choosen_diff == "Easy":
            first = 0
            second = 10
            break
        elif choosen_diff == "Medium":
            first = 0
            second = 50
            break
        elif choosen_diff == "Hard" :
            first = 0
            second = 100
            break

    return first, second
first, second = difficulty()
def guessing_game():
    answer = random.randint(first, second)
    while True:
        user_guess = int(input("Guess a number between %s and %s" % (first, second) ))
        if user_guess > answer:
            print("You guessed too high")
        elif user_guess < answer:
            print("You guessed too low")
        else:
            print("You guessed correctly \nIt was %s" % answer)
            break
guessing_game()