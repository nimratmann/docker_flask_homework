# docker_flask_homework
Gaining hands-on experience in Dockerizing Flask applications, first individually and then using Docker Compose for managing multiple application

# 1. Dockerizing a Single Flask Application
### Setting up the application 
1. Created a Flask application in the app.py file
2. Developed a requirements.txt file listing all necessary Python packages for the Flask application
3. Established a templates folder to organize HTML templates for the Flask application.
- Created a base HTML template (base.html) to serve as the foundation for other views, providing a consistent layout for the application.
- Created an about.html file within the templates folder to represent a specific view within the Flask application.

### Dockerfile Configuration
1. Developed a Dockerfile with the following configuration to containerize the Flask application:
```
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
```

### Building and Running the Docker Container
- Run the following command to build the Docker image named "mann": docker build -t mann .
- To see the list of Docker images on your system, run: docker images
- To run the Docker container in detached mode and map port 5001 on the host to port 5000 in the container, run: docker run -d -p 5001:5000 mann
- To see information about the running containers, including the container ID, run: docker ps
- If you need to stop the running container, use the container ID in the following command: docker stop <container_id>
- If you want to delete all Docker images, you can use the following command: docker system prune -a -f


# 2. Multi-Container Setup with Docker Compose
### Setting up the Application and Folder Structure 
Two separate Flask applications, located in folders flask1 and flask2, were Dockerized along with their respective templates, app.py, requirements.txt, and Dockerfile.
- Flask1
  
  app.py: Developed the main app.py Flask application script for the first container

  requirements.txt: Defined the Python dependencies for the Flask application in flask1

  templates: Created a templates folder containing an index.html file for the Flask application in flask1

  
- Flask2
  
  app.py: Developed the main app.py Flask application script for the first container

  requirements.txt: Defined the Python dependencies for the Flask application in flask2

  templates: Created a templates folder containing an index.html file for the Flask application in flask2

### Dockerfile Configuration
There is a Dockerfile located in each of the two folders with the following code:
```
FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

### Dockerizing with Docker Compose
Created a docker-compose.yml file in the root directory of my Part2 folder.
Define a service for your Flask application:
```
version: '3'           # Specifies the version of the Docker Compose file

services:              # Defines services that constitute the application (flask_app_1, flask_app_2)
  
  flask_app_1:         # Service name for the first Flask application
    build: ./flask1    # Specifies the location of the Dockerfile for building the Docker image
    ports:             # Maps the port on the host to the port on the container
      - "5001:5000"
    volumes:           # Maps the directory of the application in the container
      - ./flask1:/app

  flask_app_2:         # Service name for the second Flask application
    build: ./flask2    # Specifies the location of the Dockerfile for building the Docker image
    ports:             # Maps the port on the host to the port on the container
      - "5002:5000"
    volumes:           # Maps the directory of the application in the container
      - ./flask2:/app
```

### Docker Compose Commands
To build and run the multi-container setup, use the following commands:
```
# Navigate to the directory containing docker-compose.yaml
cd <path-to-directory>

# Build the Docker images and start the containers
docker-compose up -d
```

To manage containers, use the following commands:
```
# View running containers
docker ps

# Stop the running containers
docker-compose down
```



  

