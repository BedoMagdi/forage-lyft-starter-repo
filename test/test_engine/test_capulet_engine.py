import unittest
import sys
import os

p = os.path.abspath('.')
sys.path.append(p)
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):

    def test_battery_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_battery_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())


if __name__ == '__main__':
    unittest.main()