import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("My Quiz Punjab State Game")
image = "sindh.gif"
screen.bgcolor("Black")
screen.addshape(image)
turtle.shape(image)
guess_answer = []
while len(guess_answer)<35:
    input_state = screen.textinput(title=f"{len(guess_answer)}/25 Guess the State", prompt="What is another state name").title()
    print(input_state)
    df = pd.read_csv("Sindh_1.csv")
    all_state = df.state.to_list()

    if input_state in all_state:
        guess_answer.append(input_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == input_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(input_state)

screen.exitonclick()