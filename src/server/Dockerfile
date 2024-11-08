# Base Image: This line specifies that the Docker image being created
# should be based on the official python:3.12 image from Docker Hub.
# This image includes Python 3.12 with a minimal setup that is sufficient
# for most applications.
FROM python:3.12

# Working Directory: This line sets the working directory within the
# container to /app. All subsequent commands in the Dockerfile will
# be executed in this directory.
WORKDIR /app

# Copy Application Source Code: This command copies the content of the
# ./ directory from the host into the /app directory of the
# container. This includes application code, which Uvicorn will run.
# We want to exclude several files to be copied - Check .dockerignore.
COPY . /app/

# Install Dependencies: This command runs inside the container, using pip
# to install the packages specified in the requirements.txt file. 
# --no-cache-dir: This option tells pip not to cache the downloaded
# packages, reducing the image size.
# --upgrade: This option ensures that all packages are updated to their
# latest versions (lets not use it a while - to be shure it works).
# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
