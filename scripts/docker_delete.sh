#!/bin/bash

# Stop and remove containers defined in the docker-compose.yaml.
# Should be run from the root of the project.


echo "[*] Deleting docker containers..."
docker compose down
# down:     Use the docker compose down command to stop and remove
#           the containers defined in the docker-compose.yaml file.

# Check that deleting was successful:
if [ $? -eq 0 ]; then
    echo "[✔] Deleting docker containers: Success."
else
    echo "[✘] Deleting docker containers: Error. Try manual."
fi
