# Base image https://hub.docker.com/u/rocker/
FROM rocker/r-base:latest

LABEL Description="Python + R Breakout detection"

# Install the C/C++ libraries needed to run the script
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  libssl-dev \
  libcurl4-openssl-dev \
  libxml2-dev

# Install Python
RUN apt-get update

RUN apt-get install -y python3 python3-dev python3-pip

RUN echo "root:root" | chpasswd

# install Python dependencies
RUN pip3 install pipenv

COPY Pipfile* /tmp/

COPY install_packages.R /tmp/

RUN cd /tmp/ && pipenv lock --requirements > requirements.txt

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# install R-packages
RUN Rscript /tmp/install_packages.R

# Set working dir
RUN mkdir -p /app

WORKDIR /app

# copy everything from the current directory into the container
COPY . .

RUN useradd --create-home ruser

USER ruser

CMD [ "python3", "-m", "breakout_detection_wraper" ]
