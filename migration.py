from models.manufacturer import Manufacturer
from models.plane_type import PlaneType
from models.plane import Plane
from models.airline import Airline
from models.country import Country
from models.city import City
from models.airport import Airport
from models.regular_flight import RegularFlight
from models.scheduled_flight import ScheduledFlight
from models.scheduled_flight_service_zone import ScheduledFlightServiceZone
from models.passenger import Passenger
from models.ticket import Ticket
from models.service_level import ServiceLevel
from models.plane_service_zone import PlaneServiceZone


models = [
    Manufacturer,
    PlaneType,
    Plane,
    Airline,
    Country,
    City,
    Airport,
    RegularFlight,
    ScheduledFlight,
    ScheduledFlightServiceZone,
    Passenger,
    Ticket,
    ServiceLevel,
    PlaneServiceZone
]


def up():
    for model in models:
        print(f'🛠️\tCreating a table for {model.table_name}...')
        model.up()

    print('✅\tMigration is complete', end='\n\n')


def down():
    for model in reversed(models):
        print(f'🗑️\tDeleting a table with {model.table_name}...')
        model.down()

    print('✅\tRollback is complete', end='\n\n')


def reset():
    down()
    up()


def playground(function):
    def playground_function_wrapper(*args, **kwargs):
        reset()
        function(*args, **kwargs)
        down()

    return playground_function_wrapper
