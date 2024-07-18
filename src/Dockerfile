# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
# This file should list all the dependencies needed for the project
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose the port that the Flask app will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]

# Instructions for using this Dockerfile:
# 1. Build the Docker image using the following command:
#    docker build -t blockbusters-app .
# 2. Run the Docker container using the following command:
#    docker run -p 5000:5000 blockbusters-app
# 3. Open a web browser and navigate to http://localhost:5000/ to access the app
# 4. Tag the Docker image for GitHub Container Registry using the following command:
#    docker tag blockbusters-app:latest ghcr.io/djsaunders1997/blockbusters-app:latest
# 5. Push the Docker image to GitHub Container Registry using the following command:
#    docker push ghcr.io/djsaunders1997/blockbusters-app:latest