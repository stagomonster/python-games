# new_movement.py

from graphics import *


###############################################################
# Global character


#####################################################################
# Player class

class Player:
    def __init__(self, health, attack, status, room):
        """ Player Attributes """
        self.health = health
        self.attack = attack
        self.status = status
        self.room = room
        self.char = Rectangle(Point(680, 420), Point(720, 380))

    def m_up(self):
        self.char.move(0, -10)
        self.health -= 0.1
        print("up")

    def m_down(self):
        self.char.move(0, 10)
        self.health -= 0.1
        print("down")

    def m_right(self):
        self.char.move(10, 0)
        self.health -= 0.1
        print("right")

    def m_left(self):
        self.char.move(-10, 0)
        self.health -= 0.1
        print("left")


####################################################################
# Movement class
class Tracker():

    def __init__(self, window: GraphWin, player: Player):
        """ Set up tracker """
        self.player = player
        self.origin = Point(600, 350)
        self.space = window

        """ Set up player sprite """
        # global char
        # sprite = Circle(self.origin, 50)
        # self.sprite = Circle(self.origin, 50)

    def addPlayer(self, r, g, b):
        """ Display player sprite """
        self.player.char.draw(self.space)
        self.player.char.setFill(color_rgb(r, g, b))
        # self.sprite.draw(self.space)
        # self.sprite.setFill(color_rgb(r, g, b))

    def watchPlayer(self):
        """ Listen to arrow key inputs to move player """
        self.space.bind("<KeyPress-Up>", self.player.m_up(), None)
        self.space.bind("<KeyPress-Down>", self.player.m_down(), None)
        self.space.bind("<KeyPress-Left>", self.player.m_left(), None)
        self.space.bind("<KeyPress-Right>", self.player.m_right(), None)
        # self.space.flush()

    def removePlayer(self):
        """ Delete player sprite """
        self.player.char.undraw()
        # self.sprite.undraw()

    def getPlayerLocation(self):
        """ Return coordinates of player """
        return self.player.char.getCenter()
        # return self.sprite.getCenter()
