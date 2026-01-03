from dataclasses import dataclass, asdict

@dataclass
class DriverState:
    driver_id: str
    position: int
    gap_to_leader: float
    gap_to_ahead: float
    tire_compound: str
    tire_age: int
    pit_stops: int
    pace_rank: int
    fuel_estimate: float
    dnf_risk: float
    strategy_state: str
    win_probability: float = 0.0

    def to_dict(self) -> dict:
        return asdict(self)
