# Use the official Python 3.11 image as the base
FROM python:3.11-slim

# Set environment variables to avoid prompts during package installation
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the entire project into the working directory
COPY . /app/

# Expose the default Django port
EXPOSE 8000

# Run the application using Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
