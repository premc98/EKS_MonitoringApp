# Mini Flask Monitoring app on EKS

Flask based monitoring application & containerized it using Dockerfile. Created
Kubernetes Deployments & Service YAMLs using the image on ECR & hosted it on EKS cluster

1. create requirements.txt
2. pip3 install --no-cache-dir -r requirements.txt (To install all dependencies)
3. Create index.html in templates
4. Create app.py with set api routes and rendering on frontend
5. Run and test it locally python3 app.py
6. Create Dockerfile
7. Build docker image - docker build -t my-flask-app:v1 .
8. run docker image and publish port - docker run -d -p 5010:5010 --name FlaskAppContainer my-flask-app:v1
9. to attach a shell to a running container - docker container exec -it FlaskAppContainer bash

## To clear running container:

- docker stop FlaskAppContainer
- to restart a stopped container - docker start FlaskAppContainer
- to remove a container that was created - docker rm FlaskAppContainer
- to remove the image that was used to create the container - docker rmi my-flask-app:v1
