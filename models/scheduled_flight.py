from time import sleep
from threading import Thread 
from datetime import datetime
from jethive.model import Model
from jethive.models.regular_flight import RegularFlight
import schedule


class ScheduledFlight(Model):
    c_regular_flight = RegularFlight
    c_departure_date = datetime
    c_arrival_date = datetime
    c_price_dollars = int
    
    @classmethod
    def seed(cls):
        return [
            # Fills automatically
        ]
        
    @classmethod
    def after_seeding(cls):
        scheduler_thread = Thread(target=cls.run_scheduler)
        scheduler_thread.start()
        
    @classmethod
    def run_scheduler(cls):
        schedule.every().monday.at("00:00:00").do(cls.add_scheduled_flights_of_the_week)
        
        while True:
            schedule.run_pending()
            sleep(1)
        
    @classmethod
    def add_scheduled_flights_of_the_week(cls):
        # TODO
        pass