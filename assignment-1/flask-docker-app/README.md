# docker-assignment-1
# Dockerized Web Application

## Objective
This project demonstrates the creation of a simple web application, containerization using Docker, and deploying it on a local environment with Nginx.

## Steps to Complete the Assignment

### 1. Create a Web Application
Developed a simple web application using Python (Flask) to serve as the backend. The application is structured as follows:

```
/app
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
```
![1](https://github.com/user-attachments/assets/7516d3ed-98d7-493d-8201-fba136cd53e2)
![2](https://github.com/user-attachments/assets/d4ab3287-1cd6-4b34-8656-1e00522f3889)

### 2. Write a Dockerfile (Multi-Stage Build)

```dockerfile
# Stage 1: Build dependencies in a full Python image
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Use a lightweight runtime environment
FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY app.py .

# Run the application
CMD ["python", "app.py"]
```

### 3. Build the Docker Image
To build the image with a minimized size:
![3](https://github.com/user-attachments/assets/ffd97127-fd83-4a00-9e99-d3e1276675fa)

```sh
docker build -t my-web-app .
```

### 4. Push Image to Docker Hub with Tags
Tag and push the image with at least three versions:

![4](https://github.com/user-attachments/assets/29d3a90a-54af-432d-b6a6-feda0c64864f)
![5](https://github.com/user-attachments/assets/c0ae452d-713d-4ce2-aaca-e69625ebd53a)
![6](https://github.com/user-attachments/assets/155570d4-bbab-4ef0-95c5-b69fb799aeeb)
![7](https://github.com/user-attachments/assets/7fa55401-e69e-4511-a9bf-e18b28aa5e5d)


```sh
docker tag my-web-app mydockerhubusername/my-web-app:v1.0

docker tag my-web-app mydockerhubusername/my-web-app:latest

docker push mydockerhubusername/my-web-app:v1.0

docker push mydockerhubusername/my-web-app:latest
```

### 5. Run the Docker Container

```sh
docker run -d -p 5000:5000 --name web-container my-web-app
```
Access the application at `http://localhost:5000`.

![8](https://github.com/user-attachments/assets/d9b2b3ed-01a2-4f32-9994-df5f899d1c84)
![9](https://github.com/user-attachments/assets/479670c8-70c1-4740-93e1-75c099b6c352)
![10](https://github.com/user-attachments/assets/b3ece432-1735-4c8e-aa34-58189fac6364)

### 6. Start an Nginx Container

```sh
docker run -d --name nginx-container -p 8080:80 nginx
```

![11](https://github.com/user-attachments/assets/3a3fae71-47cf-472b-ab33-c537d9ad480d)
![12](https://github.com/user-attachments/assets/ddf3b676-cb1e-499b-86bc-a3f2388b5f04)

### 7. Check Connectivity Between Containers
To verify connectivity between the application and Nginx:

```sh
docker exec -it web-container sh
ping nginx-container
```

![13](https://github.com/user-attachments/assets/7e2c1ee4-c5eb-4e2f-9a67-9476c3ecfa56)


### 8. Push Everything to GitHub
The project is available on [GitHub](https://github.com/krishnamonani/docker-assignment-1).
The repository includes:

- `Dockerfile`
- `app.py`
- `requirements.txt`
- `README.md`
- `screenshots/` (folder containing all screenshots of steps)

## Notes
- No existing applications from labs were used.
- Environment variables are not hardcoded.
- Screenshots for each step are included in the repository.

## Conclusion
This project showcases the ability to containerize a simple web application, optimize the image size, deploy using Docker, and establish connectivity between containers using Nginx.

