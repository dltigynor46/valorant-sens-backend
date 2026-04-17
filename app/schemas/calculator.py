from pydantic import BaseModel, Field, field_validator


class SensCalculationRequest(BaseModel):
    dpi: int = Field(..., ge=100, le=20000)
    sensitivity: float = Field(..., gt=0, le=10)

    # Additional validation can be added here if needed
    @field_validator("dpi")
    @classmethod
    def validate_dpi(cls, value: int) -> int:
        return value


class SensCalculationResponse(BaseModel):
    dpi: int
    sensitivity: float
    edpi: float
    cm360: float
    psa_low: float
    psa_average: float
    psa_high: float
