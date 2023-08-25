# image name: dch-env
# VERSION     4

# The build tools is available in this base image
FROM continuumio/anaconda3:2023.07-1
LABEL maintainer="bo.yan@csiro.au"

# change to python 3.9
RUN /opt/conda/bin/conda create -y -n python3.9 python==3.9.11
ENV PATH=/opt/conda/envs/python3.9/bin:$PATH 

WORKDIR /setup

ADD requirements.txt /setup

RUN pip install -r /setup/requirements.txt

VOLUME /app
WORKDIR /app

EXPOSE 5000