from dataclasses import dataclass

@dataclass
class RoomStatusHistory:
    room_name: str
    population: int
    timestamp: int
