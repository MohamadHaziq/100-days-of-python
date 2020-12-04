import pandas as pd
import turtle

FONT = ("Courier", 24, "normal")

data = pd.read_csv("D:/DevWork_Git/100-days-of-python/day_22-30/day_25/50_states.csv")

screen = turtle.Screen()
screen.title("US States Game")
image = "D:/DevWork_Git/100-days-of-python/day_22-30/day_25/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

statewriter = turtle.Turtle()
statewriter.hideturtle()
statewriter.penup()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"Guess The State {len(guessed_states)}:50", prompt = "This be your time to guess")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in list(data.state) if state not in guessed_states]
        # for state in data.state:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('no_answers.csv')
        print(missing_states)

        break

    for state in data.state:
        if answer_state == state:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state]
            statewriter.goto(int(state_data.x), int(state_data.y))
            statewriter.write(f"{answer_state}")

screen.exitonclick()