from turtle import Turtle, Screen
import random
tim = Turtle()
#tim.shape("turtle")
#tim.color("green")

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# for i in range(10):
#     tim.forward(10)
#     tim.dot(10)

# for i in range(15):
#     tim.forward(10) #düz çizgi uzunluğu
#     tim.penup() #kalemi yukarı kaldırır yani hareket eder ama çizmez
#     tim.forward(10)
#     tim.pendown()

colours = ["pink", "green", "blue", "wheat", "DeepSkyBlue", "IndianRed"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for i in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(i)

# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")
# for i in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
tim.penup()
tim.setx(-100)
tim.pendown()
tim.pensize(10)
tim.speed("slow")

for i in range(4):
    tim.color(random.choice(colours))
    tim.forward(90)
    tim.right(90)

tim.penup()
tim.forward(150)
tim.right(90)
tim.forward(90)
tim.left(90)
tim.pendown()
tim.forward(5)
tim.color(random.choice(colours))
tim.penup()
tim.forward(55)
tim.left(90)
tim.pendown()
tim.forward(90)
for i in range(3):
    tim.color(random.choice(colours))
    tim.right(90)
    tim.forward(50)





screen = Screen()
screen.exitonclick()
