import tkinter as tk
import math
# import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE = "./day_22-30/day_28/tomato.png"

reps = 0 
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = f"00:00")
    title_label.config(text = "Timer")
    checkmark_label.config(text = "")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text = "LONG BREAK", fg = RED, bg = YELLOW, font = (FONT_NAME, 40))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text = "SHORT BREAK", fg = PINK, bg = YELLOW, font = (FONT_NAME, 40))
    else:
        count_down(work_sec)
        title_label.config(text = "WORKING", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 40))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark_label.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx = 25, pady = 25, bg = YELLOW)

## Title
title_label = tk.Label(text = "Timer")
title_label.config(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 40))
title_label.grid(column = 1, row = 0)

## Image of Tomato
canvas = tk.Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file = IMAGE)
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = 'white', font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

# count_down()

start_button = tk.Button(text = "Start", command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = tk.Button(text = "Reset", command = reset_timer)
reset_button.grid(column = 2, row = 2)

checkmark = "✔"
checkmark_label = tk.Label()
checkmark_label.config(fg = GREEN, bg = YELLOW)
checkmark_label.grid(column = 1, row = 3)

window.mainloop()