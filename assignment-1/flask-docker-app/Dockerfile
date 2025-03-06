# Build dependencies in a full Python image
FROM python:3.9-slim AS builder

# Set the working folder to /app inside the container
WORKDIR /app

# Copy the requirements.txt file from my local machine to the container
COPY requirements.txt .

# Install all the packages listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Use a lightweight runtime environment, smaller Python image
FROM python:3.9-alpine

# Set the working folder to /app inside the container
WORKDIR /app

# Copy the installed Python packages from the builder image to this smaller image
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy my app.py file to the container
COPY app.py .

# When the container starts, it will run my app.py file using Python
CMD ["python", "app.py"]
