# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Create the log directory
RUN mkdir -p /app/flaskapp

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Define the command to run the application with Waitress
CMD ["waitress-serve", "--host=0.0.0.0", "--port=65190", "wsgi:app"]