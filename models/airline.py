from jethive.model import Model, unique


class Airline(Model):
    c_name = unique(str)
    c_code = unique(str)
    
    @classmethod
    def seed(cls):
        return [
            {"name": "Lufthansa", "code": "LH"},
            {"name": "Emirates", "code": "EK"},
            {"name": "Delta Air Lines", "code": "DL"},
            {"name": "American Airlines", "code": "AA"},
            {"name": "Air France", "code": "AF"},
            {"name": "British Airways", "code": "BA"},
            {"name": "Qatar Airways", "code": "QR"},
            {"name": "Cathay Pacific", "code": "CX"},
            {"name": "Singapore Airlines", "code": "SQ"},
            {"name": "Turkish Airlines", "code": "TK"},
            {"name": "KLM Royal Dutch Airlines", "code": "KL"},
            {"name": "Etihad Airways", "code": "EY"},
            {"name": "Air Canada", "code": "AC"},
            {"name": "Japan Airlines", "code": "JL"},
            {"name": "Qantas", "code": "QF"},
            {"name": "Swiss International Air Lines", "code": "LX"},
            {"name": "Southwest Airlines", "code": "WN"},
            {"name": "Aeroflot Russian Airlines", "code": "SU"},
            {"name": "China Southern Airlines", "code": "CZ"},
            {"name": "Air New Zealand", "code": "NZ"},
            {"name": "Ryanair", "code": "FR"},
            {"name": "Norwegian Air Shuttle", "code": "DY"},
            {"name": "Air India", "code": "AI"},
            {"name": "SAS Scandinavian Airlines", "code": "SK"},
            {"name": "Korean Air", "code": "KE"},
            {"name": "Vietnam Airlines", "code": "VN"},
            {"name": "Aeromexico", "code": "AM"},
            {"name": "Alitalia", "code": "AZ"},
            {"name": "LATAM Airlines", "code": "LA"},
            {"name": "Royal Air Maroc", "code": "AT"},
            {"name": "Air China", "code": "CA"},
            {"name": "EgyptAir", "code": "MS"},
            {"name": "Iberia", "code": "IB"},
            {"name": "Kenya Airways", "code": "KQ"},
            {"name": "Air Asia", "code": "AK"},
            {"name": "Finnair", "code": "AY"},
            {"name": "TAP Air Portugal", "code": "TP"},
            {"name": "Austrian Airlines", "code": "OS"},
            {"name": "Garuda Indonesia", "code": "GA"},
            {"name": "Philippine Airlines", "code": "PR"},
            {"name": "Copa Airlines", "code": "CM"},
            {"name": "EVA Air", "code": "BR"},
            {"name": "Air Mauritius", "code": "MK"},
            {"name": "Royal Jordanian", "code": "RJ"},
            {"name": "Air Baltic", "code": "BT"},
            {"name": "LOT Polish Airlines", "code": "LO"},
        ]