from typing import Dict
from driver_state import DriverState


class RaceState:
    def __init__(self, race_name: str, total_laps: int):
        self.race_name = race_name
        self.total_laps = total_laps
        self.current_lap = 0

        self.track_condition = "dry"
        self.safety_car = False
        self.weather_confidence = 1.0

        self.drivers: Dict[str, DriverState] = {}


    def add_driver(self, driver: DriverState):
        self.drivers[driver.driver_id] = driver

    def get_driver(self, driver_id: str) -> DriverState:
        return self.drivers[driver_id]

    def lap_completed(self):
        self.current_lap += 1

    def update_position(self, driver_id: str, position: int):
        self.drivers[driver_id].position = position

    def update_gap(self, driver_id: str, gap_to_leader: float, gap_to_ahead: float):
        d = self.drivers[driver_id]
        d.gap_to_leader = gap_to_leader
        d.gap_to_ahead = gap_to_ahead

    def pit_stop(self, driver_id: str, new_compound: str):
        d = self.drivers[driver_id]
        d.pit_stops += 1
        d.tire_compound = new_compound
        d.tire_age = 0
        d.strategy_state = "out_lap"

    def deploy_safety_car(self):
        self.safety_car = True

    def end_safety_car(self):
        self.safety_car = False


    def validate(self):
        if self.current_lap > self.total_laps:
            raise ValueError("Lap count exceeds race length")

        positions = [d.position for d in self.drivers.values()]
        if len(positions) != len(set(positions)):
            raise ValueError("Duplicate positions detected")

    def to_dict(self) -> dict:
        return {
            "race_name": self.race_name,
            "total_laps": self.total_laps,
            "current_lap": self.current_lap,
            "track_condition": self.track_condition,
            "safety_car": self.safety_car,
            "weather_confidence": self.weather_confidence,
            "drivers": {
                k: v.to_dict() for k, v in self.drivers.items()
            }
        }
