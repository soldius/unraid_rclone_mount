import unittest
import re
from wgups.schedule import schedule_delivery


def strip_color_codes(string: str) -> str:
    return re.sub(r'\[\d+?m', '', string)


class TestSchedule(unittest.TestCase):
    def test_schedule(self):
        packages, trucks = schedule_delivery()
        trucks.sort(key=lambda t: t.number)
        truck1, truck2 = trucks
        self.assertEqual(round(truck1.miles_traveled, 1), 74.2)
        self.assertEqual(round(truck2.miles_traveled, 1), 72.9)

        for time in [n * 60 for n in range(8, 13)]:
            with open(f'test/packages/{time}.txt', 'r') as f:
                for (index, line) in enumerate(f):
                    self.assertEqual(strip_color_codes(
                        packages[index].info(time)), line.strip())
