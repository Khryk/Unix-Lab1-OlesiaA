#!/bin/bash

echo "Stopping old container..."
docker stop my-flask-container 2>/dev/null || true
docker rm my-flask-container 2>/dev/null || true

echo "Building Docker image..."
docker build -t my-flask-app .

echo "Running container..."
docker run -d --name my-flask-container -p 5000:5000 my-flask-app

echo "App is running at http://localhost:5000/OlesiaALab1"
