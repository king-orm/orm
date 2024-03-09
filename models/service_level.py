from jethive.model import Model, unique
from jethive.models.plane_type import PlaneType


class ServiceLevel(Model):
    c_name = unique(str)
    c_price_factor = float
    
    @classmethod
    def seed(cls):
        return [
            {"name": "Econom", "price_factor": 1.00},
            {"name": "Business", "price_factor": 2.50},
            {"name": "Elite", "price_factor": 5.50}
        ]