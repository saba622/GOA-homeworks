import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("sky blue")

# Create the turtle
castle = turtle.Turtle()
castle.speed(6)

# Function to draw a rectangle (used for the castle walls)
def draw_rectangle(width, height, color):
    castle.begin_fill()
    castle.fillcolor(color)
    for _ in range(2):
        castle.forward(width)
        castle.left(90)
        castle.forward(height)
        castle.left(90)
    castle.end_fill()

# Function to draw a triangle (used for the castle roof)
def draw_triangle(side, color):
    castle.begin_fill()
    castle.fillcolor(color)
    for _ in range(3):
        castle.forward(side)
        castle.left(120)
    castle.end_fill()

# Function to draw a tower
def draw_tower(x, y, width, height, tower_color, roof_color):
    castle.penup()
    castle.goto(x, y)
    castle.pendown()
    draw_rectangle(width, height, tower_color)
    
    # Draw the tower roof
    castle.penup()
    castle.goto(x - width / 2, y + height)
    castle.pendown()
    draw_triangle(width, roof_color)

# Function to draw a door
def draw_door(x, y, width, height):
    castle.penup()
    castle.goto(x, y)
    castle.pendown()
    draw_rectangle(width, height, "brown")

# Drawing the main castle structure
castle.penup()
castle.goto(-200, -100)
castle.pendown()
draw_rectangle(400, 200, "gray")

# Drawing towers
draw_tower(-250, -100, 50, 150, "dark gray", "red")
draw_tower(200, -100, 50, 150, "dark gray", "red")

# Drawing the castle roof
castle.penup()
castle.goto(-230, 100)
castle.pendown()
draw_triangle(460, "dark red")

# Drawing the door
draw_door(-40, -100, 80, 120)

# Hide the turtle
castle.hideturtle()

# Keep the window open
turtle.done()