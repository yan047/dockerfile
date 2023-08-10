# image name: dch-env
# VERSION     3

# The build tools is available in this base image
FROM amancevice/pandas:2.0.0
LABEL maintainer="bo.yan@csiro.au"

WORKDIR /setup

ADD requirements.txt /setup

RUN pip install -r /setup/requirements.txt

VOLUME /app
WORKDIR /app

EXPOSE 5000