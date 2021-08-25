"""
TODO:
    Lifts should have height variable that represents how far they are above
    the ground. It should be the main var and "floor" var will be calculated
    with it. Also make a settings.py file where global vars such as
    "ONE_FLOOR_HEIGHT" will be declared.
"""
from dataclasses import dataclass, field


@dataclass
class Person():
    """Class that represents a person"""

    weight: int
    start_floor: int
    floor_dest: int  # The number of the floor that the person wants to get to


@dataclass
class Elevator():
    """Class that represents an elevator"""

    max_capacity: int
    max_floor: int  # Top floor
    min_floor: int = 1
    current_floor: int = 1  # Actual floor number, not index
    speed: float = 1.0
    passangers: list[Person] = field(default_factory=list)

    def __str__(self) -> str:
        """String representation for console drawing"""
        return """TODO [elevator]
representation
bsn
newline"""
