import turtle
import pandas as pd

# Setup screen
screen = turtle.Screen()
screen.title("Punjab State Map - Cities with Spots")
screen.bgcolor("white")

# Load image
image = "sindh.gif"
screen.addshape(image)
turtle.shape(image)

# Load CSV data
df = pd.read_csv("sindh_1.csv")

# Convert state names to lowercase for consistency
df["state"] = df["state"].str.lower()

# Loop through each city and place a spot with a label
for _, row in df.iterrows():
    city_name = row["state"]  # City name
    x, y = int(row["x"]), int(row["y"])  # Coordinates

    # Create turtle to place text and dot
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)

    # Draw a red spot
    t.dot(10, "red")  # Adjust size and color as needed

    # Write city name
    t.goto(x + 10, y + 5)  # Slight offset for readability
    t.write(city_name.title(), align="left", font=("Arial", 10, "bold"))

# Keep the window open until clicked
screen.exitonclick()
