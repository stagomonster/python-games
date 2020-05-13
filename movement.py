from graphics import *
import turtle


class Player:
    def __init__(self, health, attack, status, room):
        self.health = health
        self.attack = attack
        self.status = status
        self.room = room
        self.char = Rectangle(Point(680, 420), Point(720, 380))

    def m_up(self):
        self.char.move(0, -10)

    def m_down(self):
        self.char.move(0, 10)

    def m_right(self):
        self.char.move(10, 0)

    def m_left(self):
        self.char.move(-10, 0)
