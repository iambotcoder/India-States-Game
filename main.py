import turtle, pandas
from turtle import Turtle, Screen

screen = turtle.Screen()
turtle.title("India States Game")
image = "india_map_.gif"
screen.addshape(image)
screen.setup(width=600, height=600)

turtle.shape(image)

unguessed_sates = []
guessed_states = []
count = 0

data = pandas.read_csv("states_coords.csv")
remain_states = data.state.to_list()
# print(data)
while(count <29):

    answer_state = screen.textinput(title=f"{count}/29 States Correct", prompt=" What's another state name")

    if answer_state == "exit":
        break

    state = data[data['state'] == (answer_state.title())]

    if (len(state) > 0):
        guessed_states.append(answer_state.capitalize())
        # remain_states.remove(answer_state.capitalize())
        count += 1
        state_xcor = (state.values.tolist()[0][1])
        state_ycor = (state.values.tolist()[0][2])
        # print(state, state_xcor, state_ycor)
        label = Turtle()
        label.penup()
        label.goto(state_xcor, state_ycor)
        label.pendown()
        label.write(answer_state)
        label.hideturtle()
# # data = pandas.DataFrame(remain_states)
# # data.to_csv("remain_states.csv")


        # print(f" Posision | X: {state_x} | Y: {state_y}")
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

# screen.exitonclick()

