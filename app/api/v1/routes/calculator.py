from fastapi import APIRouter

from app.schemas.calculator import SensCalculationRequest, SensCalculationResponse
from app.services.calculator_service import CalculatorService

router = APIRouter()

@router.post("/sens", response_model=SensCalculationResponse)
async def calculate_sens(payload: SensCalculationRequest) -> SensCalculationResponse:
    """Calculate eDPI, cm/360, and PSA recommendations based on user input.

    Args:
        payload (SensCalculationRequest): The DPI and sensitivity values provided by the user.

    Returns:
        SensCalculationResponse: The calculated results including eDPI, cm/360, PSA low, average, and high values.
    """
    result = CalculatorService.calculate(dpi=payload.dpi, sensitivity=payload.sensitivity)
    return SensCalculationResponse(
        dpi=result.dpi,
        sensitivity=result.sensitivity,
        edpi=result.edpi,
        cm360=result.cm360,
        psa_low=result.psa_low,
        psa_average=result.psa_average,
        psa_high=result.psa_high,
    )
