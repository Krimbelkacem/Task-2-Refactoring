from .battery import Battery
from datetime import timedelta


class NubbinBattery(Battery):
    def service_interval(self):
        return 4 * 365  # 4 years
