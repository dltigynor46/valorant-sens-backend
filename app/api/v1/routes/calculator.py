"""Sensitivity calculation endpoint."""

from fastapi import APIRouter

from app.schemas.calculator import SensCalculationRequest, SensCalculationResponse
from app.services.calculator_service import CalculatorService

router = APIRouter()


@router.post(
    "/sens",
    response_model=SensCalculationResponse,
    summary="Calculate Valorant sensitivity metrics",
)
async def calculate_sens(payload: SensCalculationRequest) -> SensCalculationResponse:
    """Calculate eDPI, approximate cm/360, and a ±20% trial range."""

    result = CalculatorService.calculate(dpi=payload.dpi, sensitivity=payload.sensitivity)
    return SensCalculationResponse(
        dpi=result.dpi,
        sensitivity=result.sensitivity,
        edpi=result.edpi,
        cm360=result.cm360,
        trial_low=result.trial_low,
        trial_current=result.trial_current,
        trial_high=result.trial_high,
    )
