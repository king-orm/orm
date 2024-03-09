from jethive.model import Model
from jethive.models.scheduled_flight import ScheduledFlight
from jethive.models.service_level import ServiceLevel


class ScheduledFlightServiceZone(Model):
    c_scheduled_flight = ScheduledFlight
    c_service_level = ServiceLevel
    c_seats_count = int
    
    @classmethod
    def seed(cls):
        return [
            # Fills automatically
        ]