import turtle
import random

# List of typical Mondrian colors plus white and black for borders
colors = ['red', 'blue', 'yellow', 'white', 'black']

def draw_filled_rect(t, x, y, width, height, color):
    """Draw a filled rectangle at (x,y) with given width, height and color."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('black', color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def mondrian(t, x, y, width, height, horizontal_split=True, min_size=40):
    """Recursive Mondrian subdivision pattern."""
    # Base case: stop when too small
    if width < min_size or height < min_size:
        color = random.choice(colors)
        draw_filled_rect(t, x, y, width, height, color)
        return

    # Choose two random colors for the two rectangles
    color1 = random.choice(colors)
    color2 = random.choice(colors)

    if horizontal_split:
        # Horizontal split into 1/3 and 2/3 heights
        split = height / 3
        # Draw upper rectangle (1/3)
        draw_filled_rect(t, x, y, width, split, color1)
        # Draw lower rectangle (2/3)
        draw_filled_rect(t, x, y - split, width, height - split, color2)

        # Recurse on both rectangles, alternate split axis
        mondrian(t, x, y, width, split, not horizontal_split, min_size)
        mondrian(t, x, y - split, width, height - split, not horizontal_split, min_size)

    else:
        # Vertical split into 1/3 and 2/3 widths
        split = width / 3
        # Draw left rectangle (1/3)
        draw_filled_rect(t, x, y, split, height, color1)
        # Draw right rectangle (2/3)
        draw_filled_rect(t, x + split, y, width - split, height, color2)

        # Recurse on both rectangles, alternate split axis
        mondrian(t, x, y, split, height, not horizontal_split, min_size)
        mondrian(t, x + split, y, width - split, height, not horizontal_split, min_size)

def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('white')

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-250, 250)  # Top-left corner starting point

    mondrian(t, -250, 250, 500, 500, horizontal_split=True, min_size=40)

    screen.mainloop()

if __name__ == "__main__":
    main()
