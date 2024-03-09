import itertools
import random
from jethive.model import Model
from jethive.models.plane_type import PlaneType
from jethive.models.service_level import ServiceLevel


class PlaneServiceZone(Model):
    c_plane_type = PlaneType
    c_service_level = ServiceLevel
    c_seats_count = int
    
    @classmethod
    def seed(cls):
        plane_types = PlaneType.all()
        service_levels = ServiceLevel.all()
        
        return [
            {"plane_type_id": plane_type.id, "service_level_id": service_level.id, "seats_count": random.randint(4, 60)}
            for plane_type, service_level
            in itertools.product(plane_types, service_levels)
        ]