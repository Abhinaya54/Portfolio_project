import turtle as tur

# Create a Turtle screen
screen = tur.Screen()
screen.bgcolor("black")

# Create a Turtle object
t = tur.Turtle()
t.speed(1)  # Set the drawing speed

# Function to draw a filled circle
def filled_circle(color, radius):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw Lord Vinayaka
def draw_ganesha():
    t.penup()

    # Draw the body
    t.goto(0, -150)
    t.pendown()
    t.color("orange")
    filled_circle("orange", 100)

    # Draw the head
    t.penup()
    t.goto(0, 0)
    t.pendown()
    filled_circle("orange", 60)

    # Draw the eyes
    t.penup()
    t.goto(-25, 30)
    t.pendown()
    t.color("black")
    filled_circle("black", 8)
    t.penup()
    t.goto(25, 30)
    t.pendown()
    filled_circle("black", 8)

    # Draw the ears
    t.penup()
    t.goto(-60, 20)
    t.pendown()
    t.setheading(150)
    t.circle(70, 40)

    t.penup()
    t.goto(60, 20)
    t.pendown()
    t.setheading(30)
    t.circle(70, 40)

    # Draw the trunk
    t.penup()
    t.goto(0, 60)
    t.pendown()
    t.setheading(270)
    t.forward(40)
    t.setheading(180)
    t.circle(20, 180)
    t.setheading(0)
    t.forward(20)

    t.hideturtle()

# Function to display wishes
def display_wishes():
    t.penup()
    t.goto(0, -180)
    t.color("gold")
    t.write("May Lord Vinayaka bless you with wisdom, success, and happiness!", align="center", font=("Arial", 14, "normal"))

# Draw Lord Vinayaka
draw_ganesha()

# Display wishes
display_wishes()

# Close the window on click
screen.exitonclick()

