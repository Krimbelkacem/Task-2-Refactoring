from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from datetime import datetime


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        # Validate parameters
        if not all(isinstance(arg, datetime) for arg in [current_date, last_service_date]):
            raise ValueError("Dates should be of type datetime")

        engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        # Validate parameters
        if not all(isinstance(arg, datetime) for arg in [current_date, last_service_date]):
            raise ValueError("Dates should be of type datetime")

        engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        # Validate parameters
        if not all(isinstance(arg, datetime) for arg in [current_date, last_service_date]):
            raise ValueError("Dates should be of type datetime")

        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        # Validate parameters
        if not all(isinstance(arg, datetime) for arg in [current_date, last_service_date]):
            raise ValueError("Dates should be of type datetime")

        engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        # Validate parameters
        if not all(isinstance(arg, datetime) for arg in [current_date, last_service_date]):
            raise ValueError("Dates should be of type datetime")

        engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
