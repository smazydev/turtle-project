from turtle import Turtle, Screen

harry = Turtle()
screen = Screen()

def move_forwards():
    harry.forward(10)

def move_backwards():
    harry.forward(10)

def move_counter_clockwise():
    new_heading = harry.heading() + 10
    harry.setheading(new_heading)

def move_clockwise():
    new_heading = harry.heading() - 10
    harry.setheading(new_heading)

def clear():
    harry.clear()
    harry.penup()
    harry.home()
    harry.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()