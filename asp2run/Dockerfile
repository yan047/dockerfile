# Version: 1
# Name: asp2run
FROM microsoft/aspnetcore:2.0.6

MAINTAINER "boyan.au@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && \
    apt-get -qq -y install libgdiplus && \
    apt-get -qq -y install procps && \
    apt-get -qq -y install vim
