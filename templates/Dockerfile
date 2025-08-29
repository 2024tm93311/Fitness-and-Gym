# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY app.py .
COPY test_app.py .

# Expose the app port
EXPOSE 5000

# Default: run the Flask app
CMD ["python", "app.py"]
