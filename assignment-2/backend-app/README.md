# docker-assignment-2

## Objective
This project demonstrates the use of Docker Compose to manage a multi-service backend application. As a backend developer, the application is integrated with a PostgreSQL database for persistent storage.

## Project Structure
```
![3](https://github.com/user-attachments/assets/b93d4ccb-f567-4dd4-bc98-02b7a2eae43a)
```

## Services Used
- **Application Service:** Runs the backend application.
- **PostgreSQL Database Service:** Provides persistent data storage.

## Features
- Uses Docker Compose to define and manage services.
- Ensures the app service starts only after the database service is ready.
- Uses environment variables from `.env` files instead of hardcoding values.
- Provides data persistence for the database service to prevent data loss on container restart.
- Supports redeployment of the application container without affecting the database.
- Allows stopping and restarting the database container while preserving stored data.

## Setup Instructions

### 1. Clone the Repository
```
git clone <repository-url>
cd <project-folder>
```

### 2. Configure Environment Variables
Create `.env` files for each service inside the `env_files/` directory. Example structure:

Ensure that sensitive credentials (e.g., database passwords) are stored in these `.env` files and not hardcoded in the code or compose file.

### 3. Build and Start the Services
```
docker-compose up --build
```
This command will build and run all services defined in the `docker-compose.yml` file.

### 4. Verify Application Functionality
- Open a browser and access the backend application.
- Verify database connectivity using tools like `pgAdmin` or `psql`.

### 5. Redeploy the Application Container
If you make code changes, redeploy only the application container:
```
docker-compose up -d --no-deps --build app
```
This ensures that the database remains unaffected.

### 6. Stop and Remove the Database Container
To test persistence, stop and remove the database container without deleting data:
```
docker-compose stop database
```
Restart the database and ensure old data loads automatically:
```
docker-compose up -d database
```

### 7. Stopping All Services
To stop all running containers:
```
docker-compose down
```

## Submission Requirements
- A public GitHub repository with all project files.
- A `screenshots/` folder containing step-wise screenshots.
- A detailed `README.md` file (this file) for documentation.

---


