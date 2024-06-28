import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY25-US_States_Game/Resources/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY25-US_States_Game/Resources/50_states.csv')
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY25-US_States_Game/Resources/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(answer_state)


# Get the x and y co-ordinates of mouse click on states.

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
