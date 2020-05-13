from graphics import *
import random
from movement import *
from dialogue import *


def setup():
    window = GraphWin("Python Graphic Game", 1400, 800)
    char = Rectangle(Point(680, 420), Point(720, 380))
    char.setFill(color_rgb(0, 0, 0))
    box = DialogueBox(window)
    box.dialogue_setup()
    box.addText("Potatoes are epic")
    char.draw(window)
    window.getMouse()
    window.close()


def user_input(char):
    char.getKey()

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

setup()
