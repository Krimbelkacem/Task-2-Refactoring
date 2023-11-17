from .battery import Battery
from datetime import timedelta


class SpindlerBattery(Battery):
    def service_interval(self):
        return 2 * 365  # 2 years
