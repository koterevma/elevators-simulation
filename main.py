#!/usr/bin/env python3
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
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
    step: float
    test_sequence: list[tuple[Person, float]]
    end_time: Optional[float] = None  # If None, simulation will go until no passengers left
    current_time: float = field(default=0.0, init=False)
    people_waiting: list[Person] = field(default_factory=list, init=False)

    @abstractmethod
    def run_simulation(self):
        pass


class SimpleSimulation(Simulation):

    def run_simulation(self):
        # People in test sequence will appear in simulation after the specified time period
        for i, (person, time_before_appearance) in enumerate(self.test_sequence):
            if time_before_appearance <= self.current_time:
                self.people_waiting.append(person)
                self.test_sequence.remove(i)
        
        if not self.test_sequence and not self.people_waiting:
            print("Simulation ended", f"Result time is {self.current_time}")
        


def visualise(stdscr):
    '''Will be implemented last'''
    pass


if __name__ == '__main__':
    sim = SimpleSimulation([Elevator(100, 5)], 1, [(Person(70, 1, 5), 1)])
    sim.run_simulation()
    # if "--visual" in sys.argv:
    # curses.wrapper(visualise)
    # else:
    #     simulate()
