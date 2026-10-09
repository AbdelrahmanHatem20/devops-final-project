# DevOps Final Project

A Flask web application integrated with Redis to track visits.
The application is containerized using Docker and Docker Compose,
with CI/CD automation using GitHub Actions and deployed on Railway.

## Technologies Used

- Python Flask
- Redis
- Docker
- Docker Compose
- GitHub Actions CI/CD
- Railway Deployment
- Docker Hub

---

## Deployment

### GitHub Repository

https://github.com/AbdelrahmanHatem20/devops-final-project


### Railway Deployment

https://devops-final-project-production.up.railway.app


### Health Check

The application provides a health check endpoint:

https://devops-final-project-production.up.railway.app/health


### Docker Hub Image

https://hub.docker.com/r/bodycool25/devops-final-project


---

## Features

- Flask web application
- Redis visit counter
- Docker containerization
- Docker Compose orchestration
- GitHub Actions CI/CD pipeline
- Railway cloud deployment
- Health check endpoint


---

## Architecture

The project consists of two main services:

### Flask Web Service
- Handles HTTP requests.
- Displays the visit counter.
- Connects with Redis.


### Redis Service
- Stores the visit counter data.
- Provides persistence during application runtime.


Docker Compose is used to manage and connect both services.


---

## Run Locally

### Clone Repository

```bash
git clone https://github.com/AbdelrahmanHatem20/devops-final-project.git

cd devops-final-project

Build and Run
docker compose up --build

Application URL
http://localhost:5000

Health Check
http://localhost:5000/health
