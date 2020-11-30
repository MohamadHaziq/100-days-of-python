from turtle import Turtle, Screen, colormode
import random

colormode(255)

color_list = [(232, 227, 219), (211, 158, 101), (223, 238, 231), (217, 230, 238), (119, 170, 197), (237, 220, 228), (46, 107, 148), (181, 168, 33), (191, 143, 165), (227, 204, 115), (129, 181, 158), (146, 64, 94), (162, 82, 50), (46, 128, 85), (145, 26, 47), 
(197, 81, 111), (220, 85, 55), (62, 168, 134), (35, 169, 194), (224, 170, 190), (68, 28, 50), (149, 214, 199), (70, 33, 22), (30, 40, 71), (35, 55, 116), (236, 171, 158), (105, 118, 173), (143, 212, 223), (142, 31, 22), (14, 100, 57)]


timmy = Turtle()
timmy.hideturtle()
timmy.speed(0)
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

number_dots = 100


for dot_count in range(1,number_dots + 1):
    timmy.dot(20,random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = Screen()
screen.exitonclick()