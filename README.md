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
