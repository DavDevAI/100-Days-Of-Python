from art import *
import random
import game_data as gd

def game():


    streak = True
    while streak:

        datalength = int(len(gd.data))
        sort1 = random.randint(0, datalength)
        sort2 = random.randint(0, datalength)

        celeb1 = gd.data[sort1]
        celeb2 = gd.data[sort2]

        print(f"Compare A: {celeb1['name']}, a {celeb1['description']}, from {celeb1['country']}")
        print(vs)
        print(f"Against B: {celeb2['name']}, a {celeb2['description']}, from {celeb2['country']}")
        choice = str(input("Who has more followers? Type 'A' or 'B': ")).upper()
        score = 0
        if choice == 'A':
            if celeb1['follower_count'] > celeb2['follower_count']:
                #case in which you switch comparison statements
                score += 1
                print(f"You're right! Current score: {score}")
                game(celeb1, )
            if celeb1['follower_count'] < celeb2['follower_count']:
                streak = False
                print(f"Sorry, that's wrong. Your final score: {score}")
        if choice == 'B':
            if celeb2['follower_count'] > celeb1['follower_count']:
                #case in which you switch comparison statements
                score += 1
                print(score)
            if celeb2['follower_count'] < celeb1['follower_count']:
                streak = False
                print("Sorry, that's wrong.")
        else:
            break



print(logo)
game ()
