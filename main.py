#!/usr/bin/env python3
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from models import Person, Elevator
import curses
import time


# Actually the task is:
# Make the simulation input sequence
# (It will be a list[tuple[Person, float]] where
# second value is a delay before the person
# will appear on the floor) and then test the
# same sequence in two different simulations.
# Then compare the results - the time for which people
# were transported to the desired floors
@dataclass
class Simulation(ABC):

    elevators: list[Elevator]
    people_waiting: list[Person]
    step: float
    test_sequence: list[tuple[Person, float]]
    # If end_time is None, simulation will go until no passengers left
    end_time: Optional[float] = None
    current_time: float = 0.0

    @abstractmethod
    def run_simulation(self):
        pass


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


if __name__ == '__main__':
    # if "--visual" in sys.argv:
    curses.wrapper(visualise)
    # else:
    #     simulate()
