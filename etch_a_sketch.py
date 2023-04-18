# THIS IS A SH+KETCH BOARD PROGRAM

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()



def move_forwards():
    tim.forward(10)
def move_back():
    tim.backward(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)



def delete_board():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(delete_board, "c")












screen.exitonclick()