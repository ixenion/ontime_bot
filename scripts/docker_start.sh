#!/bin/bash

# Starts containers defined in the docker-compose.yaml
# If they are created and stopped.


# Check is there any containers created
echo "Gathering created containers..."
container_status=$(docker compose ps -qa)

if [[ -z $container_status ]]; then
    echo "[✘] No containers are created. Please run 'docker_deploy.sh' first."
    exit
fi


# docker compose ps:    Show status info about containers specified in
#                       the docker-compose.yaml
# -a:       Also show stopped containers.
# -q:       Quiet - print only containers IDs.
for container in $(docker compose ps -qa);
do
    # Get container status: Running true or false
    container_name=$(docker inspect -f '{{.Name}}' $container);
    container_running=$(docker inspect -f '{{.State.Running}}' $container);
    # Check if container is already running...
    if [ "$container_running" == 'true' ]; then
        # If the container is running, skip it, move to the next.
        echo "[✔] Container $container_name alreadey running. Skipping it."
        continue
    else
        echo "[*] Starting container $container_name..."
        docker start $container
        # Check that start was successful:
        if [ $? -eq 0 ]; then
            echo "[✔] Starting container $container_name: Success."
        else
            echo "[✘] Starting container $container_name: Error. Try manual."
        fi
    fi

done
