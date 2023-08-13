FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

# Set the working directory to /app
WORKDIR /app

# # Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable for Celery worker
ENV C_FORCE_ROOT="true"

# Expose Flower and Celery Beat ports
EXPOSE 5555 5556 6379

# Run the command when the container launches
CMD celery -A celery_worker:app worker --loglevel=info & \
    celery -A celery_worker:app beat --loglevel=info & \
    celery -A celery_worker.app flower & \
    wait