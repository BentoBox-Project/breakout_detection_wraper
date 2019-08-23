## Base image https://hub.docker.com/u/rocker/
FROM rocker/r-base:latest

LABEL Description="Python + R Breakout detection"

## Install the C/C++ libraries needed to run the script
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev


## Install Python
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip 

RUN echo "root:root" | chpasswd

RUN pip3 install pipenv

## Set working dir
RUN mkdir -p /app
WORKDIR /app

COPY dependencies dependencies
RUN pipenv --version

RUN cd dependencies && pipenv lock --requirements > requirements.txt
RUN pip3 install --no-cache-dir -r dependencies/requirements.txt

## install R-packages
RUN Rscript dependencies/install_packages.R

## copy everything from the current directory into the container
COPY . .

## Run the Scripts
RUN cd scripts && python3 main.py

