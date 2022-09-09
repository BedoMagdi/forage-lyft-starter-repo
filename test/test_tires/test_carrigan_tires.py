import unittest
import sys
import os

p = os.path.abspath('.')
sys.path.append(p)

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):

    def test_tires_should_not_be_serviced(self):
        tires_arr = [0.5, 0.7, 0.4, 0.5]
        tires = CarriganTires(tires_arr)
        self.assertFalse(tires.needs_service())

    def test_tires_should_be_serviced(self):
        tires_arr = [0.5, 0.7, 0.4, 0.9]
        tires = CarriganTires(tires_arr)
        self.assertTrue(tires.needs_service())


if __name__ == '__main__':
    unittest.main()