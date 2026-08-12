from fastapi.testclient import TestClient

from app.main import create_app
from app.services.calculator_service import CalculatorService


client = TestClient(create_app())


def test_calculator_service_returns_expected_metrics() -> None:
    result = CalculatorService.calculate(dpi=1600, sensitivity=0.125)

    assert result.edpi == 200.0
    assert result.cm360 == 65.31
    assert result.trial_low == 0.1
    assert result.trial_current == 0.125
    assert result.trial_high == 0.15


def test_health_endpoint_returns_ok() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_calculator_endpoint_returns_expected_metrics() -> None:
    response = client.post(
        "/api/v1/calculator/sens",
        json={"dpi": 1600, "sensitivity": 0.125},
    )

    assert response.status_code == 200
    assert response.json() == {
        "dpi": 1600,
        "sensitivity": 0.125,
        "edpi": 200.0,
        "cm360": 65.31,
        "trial_low": 0.1,
        "trial_current": 0.125,
        "trial_high": 0.15,
    }


def test_calculator_endpoint_rejects_invalid_input() -> None:
    response = client.post(
        "/api/v1/calculator/sens",
        json={"dpi": 0, "sensitivity": -0.1},
    )

    assert response.status_code == 422
