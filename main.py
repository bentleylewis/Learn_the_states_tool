import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
correct_guesses = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

states_list = data["state"]
game_is_on = True
score = 0
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        correct_guesses.append(answer_state)
        score += 1
        state_search = data[data["state"].str.contains(f"{answer_state}", case=False)]
        x_value = float(state_search['x'].values[0])
        y_value = float(state_search['y'].values[0])
        writer.goto(x_value, y_value)
        writer.write(f"{answer_state}", align='left', font=('Arial', 8, 'normal'))




screen.exitonclick()