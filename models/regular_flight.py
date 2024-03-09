from random import shuffle, randint
from jethive.model import Model, column, time, unique
from jethive.models.airline import Airline
from jethive.models.plane import Plane 
from jethive.models.airport import Airport


code_length = 4


class RegularFlight(Model):
    c_code = str
    c_airline = Airline
    c_plane = Plane
    c_departure_airport = column(Airport, column_name='departure_airport_id')
    c_destination_airport = column(Airport, column_name='destination_airport_id')
    c_departure_weekday = int
    c_departure_time_utc = time
    c_arrival_weekday = int
    c_arrival_time_utc = time
    c_price_dollars = int
    
    @classmethod
    def create_code(cls):
        return str(randint(0, 10 ** code_length - 1)).zfill(code_length)
    
    @classmethod
    def seed(cls):
        airports = Airport.all()
        airlines = Airline.all()
        planes = Plane.all()
        departure_airports = airports.copy()
        destination_airports = airports.copy()
        
        shuffle(airlines)
        shuffle(planes)
        shuffle(departure_airports)
        shuffle(destination_airports)
        
        return [
            {
                'code': cls.create_code(),
                'airline_id': airline.id,
                'plane_id': plane.id,
                'departure_airport_id': departure_airport.id,
                'destination_airport_id': destination_airport.id,
                'departure_weekday': 1,
                'departure_time_utc': '18:00',
                'arrival_weekday': 2,
                'arrival_time_utc': '02:00',
                'price_dollars': randint(0, 500) * 50 
            }
            for airline, departure_airport, destination_airport, plane
            in zip(airlines, departure_airports, destination_airports, planes)
            if departure_airport.code != destination_airport.code
        ]
        
        
        
        