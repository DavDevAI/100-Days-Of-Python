import random
from PIL.ImageChops import screen
from art import *
import os, time

def game():
    print(logo)
    attempts = 0
    mind = 0
    print("Try to guess a number in a range between 1 and a 100")
    choice = input("Chose a difficulty. Type 'easy' or 'hard': ")
    if choice == "hard":
        mind = random.randint(0, 101)
        #attempts = 5
        print (f"You have 5 attempts to guess the number")
        print(mind)
        guess = int(input("Make a guess: "))
        while attempts < 4:

            if guess > mind:
                print("To High, guess again!")
                attempts += 1
                print(f"You have {5 - attempts} attempts remaining!")
                guess = int(input("Make a guess: "))
            if guess < mind:
                print("To Low, guess again!")
                attempts += 1
                print(f"You have {5 - attempts} attempts remaining!")
                guess = int(input("Make a guess: "))
            if guess == mind:
                print("CONGRATS YOU´VE WON")
                break
                #attempts = 11 we can quit by changing the flag or using break
        else:
            print("You've run out of attempts!")
            time.sleep(3)
            clearscreen()
            game()



    elif choice == "easy":
        mind = random.randint(0, 101)
        # attempts = 10
        print(f"You have 10 attempts to guess the number")
        print(mind)
        guess = int(input("Make a guess: "))
        while attempts < 9:

            if guess > mind:
                print("To High, guess again!")
                attempts += 1
                print(f"You have {10 - attempts} attempts remaining!")
                guess = int(input("Make a guess: "))
            if guess < mind:
                print("To Low, guess again!")
                attempts += 1
                print(f"You have {10 - attempts} attempts remaining!")
                guess = int(input("Make a guess: "))
            if guess == mind:
                print("CONGRATS YOU´VE WON")
                break
                # attempts = 11 we can quit by changing the flag or using break
        else:
            print("You've run out of attempts!")
            time.sleep(3)
            clearscreen()
            game()

    else:
        game() #return 0



def clearscreen():
    os.system("cls" if os.name == "nt" else "clear")


#esta mal con que solo fuera un while esta bien

def main(startup):
    if startup == 's':
        print("Accesing game")
        time.sleep(1)
        clearscreen()
        game()
    else:
        startup = input("Welcome to the Number Guessing Game! \nPress 's' to start: ")
        main(startup)


startup = input("Welcome to the Number Guessing Game! \nPress 's' to start: ")
clearscreen()
main(startup)




