"""
TODO:
    Lifts should have height variable that represents how far they are above
    the ground. It should be the main var and "floor" var will be calculated
    with it. Also make a settings.py file where global vars such as
    "ONE_FLOOR_HEIGHT" will be declared.
"""
from typing import Optional


class Person():
    """Class that represents a person"""

    weight: int
    current_floor: int
    floor_dest: int  # The number of the floor that the person wants to get to

    def __init__(self, weight: int, current_floor: int, floor_dest: int):
        self.weight = weight
        self.current_floor = current_floor
        self.floor_dest = floor_dest


class Elevator():
    """Class that represents an elevator"""

    max_capacity: int
    current_floor: int  # Actual floor number, not index
    speed: float = 1.0
    passangers: list[Person] = []
    max_floor: int  # Top floor
    min_floor: int = 1

    def __init__(self, max_capacity: int,
                 max_floor: int, min_floor: Optional[int] = None,
                 speed: Optional[float] = None):
        self.max_capacity = max_capacity
        self.current_floor = 1
        self.speed = 1.0  # m/s
        self.max_floor = max_floor
        if speed is not None:
            self.speed = speed

    def __str__(self):
        """String representation for console drawing"""
        return """TODO [elevator]
representation
bsn
newline"""
