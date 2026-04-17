from dataclasses import dataclass
from app.core.config import VALORANT_YAW, INCH_TO_CM


@dataclass(slots=True)
class CalculationResult:
    dpi: int
    sensitivity: float
    edpi: float
    cm360: float
    psa_low: float
    psa_average: float
    psa_high: float


class CalculatorService:
    @staticmethod
    def calculate(dpi: int, sensitivity: float) -> CalculationResult:
        """Calculate eDPI, cm/360, and PSA values."""
        edpi = dpi * sensitivity

        # cm/360 calculation: convert 360 degrees rotation to centimeters
        cm360 = (360.0 / (edpi * VALORANT_YAW)) * INCH_TO_CM

        psa_low = sensitivity * 0.8
        psa_high = sensitivity * 1.2
        psa_average = (psa_low + psa_high) / 2.0

        return CalculationResult(
            dpi=dpi,
            sensitivity=round(sensitivity, 6),
            edpi=round(edpi, 2),
            cm360=round(cm360, 2),
            psa_low=round(psa_low, 6),
            psa_average=round(psa_average, 6),
            psa_high=round(psa_high, 6),
        )
