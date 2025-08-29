# ACEest Fitness and Gym - DevOps Project

## Overview

This project demonstrates a complete DevOps workflow for a basic fitness/gym management system using Flask, Docker, Pytest, and GitHub Actions.

## Features

- Flask REST API with endpoints for viewing and adding gym members.
- Unit tests for all endpoints using Pytest.
- Dockerfile for containerization.
- Automated CI/CD pipeline using GitHub Actions.

## Setup & Local Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/aceest-fitness.git
   cd aceest-fitness
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**
   ```bash
   python app.py
   ```
   The app runs on [http://localhost:5000](http://localhost:5000).

## Running Tests

- Locally:
  ```bash
  pytest test_app.py
  ```

## Docker Usage

- **Build the Docker image**
  ```bash
  docker build -t aceest-fitness .
  ```

- **Run the container**
  ```bash
  docker run -p 5000:5000 aceest-fitness
  ```

- **Run tests inside Docker**
  ```bash
  docker run --rm aceest-fitness pytest test_app.py
  ```

## GitHub Actions Pipeline

- On every push, the pipeline will:
  1. Checkout code
  2. Set up Python and dependencies
  3. Run Pytest unit tests
  4. Build Docker image
  5. Run tests inside Docker

You can view the workflow and its status under the **Actions** tab in your GitHub repository.

---

**Make sure your repository is public and contains all files above for submission.**
