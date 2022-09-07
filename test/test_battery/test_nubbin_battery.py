import unittest
from datetime import datetime
import sys
import os

p = os.path.abspath('.')
sys.path.append(p)
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())


if __name__ == '__main__':
    unittest.main()