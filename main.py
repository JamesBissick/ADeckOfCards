import turtle
import time
import random

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
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        # diamonds(♦), clubs(♣), hearts(♥) and spades(♠)
        self.symbols = {'D': '♦', 'C': '♣', 'H': '♥', 'S': '♠', }

    def print_card(self):
        if self.suit == 'S':
            symbol = '♠'

        print(f"{self.name}{self.symbols[self.suit]}")

    def render(self, x, y, pen):
        # Draw the border
        pen.penup()
        pen.goto(x, y)
        pen.color('white')
        pen.goto(x - 50, y + 75)
        pen.begin_fill()
        pen.pendown()
        pen.goto(x + 50, y + 75)
        pen.goto(x + 50, y - 75)
        pen.goto(x - 50, y - 75)
        pen.goto(x - 50, y + 75)
        pen.end_fill()
        pen.penup()

        # Draw suits in the middle
        if self.symbols[self.suit] == '♦':
            pen.color('red')
        elif self.symbols[self.suit] == '♣':
            pen.color('black')
        elif self.symbols[self.suit] == '♥':
            pen.color('red')
        elif self.symbols[self.suit] == '♠':
            pen.color('black')

        # Draw suits in the middle
        pen.goto(x - 18, y - 30)
        pen.write(self.symbols[self.suit], False, font=('Courrier New', 48, 'normal'))

        if self.name != '10':
            # Draw top left
            pen.goto(x - 39, y + 47)
            pen.write(self.name, False, font=('Courrier New', 18, 'normal'))
            pen.goto(x - 40, y + 30)
            pen.write(self.symbols[self.suit], False, font=('Courrier New', 18, 'normal'))

            # Draw bottom right
            pen.goto(x + 31, y - 53)
            pen.write(self.name, False, font=('Courrier New', 18, 'normal'))
            pen.goto(x + 29, y - 71)
            pen.write(self.symbols[self.suit], False, font=('Courrier New', 18, 'normal'))
        else:
            # Draw top left
            pen.goto(x - 43, y + 47)
            pen.write(self.name, False, font=('Courrier New', 18, 'normal'))
            pen.goto(x - 40, y + 30)
            pen.write(self.symbols[self.suit], False, font=('Courrier New', 18, 'normal'))

            # Draw bottom right
            pen.goto(x + 25, y - 53)
            pen.write(self.name, False, font=('Courrier New', 18, 'normal'))
            pen.goto(x + 29, y - 71)
            pen.write(self.symbols[self.suit], False, font=('Courrier New', 18, 'normal'))


class Deck():
    def __init__(self):
        self.cards = []
        names = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        suits = ('D', 'C', 'H', 'S')

        for name in names:
            for suit in suits:
                card = Card(name, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        card = self.cards.pop()
        return card


# Create deck and shuffle it
deck = Deck()
deck.shuffle()

# Render 5 cards in the screen
start_x = -250
for x in range(5):
    card = deck.get_card()
    card.render(start_x + x * 125, 0, pen)

window.mainloop()
