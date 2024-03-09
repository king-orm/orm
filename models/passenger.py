import random
from jethive.model import Model, unique
import faker


class Passenger(Model):
    c_first_name = str
    c_middle_name = str
    c_last_name = str
    c_gender_flag = bool
    c_passport_number = unique(str)
    
    @classmethod
    def seed(cls):
        fake = faker.Factory.create()
        
        return [
            {"first_name": fake.first_name(), "middle_name": fake.first_name(), "last_name": fake.last_name(), "gender_flag": cls.random_gender(), "passport_number": cls.random_passport_number()}
            for _
            in range(200)
        ]
        
    @classmethod
    def random_gender(cls) -> bool:
        return bool(random.getrandbits(1))
    
    @classmethod
    def random_passport_number(cls):
        return f"{str(random.randint(1000, 9999)).zfill(4)} {str(random.randint(100000, 999999)).zfill(6)}"
        
    @property
    def gender(self):
        return 'F' if self.gender_index else 'M'
    
    @gender.setter
    def gender(self, gender):
        if gender not in ['F', 'M']:
            raise ValueError(f"Gender must be one of 'F' or 'M' not '{gender}'")
        
        self.gender_flag = gender == 'F'
