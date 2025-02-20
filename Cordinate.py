import turtle
import pandas as pd
import os
from tkinter import Tk, simpledialog, messagebox, Button

# 📂 File Paths
OUTPUT_FILE = "sindh_coordinates.xlsx"

# 🛠 Ensure Output Directory Exists
if not os.path.exists(OUTPUT_FILE):
    df = pd.DataFrame(columns=["City", "X", "Y"])
    df.to_excel(OUTPUT_FILE, index=False, engine="openpyxl")

# 📌 Setup Turtle Screen
screen = turtle.Screen()
screen.title("Find X, Y Coordinates on Punjab Map")
screen.bgcolor("Black")

# 🎨 Load Image
image = "sindh.gif"
if not os.path.exists(image):
    messagebox.showerror("Error", f"Image file not found: {image}")
    exit()

screen.addshape(image)
turtle.shape(image)

# 📋 Load Existing Data
df = pd.read_excel(OUTPUT_FILE)

# 🖱 Capture Mouse Clicks & Save Coordinates
def get_mouse_click_coords(x, y):
    """Get coordinates and save to Excel."""
    root = Tk()  # Create a temporary hidden Tkinter window
    root.withdraw()  # Hide Tkinter window

    city_name = simpledialog.askstring("City Name", "Enter the city name:")
    if city_name:
        # Draw Red Spot
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.dot(10, "red")  # Draw red dot

        # ✅ Place City Name EXACTLY at the Spot
        t.goto(x, y - 10)  # Move slightly up for better alignment
        t.write(city_name.title(), align="center", font=("Arial", 12, "bold"))

        # Save to Excel
        global df
        new_data = pd.DataFrame({"City": [city_name.title()], "X": [x], "Y": [y]})
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel(OUTPUT_FILE, index=False, engine="openpyxl")

        print(f"Saved: {city_name}, X={x}, Y={y}")  # Show confirmation in terminal

    root.destroy()  # Close Tkinter instance after input

# 🎯 Bind Click Event
screen.onscreenclick(get_mouse_click_coords)

# 🎛 Add "Save & Exit" Button
def save_and_exit():
    """Show confirmation and close the Turtle screen."""
    messagebox.showinfo("Success", f"Coordinates saved to: {OUTPUT_FILE}")
    screen.bye()  # Close Turtle screen

# 🖥 Tkinter Button UI
tk_root = Tk()
tk_root.withdraw()  # Hide root window

save_button = Button(tk_root, text="Save & Exit", command=save_and_exit)
save_button.pack()
tk_root.mainloop()

# 🏁 Keep Screen Open
screen.mainloop()
