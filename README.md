# Valorant Sens Calculator

This repository contains a simple **Valorant sensitivity calculator** web service built with [FastAPI](https://fastapi.tiangolo.com/).  It exposes a single endpoint for computing a player's effective DPI (`eDPI`), distance (cm) required for a 360° rotation, and PSA (Perfect Sensitivity Approximation) recommendations.

The project is structured for maintainability and scalability, separating API routing, business logic, and data models.  It also includes input validation via Pydantic and is ready for containerised deployment.

## Features

- Calculate effective DPI (`eDPI`) and cm/360 from user-provided DPI and in-game sensitivity.
- Provide PSA low/high/average recommendations.
- Designed with a clean architecture: routers only orchestrate requests, services contain business logic, and schemas validate input/output.
- Ready for containerised deployment via Docker.

## Quickstart

1. **Install dependencies**:

   ```bash
   python -m pip install -r requirements.txt
   ```

2. **Run the application**:

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Test the endpoint** (e.g. using `curl`):

   ```bash
   curl -X POST http://localhost:8000/api/v1/calculator/sens \
     -H "Content-Type: application/json" \
     -d '{"dpi": 1600, "sensitivity": 0.125}'
   ```

   Expected response:

   ```json
   {
     "dpi": 1600,
     "sensitivity": 0.125,
     "edpi": 200.0,
     "cm360": 4.55,
     "psa_low": 0.1,
     "psa_average": 0.125,
     "psa_high": 0.15
   }
   ```

## Project Structure

```
valorant-sens-calculator/
├── app/                     # Python package containing all application code
│   ├── __init__.py
│   ├── main.py             # FastAPI application factory
│   ├── api/
│   │   └── v1/
│   │       ├── routes/
│   │       │   ├── calculator.py  # Sensitivity endpoint
│   │       │   └── health.py      # Health-check endpoint
│   │       └── router.py    # Aggregates versioned routes
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── calculator.py    # Pydantic models for request/response
│   ├── services/
│   │   ├── __init__.py
│   │   └── calculator_service.py  # Business logic for calculations
│   └── core/
│       ├── __init__.py
│       └── config.py        # Configuration and constants
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container build definition
└── README.md                # Project overview (this file)
```

## API

- **POST** `/api/v1/calculator/sens`

  **Body** (JSON):

  | Field         | Type    | Description                                |
  | ------------- | ------- | ------------------------------------------ |
  | `dpi`         | integer | Dots per inch of the mouse (100–20000)   |
  | `sensitivity` | float   | In-game sensitivity (>0 and ≤10)         |

  **Response** (JSON):

  | Field         | Type    | Description                                      |
  | ------------- | ------- | ------------------------------------------------ |
  | `dpi`         | integer | Echo of the input DPI                            |
  | `sensitivity` | float   | Echo of the input sensitivity                    |
  | `edpi`        | float   | Effective DPI (DPI × sensitivity)               |
  | `cm360`       | float   | Centimetres required for a 360° rotation         |
  | `psa_low`     | float   | 80% of the given sensitivity (lower bound)       |
  | `psa_average` | float   | Midpoint between `psa_low` and `psa_high`        |
  | `psa_high`    | float   | 120% of the given sensitivity (upper bound)      |

## Deployment

To build and run the application in a Docker container:

```bash
docker build -t valorant-sens-calculator .
docker run -p 8000:8000 valorant-sens-calculator
```

This will start the service accessible at `http://localhost:8000`.

---
*This project is provided as a reference implementation and can be extended with additional features such as authentication, user profiles, persistent storage of sensitivity records, or integration with other games.*
