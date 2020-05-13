from menu import *
from new_movement import *


def main():
    """ Main Game Window """
    win = GraphWin("My Rectangle", 1200, 600)
    menu = MyMenu(win)
    menu.openStartMenu()

    """ Set up player """
    player = Player(50, 10, 0, "village")
    player_tracker = Tracker(win, player)
    player_tracker.addPlayer(50, 50, 50)
    player_tracker.watchPlayer()    # move doesn't work

    # win.getMouse()  # pause for click in window
    # win.close()
    win.mainloop()


main()