# Version: 5.0.5
FROM ubuntu:18.04

MAINTAINER "boyan.au@gmail.au"

ENV DEBIAN_FRONTEND noninteractive
ARG WORKSPACE_DEB=csiro.au-workspace.deb
ARG CMAKE_INSTALL=cmake-3.11.3-Linux-x86_64.sh

WORKDIR /app

# In case someone loses the Dockerfile
RUN rm -rf /etc/Dockerfile
ADD Dockerfile /etc/Dockerfile

RUN apt-get -qq update && \
    apt-get -qq -y install wget unzip vim libzmq3-dev libglu1-mesa libglib2.0-0 libnss3 libxcomposite-dev libxcursor-dev libxtst6 libxi6 libxss1 libfontconfig1 libxrandr2 libdbus-1-3 libasound2 libegl1 build-essential libgl1-mesa-dev libsm6 && \
    apt-get -qq -y autoremove && \
    apt-get -qq -y autoclean

# install workspace
RUN wget https://ws.data.csiro.au/collections/csiro:11028/data/5267714  --output-document=$WORKSPACE_DEB && \
    dpkg -i /app/$WORKSPACE_DEB && \
    apt-get install -f

# fix an issue of libz version complain

RUN cd /opt/csiro.au/workspace/lib/ && \
    mv libz.so.1 libz.so.1.old && \
    ln -s /lib/x86_64-linux-gnu/libz.so.1

# install cmake

RUN mkdir ~/tmp && cd ~/tmp && \
    wget https://cmake.org/files/v3.11/$CMAKE_INSTALL && \
    chmod +x $CMAKE_INSTALL && \
    ./$CMAKE_INSTALL --skip-license --prefix=/usr && \
    cd /app && rm -rf ~/tmp
