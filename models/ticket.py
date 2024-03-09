from jethive.model import Model
from jethive.models.passenger import Passenger
from jethive.models.scheduled_flight_service_zone import ScheduledFlightServiceZone


class Ticket(Model):
    c_passenger = Passenger
    c_service_zone = ScheduledFlightServiceZone
    c_price_dollars = int
    
    @classmethod
    def seed(cls):
        return [
            
        ]