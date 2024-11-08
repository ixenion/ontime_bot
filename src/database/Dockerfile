# Official PostgreSQL image, specifically version 16.3.
FROM postgres:16.3

# Working Directory: This line sets the working directory within the
# container to /app. All subsequent commands in the Dockerfile will
# be executed in this directory.
WORKDIR /app

# Copy Application scripts: This command copies the content of the
# ./ directory from the host into the /app directory in the
# container. This includes your application code, which Uvicorn will run.
# We want to exclude several files to be copied - Check .dockerignore.
COPY ./* /app/
# Another way - exclude
# COPY --exclude=venv ./* /app/

# Run script which creates DB table
COPY init.sql /docker-entrypoint-initdb.d/

# Database Initialization: This is the moment right after the container
# checks if the data directory is empty. If it is empty, PostgreSQL will
# create a new database cluster (the filesystem structure that PostgreSQL
# uses to store its databases). At this point, it will run any scripts
# found in /docker-entrypoint-initdb.d/.

# The scripts in /docker-entrypoint-initdb.d/ only run when:
# 1. The PostgreSQL data directory is not previously initialized (i.e.,
# it does not contain a PG_VERSION file). This usually means that if you
# have integrated a bind mount (like covering a local directory) and that
# directory has not been used before, the script will run during the first
# startup.
# 2. Start the container with a clean environment or a new volume.
# If you delete the volume or the data directory is empty when you start
# the container, the scripts will run.
