#!/usr/bin/env python3
from models import Person, Elevator
from time import sleep
import curses


# Actually the task is the following: 
# Make the simulation input sequence (I need to figure how
# it will look) and then test the same
# sequence in two different simulations,
# then compare the results - time in which all people are transfered
# to wanted floors
class Simulation():
    
    elevators: list[Elevator]
    persons: list[Person]
    visual_mode: bool  # If visual mode is False calculations will be instant
 

def main(stdscr):
    FPS = 15

    stdscr.addstr("It's working!!!")
    stdscr.refresh()
    sleep(1)


if __name__ == '__main__':
    curses.wrapper(main)

