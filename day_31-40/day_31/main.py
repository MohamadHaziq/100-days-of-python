import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK = "./day_31-40/day_31/images/card_back.png"
CARD_FRONT = "./day_31-40/day_31/images/card_front.png"
RIGHT_ANSWER = "./day_31-40/day_31/images/right.png"
WRONG_ANSWER = "./day_31-40/day_31/images/wrong.png"

try:
    data = pd.read_csv('./day_31-40/day_31/data/french_words_to_learn.csv')
    
except FileNotFoundError:
    data = pd.read_csv('./day_31-40/day_31/data/french_words.csv')
    
finally:
    data = data.to_dict(orient = 'records')
word = {}

##### Function to get new words #####
def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)

    word = random.choice(data)
    english = word['English']

    canvas.itemconfig(card_image, image = card_front)
    canvas.itemconfig(card_title, text = "French", fill = 'black')
    canvas.itemconfig(card_word, text = word['French'], fill = 'black')

    window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image = card_back)
    canvas.itemconfig(card_title, text = "English", fill = 'white')
    canvas.itemconfig(card_word, text = word['English'], fill = 'white')


def is_known():
    data.remove(word)
    words_to_learn = pd.DataFrame(data)
    words_to_learn.to_csv('./day_31-40/day_31/data/french_words_to_learn.csv', index = False)
    next_card()


##################################### START APP CODE #####################################

window = tk.Tk()
window.title("Flash Cards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

## Flashcard
canvas = tk.Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
card_front = tk.PhotoImage(file = CARD_FRONT)
card_back = tk.PhotoImage(file = CARD_BACK)
card_image = canvas.create_image(400, 262, image = card_front)
card_title = canvas.create_text(400,100, text = '', font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text = "", font = ("Ariel", 60, "bold"))
canvas.grid(column = 0, row = 0, columnspan = 2)


# answer buttons
wrong_button_image = tk.PhotoImage(file = WRONG_ANSWER)
wrong_button = tk.Button(image = wrong_button_image, highlightthickness = 0, bg = BACKGROUND_COLOR, command = next_card)
wrong_button.grid(column = 0, row = 1)

right_button_image = tk.PhotoImage(file = RIGHT_ANSWER)
right_button = tk.Button(image = right_button_image, highlightthickness = 0, bg = BACKGROUND_COLOR, command = is_known)
right_button.grid(column = 1, row = 1)

next_card()

window.mainloop()