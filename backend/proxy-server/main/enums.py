from enum import Enum, unique, auto
from typing import List


@unique
class BaseEnum(str, Enum):
    @staticmethod
    def _generate_next_value_(name: str, *_):
        """
        Automatically generate values for enum.
        Enum values are lower-cased enum member names.
        """
        return name.lower()

    @classmethod
    def get_values(cls) -> List[str]:
        # noinspection PyUnresolvedReferences
        return [m.value for m in cls]

    def __repr__(self):
        return self.value


class SensorDataCategory(BaseEnum):
    ROOM_TEMPERATURE = auto()
    LIGHT = auto()
    NOISE = auto()
    HUMIDITY = auto()
    AIR_QUALITY = auto()


class SensorType(BaseEnum):
    ROOM_TEMPERATURE = auto()
    LIGHT = auto()
    NOISE = auto()
    HUMIDITY = auto()
    AIR_QUALITY = auto()


class SystemHardwareDataCategory(BaseEnum):
    CPU_VOLTAGE = auto()
    CPU_PERCENTAGE = auto()
    CPU_TEMPERATURE = auto()
    GPU_PERCENTAGE = auto()
    GPU_TEMPERATURE = auto()
    MEMORY = auto()
    DISK = auto()
    NETWORK = auto()
    DEVICE_TEMPERATURE = auto()


class SystemHardwareType(BaseEnum):
    CPU = auto()
    GPU = auto()
    PERSONAL_COMPUTER = auto()
    MEMORY = auto()
    DISK = auto()


class CollectedDataType(BaseEnum):
    BOOLEAN = auto()
    FLOAT = auto()


class DeviceType(BaseEnum):
    SENSOR = auto()
    SYSTEM_HARDWARE = auto()


class DeviceStatus(BaseEnum):
    ONLINE = auto()
    OFFLINE = auto()
    INACTIVE = auto()  # used when the sensor is just plugged in but not yet activated


class TimeRange(BaseEnum):
    LAST_HOUR = auto()
    LAST_DAY = auto()
    LAST_7_DAYS = auto()
    LAST_30_DAYS = auto()
    ALL = auto()


class AlertStatus(BaseEnum):
    RESOLVED = auto()
    UNRESOLVED = auto()


class ActivationCondition(BaseEnum):
    GREATER_THAN = auto()
    LESS_THAN = auto()
