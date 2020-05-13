from graphics import *

char_color_input = input("What color would you like your character to be?")
char_color = Text(Point(700, 600), "What color would you like your character to be?")


class DialogueBox:

    def __init__(self, window):
        self.win = window
        self.box = Rectangle(Point(300, 700), Point(1100, 600))

    def dialogue_setup(self):
        self.box.draw(self.win)

    def setColor(self, color):
        self.box.setFill(color)

    def addText(self, text):
        message = Text(Point(700, 645), text)
        message.draw(self.win)
