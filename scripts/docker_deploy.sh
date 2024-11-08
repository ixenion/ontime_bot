#!/bin/bash

# Deploys and starts containers defined in the docker-compose.yaml.
# Should be run from the root of the project.


echo "[*] Deploying docker containers..."
docker compose up --build -d
# up:       This command starts the services defined in docker-compose.yml
#           file. It creates and starts containers, networks,
#           and volumes as needed.
# --build:  This option forces the rebuilding of images for the services
#           defined in docker-compose.yml file. If there have been changes
#           to the Dockerfile or the files in the build context, this
#           ensures that you are using the latest version of your images.
# -d:       Detached mode: Run containers in the background.

# Check that deploy was successful:
if [ $? -eq 0 ]; then
    echo "[✔] Deploying docker containers: Success."
else
    echo "[✘] Deploying docker containers: Error. Try start."
fi
