import os
import turtle
import math

def recursive_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
        return

    third = length / 3
    recursive_edge(t, third, depth - 1)
    t.left(60)
    recursive_edge(t, third, depth - 1)
    t.right(120)
    recursive_edge(t, third, depth - 1)
    t.left(60)
    recursive_edge(t, third, depth - 1)

def draw_recursive_polygon(t, sides, side_length, depth):
    exterior_angle = 360 / sides
    for _ in range(sides):
        recursive_edge(t, side_length, depth)
        t.left(exterior_angle)

def main():
    sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    if sides < 3:
        print("Number of sides must be at least 3.")
        return

    # Try to create turtle screen safely
    try:
        screen = turtle.Screen()
    except Exception:
        print("\nTurtle needs a graphical display, but your environment has no GUI.")
        print("Run this in a normal Python setup (Windows/Mac terminal or VS Code) instead.\n")
        return

    screen.title("Recursive Polygon Pattern")
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)

    apothem = side_length / (2 * math.tan(math.pi / sides))
    t.penup()
    t.goto(-side_length / 2, -apothem)
    t.pendown()

    draw_recursive_polygon(t, sides, side_length, depth)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
