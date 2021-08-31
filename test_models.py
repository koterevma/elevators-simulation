import unittest
from models import Elevator, Person


class ModelsTest(unittest.TestCase):

    def test_can_fit(self):

        self.elevator = Elevator(10, 10)
        self.elevator.passangers.append(Person(10, 1, 10))
        self.assertFalse(self.elevator.can_fit(Person(1, 1, 1)))

        self.elevator = Elevator(10, 10)
        self.elevator.passangers.append(Person(9, 1, 10))
        self.assertTrue(self.elevator.can_fit(Person(1, 1, 1)))

        self.elevator = Elevator(30, 10)
        self.elevator.passangers.append(Person(10, 1, 10))
        self.elevator.passangers.append(Person(20, 1, 10))
        self.assertFalse(self.elevator.can_fit(Person(1, 1, 1)))

        self.elevator = Elevator(30, 10)
        self.elevator.passangers.append(Person(10, 1, 10))
        self.elevator.passangers.append(Person(19, 1, 10))
        self.assertTrue(self.elevator.can_fit(Person(1, 1, 1)))


if __name__ == '__main__':
    unittest.main()
