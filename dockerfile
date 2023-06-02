# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the container
COPY scrape_smasaga.py .
COPY templates templates/

# Install dependencies if needed
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run the Python script when the container starts
CMD [ "python", "scrape_smasaga.py" ]
