# ACEest Fitness & Gym – Flask API (DevOps Assignment)

A minimal Flask application demonstrating core DevOps workflows: Git, Pytest, Docker, and GitHub Actions CI.

## Features
- **API endpoints**
  - `GET /` – service info
  - `GET /health` – health probe
  - `POST /bmi` – BMI calculator: `{ "weight_kg": 70, "height_cm": 175 }`
  - `GET /members` – list members
  - `POST /members` – add member: `{ "name": "Riya", "age": 28 }`

- **Tests** with `pytest` for endpoints and BMI logic
- **Docker** multi-stage build for runtime and test
- **GitHub Actions** pipeline:
  1. Install deps & run `pytest` (fast local check)
  2. Build Docker images (`runtime` & `test`)
  3. Run tests **inside** the Docker image

---

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
# App will be at http://127.0.0.1:8000
```

### Run tests locally
```bash
pytest -q
```

## Docker

Build and run runtime image:
```bash
docker build --target runtime -t aceest/fitness-api:runtime .
docker run --rm -p 8000:8000 aceest/fitness-api:runtime
```

Run tests **in Docker**:
```bash
docker build --target test -t aceest/fitness-api:test .
docker run --rm aceest/fitness-api:test
```

## Git & GitHub

```bash
git init
git add .
git commit -m "Initial commit: Flask app, tests, Docker, CI"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

Once pushed, GitHub Actions will trigger automatically. Check **Actions** tab for green checks.

---

## Notes
- Default port is **8000**.
- The app uses in-memory storage for demo purposes.
- For production, attach a real database and add authentication.
