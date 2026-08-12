"""Request and response schemas for sensitivity calculations."""

from pydantic import BaseModel, ConfigDict, Field, field_validator


class SensCalculationRequest(BaseModel):
    """Validated input for a Valorant sensitivity calculation."""

    model_config = ConfigDict(extra="forbid")

    dpi: int = Field(..., ge=100, le=20000, description="Mouse DPI value")
    sensitivity: float = Field(
        ...,
        gt=0,
        le=10,
        description="Valorant in-game sensitivity",
    )

    @field_validator("dpi")
    @classmethod
    def validate_dpi(cls, value: int) -> int:
        """Keep DPI values as whole numbers within the declared bounds."""

        return value


class SensCalculationResponse(BaseModel):
    """Calculated sensitivity metrics returned by the API."""

    dpi: int
    sensitivity: float
    edpi: float
    cm360: float
    trial_low: float
    trial_current: float
    trial_high: float
