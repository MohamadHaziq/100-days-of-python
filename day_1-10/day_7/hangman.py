import random
import hangman_art
from word_list import word_list

stages = hangman_art.stages

## List of possible words

chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)

lives = 6
print(lives)

while "_" in display and lives > 0:
    letter = input('Guess a letter !').lower()

    for position in range(len(chosen_word)):
        if letter == chosen_word[position]:
            display[position] = letter

    if letter in display:
        print (f"You already chose {letter}")
    
    if letter not in chosen_word:
        lives -= 1
    
    print(stages[lives])
    print(display)

if "_" not in display:
    print ("You win")
else:
    print ("Loser")

print ("Game over !")
print (f"The word was {chosen_word}")