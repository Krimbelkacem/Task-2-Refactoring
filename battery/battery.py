from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Battery(ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        if not isinstance(self.current_date, datetime) or not isinstance(self.last_service_date, datetime):
            raise ValueError("Dates should be of type datetime")

    @abstractmethod
    def service_interval(self):
        pass

    def needs_service(self):
        service_date = self.last_service_date + \
            timedelta(days=self.service_interval())
        return self.current_date >= service_date
