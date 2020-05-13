# menu.py
# Displays Main Sidebar Menu for python graphic game

from graphics import *


class MyMenu:

    def __init__(self, window):
        """ Sets up initial menu side bar """
        self.parent = window
        self.origin = Point(50, 50)

        self.sidebar = Rectangle(self.origin, Point(150, 600))
        self.sidebar.draw(self.parent)
        self.sidebar.setFill(color_rgb(0, 0, 50))

    def setColor(self):
        self.sidebar.setFill(color_rgb(0, 0, 0))

    def setSize(self, height, width):
        y = Point(width, height)
        self.sidebar = Rectangle(self.origin, y)
        self.sidebar.draw(self.parent)

