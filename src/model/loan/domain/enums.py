import enum

class VehicleType(str, enum.Enum):
    MOTOR = "motor"
    MOBIL = "mobil"

class VehicleCondition(str, enum.Enum):
    BARU = "baru"
    BEKAS = "bekas"

