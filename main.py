import turtle
import pandas


screen = turtle.Screen()
screen.title("Guess Indian States")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("indian_states_new.csv")
all_states = data.State.to_list()
guessed_states = []

while len(guessed_states)<29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 correct states", prompt="What's another state's name").title()

    if answer_state=="Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["State"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



