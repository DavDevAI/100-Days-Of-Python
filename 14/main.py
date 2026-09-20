from art import *
import random
import game_data as gd
#BEST ONE FOR COMMAND LINE MANAGEMENT
#import rich as rch
from rich.console import Console
console = Console() #creating and object out of the class that is inside the module

print(logo)
data_lenght = len(gd.data) #posible index error to fix in datapull and index assignment
streak = True
score = 0


def celebs_getter(data_lenght):
    #sort1 = random.randint(0, datalenght)
    sort2 = random.randint(0, data_lenght - 1) #posible index error
    #celeb1 = gd.data[sort1]
    celeb2 = gd.data[sort2]
    # return celeb1, celeb2 # returns both of them as tuple of 2 lists or a tuple containing 2 lists
    return celeb2

def count_checker(auxcho, celebx):
    if auxcho['follower_count'] < celebx['follower_count']:
        return False
    else:
        return True


#Celeb starter where all begins, then replaced
celeb2  = celebs_getter(data_lenght)

while streak:
    val = 0
    choice = "-"
    celeb1 = celeb2
    celeb2 = celebs_getter(data_lenght)
    while celeb1 == celeb2:
        celeb2 = celebs_getter(data_lenght)

    print(f"Compare A: {celeb1['name']}, a {celeb1['description']}, from {celeb1['country']}")
    print(vs)
    print(f"Against B: {celeb2['name']}, a {celeb2['description']}, from {celeb2['country']}")
    #choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    while choice != 'A' and choice != 'B':
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()


    console.clear()
    #print("\n" * 20)
    print(logo)

    #This comparison is for the assigment of new 'celeb1' in case is correct
    if choice == 'A':
        #auxcho = celeb1['follower_count']
        auxcho = celeb1
        celebx = celeb2
        val = count_checker(auxcho, celebx)

    elif choice == 'B':
        auxcho = celeb2
        celebx = celeb1
        val = count_checker(auxcho, celebx)
        #newcel = logic_checker(auxcho, celebx)
        #celeb1 = newcel

    if val == True:
        score +=1   #remember score = score +1
        print(f"You're right! Current score: {score}")
    else :
        print(f"Sorry, that's wrong. Your final score: {score}")
        streak = False
