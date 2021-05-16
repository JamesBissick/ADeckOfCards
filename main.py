import turtle

window = turtle.Screen()
window.bgcolor('black')
window.setup(800, 600)
window.title('Deck of Cards by @JamesBissick')

# Create classes
class Card():
    def __init__(self, name, suite):
        self.name = name
        self.suite = suite

    def print_card(self):
        print(self.name, self.suite)

card = Card('A', 'S')
card.print_card()

window.mainloop()