FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

# Set the working directory to /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5555
