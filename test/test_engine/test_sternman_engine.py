import unittest
import sys
import os

p = os.path.abspath('.')
sys.path.append(p)
from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):

    def test_battery_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

    def test_battery_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())


if __name__ == '__main__':
    unittest.main()