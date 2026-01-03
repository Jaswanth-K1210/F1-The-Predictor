# F1-The-Predictor API Reference

This document tracks all classes, variables, and functions used in the project.

---

## Table of Contents

- [Python Modules](#python-modules)
  - [state/driver_state.py](#statedriver_statepy)
  - [state/race_state.py](#staterace_statepy)
- [C++ Modules](#c-modules) *(placeholder)*

---

## Python Modules

### state/driver_state.py

#### Class: `DriverState`

A dataclass representing the current state of a driver during a race.

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `driver_id` | `str` | *required* | Unique identifier for the driver |
| `position` | `int` | *required* | Current race position (1 = leader) |
| `gap_to_leader` | `float` | *required* | Time gap to the race leader (seconds) |
| `gap_to_ahead` | `float` | *required* | Time gap to the car ahead (seconds) |
| `tire_compound` | `str` | *required* | Current tire compound (e.g., "soft", "medium", "hard") |
| `tire_age` | `int` | *required* | Number of laps on current tires |
| `pit_stops` | `int` | *required* | Total number of pit stops made |
| `pace_rank` | `int` | *required* | Relative pace ranking among drivers |
| `fuel_estimate` | `float` | *required* | Estimated remaining fuel (kg or laps) |
| `dnf_risk` | `float` | *required* | Probability of DNF (0.0 - 1.0) |
| `strategy_state` | `str` | *required* | Current strategy phase (e.g., "out_lap", "push", "conserve") |
| `win_probability` | `float` | `0.0` | Calculated probability of winning (0.0 - 1.0) |

#### Functions

| Function | Parameters | Return Type | Description |
|----------|------------|-------------|-------------|
| `to_dict()` | *none* | `dict` | Converts the dataclass instance to a dictionary |

---

### state/race_state.py

#### Class: `RaceState`

Manages the overall state of a race, including all drivers and race conditions.

##### Instance Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `race_name` | `str` | *constructor* | Name of the race (e.g., "Monaco Grand Prix") |
| `total_laps` | `int` | *constructor* | Total number of laps in the race |
| `current_lap` | `int` | `0` | Current lap number |
| `track_condition` | `str` | `"dry"` | Track surface condition ("dry", "wet", "damp") |
| `safety_car` | `bool` | `False` | Whether safety car is currently deployed |
| `weather_confidence` | `float` | `1.0` | Confidence level in weather predictions (0.0 - 1.0) |
| `drivers` | `Dict[str, DriverState]` | `{}` | Dictionary mapping driver IDs to their state objects |

#### Functions

| Function | Parameters | Return Type | Description |
|----------|------------|-------------|-------------|
| `__init__` | `race_name: str`, `total_laps: int` | `None` | Constructor - initializes race state |
| `add_driver` | `driver: DriverState` | `None` | Adds a driver to the race |
| `get_driver` | `driver_id: str` | `DriverState` | Retrieves a driver's state by ID |
| `lap_completed` | *none* | `None` | Increments the current lap counter |
| `update_position` | `driver_id: str`, `position: int` | `None` | Updates a driver's position |
| `update_gap` | `driver_id: str`, `gap_to_leader: float`, `gap_to_ahead: float` | `None` | Updates a driver's gap times |
| `pit_stop` | `driver_id: str`, `new_compound: str` | `None` | Records a pit stop, resets tire age, updates compound |
| `deploy_safety_car` | *none* | `None` | Sets safety car status to active |
| `end_safety_car` | *none* | `None` | Sets safety car status to inactive |
| `validate` | *none* | `None` | Validates race state (checks lap count, duplicate positions) |
| `to_dict` | *none* | `dict` | Serializes entire race state to dictionary |

---

## C++ Modules

> **Note:** C++ modules are currently empty placeholders. Documentation will be added as code is implemented.

### Planned Structure

| Module | Path | Purpose |
|--------|------|---------|
| Monte Carlo Engine | `cpp/engines/monte_carlo/` | Race outcome simulations |
| Probability Engine | `cpp/engines/probability/` | Statistical probability calculations |
| Strategy Engine | `cpp/engines/strategy/` | Pit stop and tire strategy optimization |
| Python Bindings | `cpp/bindings/` | pybind11 interface for Python integration |
| Common Utilities | `cpp/common/` | Shared utilities and data structures |
| Models | `cpp/models/` | Data model definitions |

---

## Changelog

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-03 | - | Initial documentation created |

---

*Last updated: January 3, 2026*
