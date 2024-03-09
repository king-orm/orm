from typing import List
from jethive.model import Model, unique


class Manufacturer(Model):
    c_name = unique(str)

    @classmethod
    def seed(cls) -> List[dict]:
        return [
            {"name": "Airbus"},
            {"name": "Boeing"},
            {"name": "Bombardier"},
            {"name": "Embraer"},
            {"name": "Gulfstream Aerospace"},
            {"name": "Cessna"},
            {"name": "Dassault Aviation"},
            {"name": "Saab AB"},
            {"name": "Sukhoi"},
            {"name": "Piper Aircraft"},
            {"name": "Diamond Aircraft"},
            {"name": "Beechcraft"},
            {"name": "Antonov"},
            {"name": "Kawasaki Heavy Industries"},
            {"name": "Pilatus Aircraft"},
            {"name": "Leonardo"},
            {"name": "Piaggio Aerospace"},
            {"name": "Aerospatiale"},
            {"name": "Northrop Grumman"},
            {"name": "Thales"},
            {"name": "Mitsubishi Heavy Industries"},
            {"name": "Cirrus Aircraft"},
            {"name": "Air Tractor"},
            {"name": "Hawker Beechcraft"},
            {"name": "Textron Aviation"},
            {"name": "Tupolev"},
            {"name": "Sikorsky Aircraft"},
            {"name": "Ilyushin"},
            {"name": "Kaman Aerospace"},
            {"name": "Raytheon Aircraft Company"},
            {"name": "Fairchild Republic"},
            {"name": "Hindustan Aeronautics Limited"},
            {"name": "AgustaWestland"},
            {"name": "Fokker"},
        ]