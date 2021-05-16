import turtle
import time

window = turtle.Screen()
window.bgcolor('black')
window.setup(800, 600)
window.title('Deck of Cards by @JamesBissick')

pen = turtle.Turtle()
# pen.speed(0)
pen.hideturtle()
time.sleep(3)


# Create classes
class Card():
    def __init__(self, name, suite):
        self.name = name
        self.suite = suite
        # diamonds(♦), clubs(♣), hearts(♥) and spades(♠)
        self.symbols = {'D': '♦', 'C': '♣', 'H': '♥', 'S': '♠', }

    def print_card(self):
        if self.suite == 'S':
            symbol = '♠'
        print(f"{self.name}{self.symbols[self.suite]}")

    def render(self, x, y, pen):
        # Draw the border
        pen.penup()
        pen.goto(x, y)
        pen.color('white')
        pen.goto(x - 50, y + 75)
        pen.pendown()
        pen.goto(x + 50, y + 75)
        pen.goto(x + 50, y - 75)
        pen.goto(x - 50, y - 75)
        pen.goto(x - 50, y + 75)
        pen.penup()

        # Draw suites in the middle
        pen.goto(x-18, y-30)
        pen.write(self.symbols[self.suite], False, font=('Courrier New', 48, 'normal'))


card = Card('A', 'S')
card.render(0, 0, pen)

window.mainloop()
