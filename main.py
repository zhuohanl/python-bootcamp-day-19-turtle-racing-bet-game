from turtle import Turtle, Screen
import random
import tkinter as tk


# Define a function to close the window when clicked
def close_window(event):
    event.widget.destroy()
    event.widget.quit()


# Define a function to output message in GUI to user
def output_text_in_gui(message):

    # Create a new window
    window = tk.Tk()

    # Set the title of the window
    window.title("Output Window")

    # Set the size of the window
    window.geometry("400x200")

    # Calculate the x and y positions of the window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) / 2 - 150
    y = (screen_height - window.winfo_reqheight()) / 2

    # Set the position of the window to the center of the screen
    window.geometry("+%d+%d" % (x, y))

    # Create a label widget with some text centered in it
    output_label = tk.Label(window, text=message, font=("Arial", 14), anchor="center")

    # Add the label widget to the window
    output_label.pack(fill=tk.BOTH, expand=1)

    # Bind the function to the window's Button-1 event
    window.bind("<Button-1>", close_window)

    # Show the window
    window.deiconify()

    # Start the main event loop to display the window
    window.mainloop()


def play_turtle_racing():
    is_race_on = False

    # Set up the canvas
    canva_width = 600
    canva_height = 400
    screen = Screen()
    screen.setup(width=canva_width, height=canva_height)

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # Get user bet
    user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color below \n"
                                                              f"You can choose from {colors}:").lower()

    # Set up the turtles
    all_turtles = []
    # -70, -40, -10, 20, 50, 80
    y_lowest = -70
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        y_lowest += 30
        new_turtle.goto(x=-(canva_width/2 - 30), y=y_lowest)
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

            # For debugging use
            # print(f"{turtle.pencolor()} : {turtle.position()[0]}")

            if turtle.xcor() >= (canva_width/2 - 30):
                is_race_on = False
                winner_color = turtle.pencolor()

                if winner_color == user_bet:
                    output_text_in_gui(f"You win!\n The {winner_color.upper()} turtle wins.")
                else:
                    output_text_in_gui(f"You lose.\n The {winner_color.upper()} turtle wins while you bet on {user_bet.upper()}.")

    screen.exitonclick()


play_turtle_racing()