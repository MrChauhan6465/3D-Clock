import turtle
import time

t = turtle.Turtle()
t.home()
t.screen.bgcolor("black")
t.color("white")
x = 0
y = 0
# t.write((x,y))
t.speed(20)
t.penup()
t.goto(x, -100)
t.pendown()
t.begin_fill()
t.fillcolor("red")
t.circle(100)
t.penup()
t.goto(x, -60)
t.pendown()
t.circle(60)
t.penup()
t.home()
t.left(90)
t.end_fill

for i in range(1, 13):
    t.right(360/12)
    t.forward(85)
    t.write(i)
    t.goto(0, 0)


def draw_hour_arm():
    t.penup()
    t.home()
    t.pendown()
    t.right(180)
    t.pensize(5)
    t.forward(40)


def draw_minute_arm():
    t.penup()
    t.home()
    t.pendown()
    t.pensize(3)
    t.right(270)
    t.forward(70)


draw_hour_arm()
draw_minute_arm()


t.pensize(2)
angle = 1
while True:
    start = time.time()
    first_start = 1
    if first_start == 1:
        t.penup()
        t .home()
        t.left(90)
        first_start = 2
    t.pendown()
    t.right(angle)
    t.forward(60)
    time.sleep(1-(time.time()-start))
    t.undo()
    t.penup()
    t.goto(0, 0)
    t.right(360/60)
    angle += 360/60
turtle.done()
