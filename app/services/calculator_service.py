"""Business logic for Valorant sensitivity calculations."""

from dataclasses import dataclass

from app.core.config import INCH_TO_CM, VALORANT_YAW


@dataclass(frozen=True, slots=True)
class CalculationResult:
    """A calculated set of display-ready sensitivity metrics."""

    dpi: int
    sensitivity: float
    edpi: float
    cm360: float
    trial_low: float
    trial_current: float
    trial_high: float


class CalculatorService:
    """Calculate comparable Valorant sensitivity metrics."""

    @staticmethod
    def calculate(dpi: int, sensitivity: float) -> CalculationResult:
        """Calculate eDPI, approximate cm/360, and a ±20% trial range."""

        edpi = dpi * sensitivity
        cm360 = (360.0 / (edpi * VALORANT_YAW)) * INCH_TO_CM

        return CalculationResult(
            dpi=dpi,
            sensitivity=round(sensitivity, 6),
            edpi=round(edpi, 2),
            cm360=round(cm360, 2),
            trial_low=round(sensitivity * 0.8, 6),
            trial_current=round(sensitivity, 6),
            trial_high=round(sensitivity * 1.2, 6),
        )
