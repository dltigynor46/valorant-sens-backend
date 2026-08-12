# Valorant Sens Calculator API

A small FastAPI service for calculating Valorant sensitivity metrics. The static frontend can run without this API; use the API when a server-side integration is genuinely needed.

## Features

- Calculates **eDPI** (`DPI × sensitivity`).
- Calculates approximate **cm/360**.
- Returns a clearly labelled ±20% **trial range** around the supplied sensitivity.
- Validates DPI from 100 to 20,000 and sensitivity from greater than 0 to 10.
- Includes a health endpoint and automated tests.

## Calculation method

```text
eDPI = DPI × sensitivity
cm/360 = (360 / (eDPI × 0.07)) × 2.54
```

For `1600 DPI` and `0.125` sensitivity, the expected result is:

```json
{
  "dpi": 1600,
  "sensitivity": 0.125,
  "edpi": 200.0,
  "cm360": 65.31,
  "trial_low": 0.1,
  "trial_current": 0.125,
  "trial_high": 0.15
}
```

The trial range is an exploration aid, not a personalised or scientifically validated “perfect sensitivity” recommendation.

## Run locally

```bash
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The interactive API documentation is available at `http://localhost:8000/docs`.

## API

### Health check

```text
GET /api/v1/health
```

### Calculate sensitivity metrics

```text
POST /api/v1/calculator/sens
Content-Type: application/json
```

```json
{
  "dpi": 1600,
  "sensitivity": 0.125
}
```

## CORS configuration

Set `ALLOWED_ORIGINS` to a comma-separated list of browser origins when deploying, for example:

```bash
ALLOWED_ORIGINS=https://your-account.github.io,https://app.example.com
```

The default is limited to local development origins. Credentials are disabled because this API does not currently use cookie or token-based authentication.

## Test

```bash
pytest -q
```

The test suite verifies the calculation values, health endpoint, valid request, and invalid request handling.

## Container

```bash
docker build -t valorant-sens-calculator-api .
docker run -p 8000:8000 \
  -e ALLOWED_ORIGINS=https://your-account.github.io \
  valorant-sens-calculator-api
```
