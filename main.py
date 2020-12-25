from turtle import Turtle, Screen

harry = Turtle()
screen = Screen()

def move_forwards():
    harry.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()