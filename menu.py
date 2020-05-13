# menu.py

from graphics import *


######################################################################
# Menu class

class MyMenu:
    """ Displays Main Sidebar Menu for python graphic game """

    def __init__(self, window):
        """ Sets up initial menu side bar """
        self.parent = window
        self.origin = Point(50, 50)

        self.sidebar = Rectangle(self.origin, Point(200, 550))
        self.sidebar.draw(self.parent)
        self.sidebar.setFill(color_rgb(0, 0, 50))

    def setColor(self):
        self.sidebar.setFill(color_rgb(0, 0, 0))

    def setSize(self, height, width):
        y = Point(width, height)
        self.sidebar = Rectangle(self.origin, y)
        self.sidebar.draw(self.parent)

    def openStartMenu(self):
        """ Same left and right buffer """
        left_xbuffer = self.origin.getX() + 15
        right_xbuffer = left_xbuffer + 100 + 20

        """ New Game button """
        left_y = self.origin.getY() + 15
        right_y = left_y + 30
        # print(left_y, right_y)

        buffer_origin = Point(left_xbuffer, left_y)  # top left
        b_new_game_end = Point(right_xbuffer, right_y)  # bottom right

        b_new_game = Rectangle(buffer_origin, b_new_game_end)
        b_new_game.draw(self.parent)
        b_new_game.setFill(color_rgb(255, 255, 0))
        label_new_game = Text(b_new_game.getCenter(), "New Game")
        label_new_game.draw(self.parent)

        """ New Game button """
        left_y = right_y + 10
        right_y = left_y + 30
        # print(left_y, right_y)

        buffer_origin = Point(left_xbuffer, left_y)  # top left
        b_new_game_end = Point(right_xbuffer, right_y)  # bottom right

        b_new_game = Rectangle(buffer_origin, b_new_game_end)
        b_new_game.draw(self.parent)
        b_new_game.setFill(color_rgb(255, 255, 0))
        label_new_game = Text(b_new_game.getCenter(), "New Game")
        label_new_game.draw(self.parent)

        """ New Game button """
        left_y = right_y + 10
        right_y = left_y + 30
        # print(left_y, right_y)

        buffer_origin = Point(left_xbuffer, left_y)  # top left
        b_new_game_end = Point(right_xbuffer, right_y)  # bottom right

        b_new_game = Rectangle(buffer_origin, b_new_game_end)
        b_new_game.draw(self.parent)
        b_new_game.setFill(color_rgb(255, 255, 0))
        label_new_game = Text(b_new_game.getCenter(), "New Game")
        label_new_game.draw(self.parent)

        """ New Player button """
        left_y = right_y + 10
        right_y = left_y + 30
        # print(left_y, right_y)

        b_origin = Point(left_xbuffer, left_y)  # top left
        b_end = Point(right_xbuffer, right_y)  # bottom right

        b_new_player = Rectangle(b_origin, b_end)
        b_new_player.draw(self.parent)
        b_new_player.setFill(color_rgb(255, 255, 0))
        label_new_player = Text(b_new_player.getCenter(), "New Player")
        label_new_player.draw(self.parent)

        """ New Player button """
        left_y = right_y + 10
        right_y = left_y + 30
        # print(left_y, right_y)

        b_origin = Point(left_xbuffer, left_y)  # top left
        b_end = Point(right_xbuffer, right_y)  # bottom right

        b_new_player = Rectangle(b_origin, b_end)
        b_new_player.draw(self.parent)
        b_new_player.setFill(color_rgb(255, 255, 0))
        label_new_player = Text(b_new_player.getCenter(), "New Player")
        label_new_player.draw(self.parent)

        """ New Player button """
        left_y = right_y + 10
        right_y = left_y + 30
        # print(left_y, right_y)

        b_origin = Point(left_xbuffer, left_y)  # top left
        b_end = Point(right_xbuffer, right_y)  # bottom right

        b_new_player = Rectangle(b_origin, b_end)
        b_new_player.draw(self.parent)
        b_new_player.setFill(color_rgb(255, 255, 0))
        label_new_player = Text(b_new_player.getCenter(), "New Player")
        label_new_player.draw(self.parent)

        """ New Player button """
        left_y = right_y + 10
        right_y = left_y + 30
        # print(left_y, right_y)

        b_origin = Point(left_xbuffer, left_y)  # top left
        b_end = Point(right_xbuffer, right_y)  # bottom right

        b_new_player = Rectangle(b_origin, b_end)
        b_new_player.draw(self.parent)
        b_new_player.setFill(color_rgb(255, 255, 0))
        label_new_player = Text(b_new_player.getCenter(), "New Player")
        label_new_player.draw(self.parent)