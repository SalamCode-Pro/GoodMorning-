import turtle
import time

def draw_text(text, size, color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.write(text, font=("Arial", size, "normal"))

def main():
    turtle.speed(2)
    
    draw_text("Good", 40, "blue", -50, 0)
    time.sleep(1)
    turtle.clear()

    draw_text("Morning", 40, "green", -50, 0)
    time.sleep(1)
    turtle.clear()

    draw_text("World!", 40, "red", -50, 0)

    turtle.done()

if __name__ == "__main__":
    main()
