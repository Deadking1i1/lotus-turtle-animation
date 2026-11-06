import turtle
import time

# --- Screen setup ---
screen = turtle.Screen()
screen.bgcolor("#4dbdc5")        # blue pond
screen.setup(800, 600)
screen.tracer(0)
screen.colormode(255)          # RGB mode for glow

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# --- Draw solid lily pad ---
def draw_lily_pad(x, y, size):
    pen.penup()
    pen.goto(x, y - size)
    pen.setheading(0)
    pen.color("#109648")
    pen.begin_fill()
    pen.pendown()
    pen.circle(size)
    pen.end_fill()

# --- Draw filled petal ---
def draw_petal(radius, angle, color):
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.circle(radius, angle)
        pen.left(180 - angle)
    pen.end_fill()

# --- Draw glowing yellow center ---
def draw_glow_center(x, y, size):
    glow_layers = 6
    for i in range(glow_layers):
        pen.penup()
        pen.goto(x, y - size * (0.12 + i * 0.02))
        pen.setheading(0)
        shade = 255 - i * 20
        pen.color((255, shade, 0))
        pen.begin_fill()
        pen.pendown()
        pen.circle(size * (0.12 + i * 0.02))
        pen.end_fill()
    # Bright core
    pen.penup()
    pen.goto(x, y - size * 0.12)
    pen.color("yellow")
    pen.begin_fill()
    pen.pendown()
    pen.circle(size * 0.12)
    pen.end_fill()

# --- Draw flower with big + smaller petals ---
def draw_flower(x, y, open_factor, size):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(90)
    pen.pendown()

    petals = 10

    # --- Big petals ---
    for _ in range(petals):
        radius = size * (0.50 + open_factor * 0.8)
        angle = 30 + open_factor * 25
        draw_petal(radius, angle, "#d00790")
        pen.left(360 / petals)

    # --- Smaller petals in between ---
    pen.left(360 / (2 * petals))  # offset to fit between big petals
    for _ in range(petals):
        radius = size * (0.5 + open_factor * 0.2)  # smaller radius
        angle = 65 + open_factor * 7             # smaller angle
        draw_petal(radius, angle, "#be2e6f")     # lighter pink
        pen.left(360 / petals)
        
    # --- Smaller petals in between 2 ---
    pen.left(360 / (2 * petals))  # offset to fit between big petals
    for _ in range(petals):
        radius = size * (0.5 + open_factor * 0.2)  # smaller radius
        angle = 50 + open_factor * 4            # smaller angle
        draw_petal(radius, angle, "#dd5db7")     # lighter pink
        pen.left(360 / petals)
        
    # --- Smaller petals in between 3 ---
    pen.left(360 / (2 * petals))  # offset to fit between big petals
    for _ in range(petals):
        radius = size * (0.5 + open_factor * 0.2)  # smaller radius
        angle = 50 + open_factor * 3           # smaller angle
        draw_petal(radius, angle, "#e36fc0")     # lighter pink
        pen.left(360 / petals)

  # --- Smaller petals in between 4 ---
    pen.left(360 / (2 * petals))  # offset to fit between big petals
    for _ in range(petals):
        radius = size * (0.5 + open_factor * 0.2)  # smaller radius
        angle = 45 + open_factor * 3           # smaller angle
        draw_petal(radius, angle, "#c62596")     # lighter pink
        pen.left(360 / petals)
 
    # --- Glowing yellow center ---
    draw_glow_center(x, y, size)

# --- Fixed lily pad positions ---
lilies = [
    {"x": 0, "y": 0, "size": 100, "speed": 0.02, "open": 0},          # middle
    {"x": -250, "y": -150, "size": 80, "speed": 0.015, "open": 0},    # bottom-left
    {"x": 250, "y": 180, "size": 60, "speed": 0.018, "open": 0},      # top-right
    {"x": 250, "y": -150, "size": 70, "speed": 0.017, "open": 0},     # bottom-right
    {"x": -250, "y": 180, "size": 80, "speed": 0.016, "open": 0}      # top-left
]

# --- Animation loop ---
while True:
    pen.clear()
    for lily in lilies:
        if lily["open"] < 1:
            lily["open"] += lily["speed"]
        draw_lily_pad(lily["x"], lily["y"], lily["size"])
        draw_flower(lily["x"], lily["y"], lily["open"], lily["size"])
    screen.update()
    time.sleep(0.03)

turtle.done()