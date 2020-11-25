import art
import os
import random


def clear(): 
      # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 


def play_game():
    print(art.logo)
    print("Welcome to Number Guessing !")
    print("I'm thinking of a number between 1 and 100")

    difficulty = input("Do you want to make it 'easy' or 'hard'?: ")
    random_number = random.randint(1,100)
    lives = 0
    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5
    else:
        lives = 1

    print (f"You have {lives} lives for this round")

    while lives > 0:
        guess = int(input('Guess a number: '))
        if guess < random_number:
            print ('Guess too low')
            lives -= 1
        if guess > random_number:
            print ('Guess too high')
            lives += 1
        if guess == random_number:
            print ('You guessed right !')
            lives = 0
        print (f"You have {lives} lives remaining")

    return (f"The right answer was {guess}")


    
play = input("Do you want to play ? 'y' or 'n'.: ")

while play == 'y':
    play_game()
    play = input("Do you want to play again ? 'y' or 'n'.: ")
    clear()
    