from guessinggamelogo import logo
import random

def Game():
    print(logo)
    THE_NUMBER = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    Comp_num = random.choice(THE_NUMBER)

    LIVES_hard= 5
    LIVES_easy = 10

    print("Welcome to the game")

    Levels = input("play easy or hard: ")

    if Levels == "hard":
        print(f"You have chosen hard with {LIVES_hard} lives")
        lives = LIVES_hard
    elif Levels == "easy":
        print(f"You have chosen easy with {LIVES_easy} lives")
        lives = LIVES_easy

    #print(f"Hint, BIG BIG HINT: {Comp_num}")     

    Playing = True
    while Playing:
        USER_INPUT = int(input("GUESS THE NUMBER BETWEEN 1 AND 100: "))
        if USER_INPUT == Comp_num:
            print(Comp_num)
            print("User won")
            Playing = False
        elif USER_INPUT > Comp_num:
            lives -= 1
            print("You were too high!!!!!!")
            print(f"you have {lives} lives left")
        elif USER_INPUT < Comp_num:
            lives -= 1
            print(f"You were too low!!!!!")
            print(f"you have {lives} lives left")
        if lives == 0:
            print(lives)
            print(f"it was {Comp_num}")
            print("You lost")
            Playing = False


Game()





