from dataclasses import dataclass


@dataclass
class AverageAgeCommand:  # TODO: make this generic
    should_round: bool
