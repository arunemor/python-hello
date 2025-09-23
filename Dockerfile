# Use official Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Expose Flask port
EXPOSE 5000

# Use Gunicorn for production
# 4 worker processes, bind to all interfaces
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
