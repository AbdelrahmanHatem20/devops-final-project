## Deployment

### GitHub Repository
https://github.com/AbdelrahmanHatem20/devops-final-project

### Railway Deployment
https://devops-final-project-production.up.railway.app

### Health Check
https://devops-final-project-production.up.railway.app/health

### Docker Hub Image
https://hub.docker.com/r/bodycool25/devops-final-project
## Run Locally

Clone the repository:

```bash
git clone https://github.com/AbdelrahmanHatem20/devops-final-project.git
cd devops-final-project
```

Build and run:

```bash
docker compose up --build
```

The application will run on:

```text
http://localhost:5000
```

Health check:

```text
http://localhost:5000/health
```
