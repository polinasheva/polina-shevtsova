import turtle
import random

screen = turtle.Screen()
screen.bgcolor("navy") 
screen.setup(800, 600)

moon = turtle.Turtle()
moon.speed(0)
moon.hideturtle()

def draw_crescent_moon(x, y, radius):
    moon.penup()
    moon.goto(x, y - radius)
    moon.pendown()
    
    moon.color("yellow")
    moon.begin_fill()
    moon.circle(radius)
    moon.end_fill()
    
    moon.penup()
    moon.goto(x - radius * 0.4, y - radius)
    moon.pendown()
    
    moon.color("navy")
    moon.begin_fill()
    moon.circle(radius * 1.1)
    moon.end_fill()

def draw_star(x, y, size, color="white"):
    star = turtle.Turtle()
    star.speed(0)
    star.hideturtle()
    star.penup()
    star.goto(x, y)
    star.pendown()
    
    star.color(color)
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()

def create_constellation(points, size=4, color="white", name=""):
    for point in points:
        x, y = point
        draw_star(x, y, size, color)
    
    if len(points) > 1:
        line = turtle.Turtle()
        line.speed(0)
        line.hideturtle()
        line.color(color)
        line.pensize(1)
        line.penup()
        line.goto(points[0])
        line.pendown()
        
        for point in points[1:]:
            line.goto(point)

def draw_random_stars():
    for _ in range(100):
        x = random.randint(-380, 380)
        y = random.randint(-280, 280)
        size = random.uniform(1, 3)
        draw_star(x, y, size)

draw_crescent_moon(-150, 100, 60)

draw_random_stars()

ursa_major = [(-300, 200), (-250, 220), (-200, 200),
    (-180, 160), (-220, 140), (-280, 150), (-300, 200)]
create_constellation(ursa_major, 5, "lightblue", "Большая Медведица")

orion = [(200, 150), (250, 180), (280, 150),
    (250, 120), (200, 100), (150, 120), (200, 150)]
create_constellation(orion, 5, "lightyellow", "Орион")

cassiopeia = [(0, 200), (50, 220), (100, 200),
    (120, 230), (80, 250), (0, 200)]
create_constellation(cassiopeia, 4, "lightgreen", "Кассиопея")

cygnus = [(-100, -100), (-50, -80), (0, -100),
    (50, -120), (0, -140), (-100, -100)]
create_constellation(cygnus, 4, "orange", "Лебедь")

ursa_minor = [(300, -150), (280, -120), (250, -100),
    (230, -120), (250, -140), (280, -160), (300, -150)]
create_constellation(ursa_minor, 3, "white", "Малая Медведица")

turtle.done()