import turtle
import time

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("sky blue")
screen.title("Car Animation")

# Create the car body
car_body = turtle.Turtle()
car_body.shape("circle")
car_body.color("blue")
car_body.penup()
car_body.shapesize(stretch_wid=2, stretch_len=5)  # Resize to make it look like a car
car_body.goto(-300, 0)

# Create the car wheels
wheel1 = turtle.Turtle()
wheel1.shape("circle")
wheel1.color("black")
wheel1.penup()
wheel1.goto(-330, -20)

wheel2 = turtle.Turtle()
wheel2.shape("circle")
wheel2.color("black")
wheel2.penup()
wheel2.goto(-270, -20)

# Function to move the car
def move_car():
    for _ in range(120):  # Move for 120 frames
        car_body.forward(5)
        wheel1.forward(5)
        wheel2.forward(5)
        time.sleep(0.05)  # Slow down the animation slightly

# Start the animation
move_car()

# End the program gracefully
screen.mainloop()