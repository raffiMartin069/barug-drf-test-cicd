import gdown
import os

try:
    docker = os.getenv("DOCKERFILE_URL", "")
    nginx = os.getenv("NGINX_URL", "")
    gdown.download(docker, output="../nginx.conf", quiet=False)
    print("Dockerfile downloaded successfully.")
    gdown.download(nginx, output="../Dockerfile", quiet=False)
    print("Nginx configuration downloaded successfully.")
except Exception as e:
    print(f"Error retrieving environment variables: {e}")
    raise ValueError("Environment variables DOCKERFILE_URL and NGINX_URL must be set.")

