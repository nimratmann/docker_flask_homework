# Use the official Python 3.7 Alpine image as the base image
FROM python:3.7-alpine

# Set the working directory to /app in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 to the outside world, allowing external access to your application
EXPOSE 5000

# Define the default command to run when the container starts
CMD ["python", "app.py"]

#Documentation

# Run the following command to build the Docker image named "mann": docker build -t mann .
# To see the list of Docker images on your system, run: docker images
# To run the Docker container in detached mode and map port 5001 on the host to port 5000 in the container, run: docker run -d -p 5001:5000 mann
# To see information about the running containers, including the container ID, run: docker ps
# If you need to stop the running container, use the container ID in the following command: docker stop <container_id>
# If you want to delete all Docker images, you can use the following command: docker system prune -a -f