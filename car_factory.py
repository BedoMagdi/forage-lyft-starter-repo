import imp
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.engine import Engine
from battery.battery import Battery
from car import Car
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_Service_date, current_mileage, last_Service_mileage):
        engine = CapuletEngine(current_mileage, last_Service_mileage)
        battery = SpindlerBattery(last_Service_date, current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(current_date, last_Service_date, current_mileage, last_Service_mileage):
        engine = WilloughbyEngine(current_mileage, last_Service_mileage)
        battery = SpindlerBattery(last_Service_date, current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_plaindrome(current_date, last_Service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_Service_date, current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date, last_Service_date, current_mileage, last_Service_mileage):
        engine = WilloughbyEngine(current_mileage, last_Service_mileage)
        battery = NubbinBattery(last_Service_date, current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date, last_Service_date, current_mileage, last_Service_mileage):
        engine = CapuletEngine(current_mileage, last_Service_mileage)
        battery = NubbinBattery(last_Service_date, current_date)
        car = Car(engine, battery)
        return car