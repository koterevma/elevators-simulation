#!/usr/bin/env python3
from models import Person, Elevator
import curses
import time


# Actually the task is:
# Make the simulation input sequence (I need to figure how
# it will look) and then test the same
# sequence in two different simulations.
# Then compare the results - the time for which people
# were transported to the desired floors
class Simulation():

    elevators: list[Elevator]
    persons: list[Person]
    current_time: float = 0


def visualise(stdscr):
    FPS = 15
    start = time.time()
    stdscr.addstr(str(start))
    stdscr.refresh()
    time.sleep(2)
    stdscr.erase()
    stdscr.addstr(str(time.time() - start))
    stdscr.refresh()
    time.sleep(2)


def simulate():
    pass


if __name__ == '__main__':
    # if "--visual" in sys.argv:
    curses.wrapper(visualise)
    # else:
    #     simulate()
