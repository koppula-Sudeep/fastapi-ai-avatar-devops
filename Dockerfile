
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from creating bytecode files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Python dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application
COPY app/ ./app/

# Expose the FastAPI port
EXPOSE 8000

# Start the application and allow external container access
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
